from wtforms import Form
from wtforms import StringField, TextAreaField, PasswordField, IntegerField, SelectField, BooleanField
from wtforms import validators

class UserForm(Form):
    username = StringField('Kullanıcı Adı', [validators.Length(min=4, max=25)])
    email = StringField('E-mail Adresi', [
        validators.Length(min=6, max=500),
        validators.Email('This field requires a valid email address')
    ])
    first_name = StringField('Adı', [validators.Length(min=2, max=25)])
    middle_name = StringField('İkinci Adı', [])
    surname = StringField('Soyadı', [validators.Length(min=2, max=25)])
    role_id = SelectField('Statüsü', choices = [ ("1","İdari Personel"), ("2","Öğretmen"), ("3","Öğrenci") ])
    password = PasswordField('Şifre', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Şifre Tekrar')

class GeneralInfoForm(Form):
    tc = StringField('Tc Kimlik No', [validators.Length(min=1, max=50)])
    nationality = StringField('Uyruğu', [validators.Length(min=1, max=50)])
    gender = SelectField('Cinsiyet', choices = [ ("Kiz","Kiz"), ("Erkek","Erkek") ])
    birthplace = StringField('Doğum Yeri', [validators.Length(min=1, max=50)])
    birthdate = StringField('Doğum Tarihi', [validators.Length(min=1, max=50)])
    pension_fund = BooleanField('Emekli Sandığı (Yok,Var)?')
    military_service = BooleanField('Askerlik Hizmeti (Yapıldı, Yapılmadı)?')
    disability_status = StringField('Özür Durumu', [validators.required(),validators.Length(min=1, max=50)])
    is_want_scholarship = BooleanField('Burs İstiyor Mu? (Evet Hayır)?')
    preference_order = IntegerField('YTÜ Bilgisayar Tercih Sırası')

class HighschoolInfoForm(Form):
    school_name = StringField('Mezun Olunan Lise', [validators.Length(min=4, max=25)])
    school_department = StringField('Mezun Olunan Bölüm', [validators.Length(min=4, max=25)])
    diploma_success_note = StringField('Diploma Başarı Notu', [validators.Length(min=4, max=25)])
    diploma_course_branch = StringField('Diploma Kolu / Branşı', [validators.Length(min=4, max=25)])
    foreign_language = StringField('Yabanci Dil', [validators.Length(min=4, max=25)])

class PopulationInfoForm(Form):
    neighborhoodNvillage = StringField('Mahalle / Köy', [validators.Length(min=4, max=25)])
    population_administration = StringField('Verildiği Nüfus İdaresi', [validators.Length(min=4, max=25)])
    c_no = IntegerField('Cilt No')
    id_card_no = IntegerField('Nüfus Cüzdanı No')
    family_queue_no = IntegerField('Aile Sıra No')
    queue_no = IntegerField('Sıra No')

class UniversityInfoForm(Form):
    university_student_no = StringField('Üniversite Öğrenci No', [validators.Length(min=4, max=25)])
    faculty = StringField('Fakülte / MYO', [validators.Length(min=4, max=25)])
    department = SelectField('Bölüm / Program', choices = [
        ("BilgisayarMuh","Bilgisayar Muhendisligi"),
        ("ElektrikMuh","Elektrik Muhendisligi")
    ])
    teaching_style = SelectField('Öğretim Şekli', choices = [ ("Orgun","Örgun Öğretim"), ("2.ci Ogretim","2.ci Öğretim") ])
    student_score = IntegerField('Öss Puanı')
    completed_yok = StringField('Tamamlanan Yök', [validators.Length(min=4, max=25)])