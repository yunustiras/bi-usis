from werkzeug.security import generate_password_hash, check_password_hash

from run import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    middle_name = db.Column(db.String(80))
    surname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    photoname = db.Column(db.String(120), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref=db.backref('users', lazy=True))
    general_info = db.relationship('GeneralInfo', backref=db.backref('users', lazy=True))
    highschool_info = db.relationship('HighschoolInfo', backref=db.backref('users', lazy=True))
    population_info = db.relationship('PopulationInfo', backref=db.backref('users', lazy=True))
    university_info = db.relationship('UniversityInfo', backref=db.backref('users', lazy=True))
    family = db.relationship('Family', backref=db.backref('users', lazy=True))
    interests = db.relationship('Interests', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return "<User {0!r}>".format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(25), nullable=False)
    field = db.Column(db.String(25), nullable=False)
    value = db.Column(db.String(25), nullable=False)
    time = db.Column(db.String(25), nullable=False)
    ip = db.Column(db.String(20), nullable=False)
    object_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('logs', lazy=True))

    def __repr__(self):
        return "<Log {0!r}>".format(self.id)

class GeneralInfo(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    tc = db.Column(db.String(11), unique=True, nullable=False)  # TC --
    nationality = db.Column(db.String(11), nullable=False)      # Uyruğu
    gender = db.Column(db.String(11), nullable=False)           # Cinsiyet
    birthplace = db.Column(db.String(11), nullable=False)       # Dogum yeri --
    birthdate = db.Column(db.String(11), nullable=False)        # Dogum tarihi --
    pension_fund = db.Column(db.Boolean, nullable=False)        # Emekli Sandığı (Yok,Var)
    military_service = db.Column(db.Boolean, nullable=False)    # Askerlik Hizmeti (Yapıldı, Yapılmadı)
    disability_status = db.Column(db.String(11), nullable=False)# Özür Durumu
    preference_order = db.Column(db.Integer, nullable=False)    # YTÜ Bilgisayar Tercih Sırası
    is_want_scholarship = db.Column(db.Boolean, nullable=False) # Burs İstiyor Mu? (Evet Hayır)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "<StudentGeneralInfo {0!r}>".format(self.id)

class HighschoolInfo(db.Model): # Mezun Olunan Lise Bilgileri
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(120), nullable=False)             # Mezun Olunan Lise --
    school_department = db.Column(db.String(25), nullable=False)        # Mezun Olunan Bölüm --
    diploma_success_note = db.Column(db.String(11), nullable=False)     # Diploma Başarı Notu --
    diploma_course_branch = db.Column(db.String(11), nullable=False)    # Diploma Kolu / Branşı --
    foreign_language = db.Column(db.String(11), nullable=False)         # Yabanci Dil --
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "<StudentHighschoolInfo {0!r}>".format(self.id)

class PopulationInfo(db.Model): # Nüfus Bilgileri
    id = db.Column(db.Integer, primary_key=True)
    neighborhoodNvillage = db.Column(db.String(120), nullable=False)     # Mahalle / Köy --
    population_administration = db.Column(db.String(25), nullable=False) # Verildiği Nüfus İdaresi --
    c_no = db.Column(db.Integer, nullable=False)                         # Cilt No
    id_card_no = db.Column(db.Integer, nullable=False)                   # Nüfus Cüzdanı No --
    family_queue_no = db.Column(db.Integer, nullable=False)              # Aile Sıra No --
    queue_no = db.Column(db.Integer, nullable=False)                     # Sıra No --
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "<StudentPopulationInfo {0!r}>".format(self.id)

class UniversityInfo(db.Model): # Universite Bilgileri
    id = db.Column(db.Integer, primary_key=True)
    university_student_no = db.Column(db.Integer, nullable=False)   # Üniversite Öğrenci No
    faculty = db.Column(db.String(25), nullable=False)              # Fakülte / MYO
    department = db.Column(db.String(120), nullable=False)          # Bölüm / Program
    teaching_style = db.Column(db.String(120), nullable=False)      # Öğretim Şekli --
    student_score = db.Column(db.Integer, nullable=False)           # Öss Puanı --
    completed_yok = db.Column(db.String(120), nullable=False)       # Tamamlanan Yök --
    preferences = db.relationship('UniversityPreferences', backref=db.backref('university_info', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "<StudentUniversityInfo {0!r}>".format(self.id)

class UniversityPreferences(db.Model): # Universite Tercihleri
    id = db.Column(db.Integer, primary_key=True)
    preference_index = db.Column(db.Integer, nullable=False)   # Tercih sirasi
    preference_name = db.Column(db.String(25), nullable=False) # Tercih edilen universite
    university_info_id = db.Column(db.Integer, db.ForeignKey('university_info.id'), nullable=False)

    def __repr__(self):
        return "<StudentUniversityPreferences {0!r}>".format(self.id)

class Interests(db.Model): # Ilgileri
    id = db.Column(db.Integer, primary_key=True)
    interest_name = db.Column(db.String(25), nullable=False) # Ilgisi | Select ile secilirse iyi olur.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "<Interests {0!r}>".format(self.id)

class Family(db.Model): # Aile
    id = db.Column(db.Integer, primary_key=True)
    monthly_income_level = db.Column(db.Integer, nullable=False) # Aile Aylık Gelir Düzeyi
    persons = db.relationship('OtherPersons', backref=db.backref('familys', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "<Family {0!r}>".format(self.id)

class OtherPersons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)   # Ismi
    gender = db.Column(db.String(16), nullable=False)       # Cinsiyeti
    job = db.Column(db.String(80), nullable=False)          # Isi
    marial_status = db.Column(db.String(25), nullable=False)# Evlilik durumu
    education = db.Column(db.String(25), nullable=False)    # Ogretim durumu
    email = db.Column(db.String(16), nullable=False)        # Email
    birthdate = db.Column(db.String(11), nullable=False)    # Dogum tarihi --
    death_date = db.Column(db.String(11), nullable=False)   # Olum tarihi --
    phone_id = db.Column(db.Integer, db.ForeignKey('phone.id'), nullable=True)     # Telefon numarasi
    phone = db.relationship('Phone', backref=db.backref('persons', lazy=True))
    family_id = db.Column(db.Integer, db.ForeignKey('family.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('person_type.id'), nullable=False)    # Ogrencinin neyi
    type_ = db.relationship('PersonType', backref=db.backref('persons', lazy=True))

    def __repr__(self):
        return '<OtherPersons {0!r}>'.format(self.id)

class PersonType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<PersonType {0!r}>'.format(self.id)

class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('person_type.id'), nullable=False)

    def __repr__(self):
        return '<Emails {0!r}>'.format(self.id)

class Addresses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('person_type.id'), nullable=False)

    def __repr__(self):
        return '<Addresses {0!r}>'.format(self.id)

class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('person_type.id'), nullable=False)

    def __repr__(self):
        return '<Phone {0!r}>'.format(self.id)