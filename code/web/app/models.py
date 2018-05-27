from run import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    funcs = db.relationship('RoleFuncs', backref=db.backref('users', lazy=True))

    def access(self, query):
        for func in self.funcs:
            if func.name == query:
                return True
        return False

    def __repr__(self):
        return '<Role {0!r}>'.format(self.name)

class RoleFuncs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    def __repr__(self):
        return '<RoleFuncs {0!r}>'.format(self.id)

class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consultancy_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(80), nullable=False)
    create_date = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Opinion %r>' % self.consultancy_id

class Consultancy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<Consultancy %r>' % self.teacher_id

def get_mysql_info():
    querys = [ "select version();", "show tables;", "show databases;" ]
    data = {}
    for query in querys:
        result  = db.engine.execute(query)
        data[query] = []
        for row in result:
            data[query].append(row[0])

    return data
