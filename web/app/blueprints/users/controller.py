from datetime import datetime
from flask import current_app, g

from run import db
from app.blueprints.users.models import (
    User,
    GeneralInfo,
    HighschoolInfo,
    PopulationInfo,
    UniversityInfo,
    Log
)

def create_new_log(model, field, value, object_id):
    time = datetime.now()
    log = Log(
        model=model,
        field=field,
        value=value,
        time=time,
        ip=g.user_context['ip'],
        object_id=object_id,
        user_id=g.user_context['user'].id
    )
    db.session.add(log)
    db.session.commit()

def create_new_user(uname, password, fname, mname, sname, email, role_id):
    user = User(
        username=uname,
        email=email,
        first_name=fname,
        middle_name=mname,
        surname=sname,
        role_id=role_id
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    current_app.logger.info(fname)
    return user

def update_login_info(user, username, email, first_name, middle_name, surname, password, role_id):
    if user.username != username:
        create_new_log('User', 'username', user.username, user.id)
        user.username = username

    if user.email != email:
        create_new_log('User', 'email', user.email, user.id)
        user.email = email

    if user.first_name != first_name:
        create_new_log('User', 'first_name', user.first_name, user.id)
        user.first_name = first_name

    if user.middle_name != middle_name:
        create_new_log('User', 'middle_name', user.middle_name, user.id)
        user.middle_name = middle_name

    if user.surname != surname:
        create_new_log('User', 'surname', user.surname, user.id)
        user.surname = surname

    if user.role_id != role_id:
        create_new_log('User', 'role_id', user.role_id, user.id)
        user.role_id = role_id

    user.set_password(password)
    db.session.commit()

def create_general_info(user_id,
                        tc,
                        nationality,
                        gender,
                        birthplace,
                        birthdate,
                        pension_fund,
                        military_service,
                        disability_status,
                        preference_order,
                        is_want_scholarship):
    new_user_general_info = GeneralInfo(
        tc=tc,
        nationality=nationality,
        gender=gender,
        birthplace=birthplace,
        birthdate=birthdate,
        pension_fund=pension_fund,
        military_service=military_service,
        disability_status=disability_status,
        preference_order=preference_order,
        is_want_scholarship=is_want_scholarship,
        user_id = user_id
    )
    db.session.add(new_user_general_info)
    db.session.commit()

def update_general_info(general_info,
                        tc,
                        nationality,
                        gender,
                        birthplace,
                        birthdate,
                        pension_fund,
                        military_service,
                        disability_status,
                        preference_order,
                        is_want_scholarship):
    general_info.tc = tc
    general_info.nationality = nationality
    general_info.gender = gender
    general_info.birthplace = birthplace
    general_info.birthdate = birthdate
    general_info.pension_fund = pension_fund
    general_info.military_service = military_service
    general_info.disability_status = disability_status
    general_info.preference_order = preference_order
    general_info.is_want_scholarship = is_want_scholarship
    db.session.commit()

def create_highschool_info(user_id,
                        school_name,
                        school_department,
                        diploma_success_note,
                        diploma_course_branch,
                        foreign_language):
    new_user_highschool_info = HighschoolInfo(
        school_name=school_name,
        school_department=school_department,
        diploma_success_note=diploma_success_note,
        diploma_course_branch=diploma_course_branch,
        foreign_language=foreign_language,
        user_id = user_id
    )
    db.session.add(new_user_highschool_info)
    db.session.commit()

def update_highschool_info(highschool_info,
                        school_name,
                        school_department,
                        diploma_success_note,
                        diploma_course_branch,
                        foreign_language):
    highschool_info.school_name = school_name
    highschool_info.school_department = school_department
    highschool_info.diploma_success_note = diploma_success_note
    highschool_info.diploma_course_branch = diploma_course_branch
    highschool_info.foreign_language = foreign_language
    db.session.commit()
    
def create_population_info(user_id,
                        neighborhoodNvillage,
                        population_administration,
                        c_no,
                        id_card_no,
                        family_queue_no,
                        queue_no):
    new_user_population_info = PopulationInfo(
        neighborhoodNvillage=neighborhoodNvillage,
        population_administration=population_administration,
        c_no=c_no,
        id_card_no=id_card_no,
        family_queue_no=family_queue_no,
        queue_no=queue_no,
        user_id = user_id
    )
    db.session.add(new_user_population_info)
    db.session.commit()

def update_population_info(population_info,
                        neighborhoodNvillage,
                        population_administration,
                        c_no,
                        id_card_no,
                        family_queue_no,
                        queue_no):
    population_info.neighborhoodNvillage = neighborhoodNvillage
    population_info.population_administration = population_administration
    population_info.c_no = c_no
    population_info.id_card_no = id_card_no
    population_info.family_queue_no = family_queue_no
    population_info.queue_no = queue_no
    db.session.commit()

def create_university_info(user_id,
                        university_student_no,
                        faculty,
                        department,
                        teaching_style,
                        student_score,
                        completed_yok):
    new_user_university_info = UniversityInfo(
        university_student_no=university_student_no,
        faculty=faculty,
        department=department,
        teaching_style=teaching_style,
        student_score=student_score,
        completed_yok=completed_yok,
        user_id = user_id
    )
    db.session.add(new_user_university_info)
    db.session.commit()

def update_university_info(university_info,
                        university_student_no,
                        faculty,
                        department,
                        teaching_style,
                        student_score,
                        completed_yok):
    university_info.university_student_no = university_student_no
    university_info.faculty = faculty
    university_info.department = department
    university_info.teaching_style = teaching_style
    university_info.student_score = student_score
    university_info.completed_yok = completed_yok
    db.session.commit()