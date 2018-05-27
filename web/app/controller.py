from run import db
from app.models import Opinion, Consultancy

def create_opinion(consultancy_id, content, create_date):
    new_opinion = Opinion(
        consultancy_id = consultancy_id,
        content = content,
        create_date = create_date
    )

    db.session.add(new_opinion)
    db.session.commit()

def create_consultancy_relation(teacher_id, student_id):
    new_consultancy_relation = Consultancy(
        teacher_id = teacher_id,
        student_id = student_id
    )

    db.session.add(new_consultancy_relation)
    db.session.commit()
