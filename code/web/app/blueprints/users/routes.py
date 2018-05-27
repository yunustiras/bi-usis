import hashlib, os
from werkzeug import secure_filename
from flask import (
    Blueprint,
    render_template,
    g,
    redirect,
    url_for,
    request,
    flash,
    current_app,
    send_file
)
from app.decorators import (
    is_logged_in,
    is_personal,
    is_teacher
)
from app.blueprints.users import controller
from app.blueprints.users.models import (
    User,
    GeneralInfo,
    HighschoolInfo,
    PopulationInfo,
    Log
)
from app.blueprints.users.forms import (
    UserForm,
    GeneralInfoForm,
    HighschoolInfoForm,
    PopulationInfoForm,
    UniversityInfoForm
)
from run import db

users = Blueprint('users', __name__, template_folder='templates', url_prefix='/users')

PER_PAGE = 3

@users.route('/', methods=["GET"])
@is_logged_in
def home():
    page = request.args.get('page', 1, type=int)
    all_users = User.query.paginate(page=page, per_page=PER_PAGE)
    return render_template("users.html", users=all_users, context=g.user_context)

@users.route('/<int:user_id>', methods=["GET"])
@is_logged_in
def show_user(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    return render_template("user/show.html", context=g.user_context, user=user)

@users.route('/<int:user_id>/photo/edit', methods = ['GET', 'POST'])
@is_logged_in
def update_photo(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    if request.method == 'POST':
        f = request.files['file']
        current_app.logger.info(f.filename)
        secure_name = secure_filename(f.filename)
        extension = secure_name[-4:]
        hash_value = hashlib.md5(secure_name.encode()).hexdigest()
        # Burda static dizine versek cok iyi olur.
        file_path = "/tmp/{}{}".format(hash_value, extension)
        current_app.logger.info(file_path)
        f.save(file_path)
        user.photoname = "{}{}".format(hash_value, extension)
        db.session.commit()
        return 'file uploaded successfully'
        #return redirect(url_for('users.show_user', user_id=user_id))

    return render_template('user/upload_photo.html', context=g.user_context)

@users.route('/<int:user_id>/photo')
@is_logged_in
def return_file(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    try:
        return send_file("/tmp/{}".format(user.photoname), attachment_filename=user.photoname)
    except Exception as e:
        return str(e)

@users.route('/<int:user_id>/university_info', methods=["GET"])
@is_logged_in
def show_user_university_info(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    return render_template("user/university_info/show.html", context=g.user_context, user=user)

@users.route('/<int:user_id>/university_info/edit', methods = ['GET', 'POST'])
@is_logged_in
def edit_user_university_info(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    form = UniversityInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        # Update Edilmeli ve Log yazilmali.
        current_app.logger.info("validated")
        controller.update_university_info(
            university_info=user.university_info[0],
            university_student_no=form.university_student_no.data,
            faculty=form.faculty.data,
            department=form.department.data,
            teaching_style=form.teaching_style.data,
            student_score=form.student_score.data,
            completed_yok=form.completed_yok.data
        )
        flash('Universite Bilgileri guncellendi.')
        return redirect(url_for('users.show_user_university_info', user_id=user_id))

    form.university_student_no.data = str(user.university_info[0].university_student_no)
    form.faculty.data = user.university_info[0].faculty
    form.department.data = user.university_info[0].department
    form.student_score.data = user.university_info[0].student_score
    form.teaching_style.data = user.university_info[0].teaching_style
    form.completed_yok.data = user.university_info[0].completed_yok
    return render_template('user/university_info/edit.html', context=g.user_context, form=form, user=user)


@users.route('/<int:user_id>/population_info', methods=["GET"])
@is_logged_in
def show_user_population_info(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template("user/population_info/show.html", context=g.user_context, user=user)

@users.route('/<int:user_id>/population_info/edit', methods = ['GET', 'POST'])
@is_logged_in
def edit_user_population_info(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    form = PopulationInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        controller.update_population_info(
            population_info=user.population_info[0],
            neighborhoodNvillage=form.neighborhoodNvillage.data,
            population_administration=form.population_administration.data,
            c_no=form.c_no.data,
            id_card_no=form.id_card_no.data,
            family_queue_no=form.family_queue_no.data,
            queue_no=form.queue_no.data
        )
        flash('Nufus Bilgileri guncellendi.')
        return redirect(url_for('users.show_user_population_info', user_id=user_id))

    form.c_no.data = user.population_info[0].c_no
    form.family_queue_no.data = user.population_info[0].family_queue_no
    form.id_card_no.data = user.population_info[0].id_card_no
    form.neighborhoodNvillage.data = user.population_info[0].neighborhoodNvillage
    form.population_administration.data = user.population_info[0].population_administration
    form.queue_no.data = user.population_info[0].queue_no
    return render_template('user/population_info/edit.html', context=g.user_context, form=form, user=user)

@users.route('/<int:user_id>/highschool_info', methods=["GET"])
@is_logged_in
def show_user_highschool_info(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    return render_template("user/highschool_info/show.html", context=g.user_context, user=user)

@users.route('/<int:user_id>/highschool_info/edit', methods = ['GET', 'POST'])
@is_logged_in
def edit_user_highschool_info(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    form = HighschoolInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        current_app.logger.info("form validated!")
        controller.update_highschool_info(
            highschool_info=user.highschool_info[0],
            school_name=form.school_name.data,
            school_department=form.school_department.data,
            diploma_success_note=form.diploma_success_note.data,
            diploma_course_branch=form.diploma_course_branch.data,
            foreign_language=form.foreign_language.data
        )
        flash('Lise Bilgileri guncellendi.')
        return redirect(url_for('users.show_user_highschool_info', user_id=user_id))

    form.diploma_course_branch.data = user.highschool_info[0].diploma_course_branch
    form.diploma_success_note.data = user.highschool_info[0].diploma_success_note
    form.school_name.data = user.highschool_info[0].school_name
    form.school_department.data = user.highschool_info[0].school_department
    form.foreign_language.data = user.highschool_info[0].foreign_language
    return render_template('user/highschool_info/edit.html', context=g.user_context, form=form, user=user)

@users.route('/<int:user_id>/general_info', methods=["GET"])
@is_logged_in
def show_user_general_info(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template("user/general_info/show.html", context=g.user_context, user=user)

@users.route('/<int:user_id>/general_info/edit', methods = ['GET', 'POST'])
@is_logged_in
def edit_user_general_info(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    form = GeneralInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        current_app.logger.info("form validated!")
        controller.update_general_info(
            general_info=user.general_info[0],
            tc=form.tc.data,
            nationality=form.nationality.data,
            gender=form.gender.data,
            birthplace=form.birthplace.data,
            birthdate=form.birthdate.data,
            pension_fund=form.pension_fund.data,
            military_service=form.military_service.data,
            disability_status=form.disability_status.data,
            preference_order=form.preference_order.data,
            is_want_scholarship=form.is_want_scholarship.data
        )
        flash('Kişisel Bilgileri guncellendi.')
        return redirect(url_for('users.show_user_general_info', user_id=user_id))

    form.tc.data = user.general_info[0].tc
    form.nationality.data = user.general_info[0].nationality
    form.gender.data = user.general_info[0].gender
    form.birthplace.data = user.general_info[0].birthplace
    form.birthdate.data = user.general_info[0].birthdate
    form.pension_fund.data = user.general_info[0].pension_fund
    form.disability_status.data = user.general_info[0].disability_status
    form.is_want_scholarship.data = user.general_info[0].is_want_scholarship
    form.military_service.data = user.general_info[0].military_service
    form.preference_order.data = user.general_info[0].preference_order
    return render_template('user/general_info/edit.html', context=g.user_context, form=form, user=user)

@users.route('/<int:user_id>/login_info/log/<string:field>/<int:object_id>', methods=["GET"])
@is_logged_in
def show_user_login_info_in_log(user_id, field, object_id):
    logs = Log.query.filter_by(model='User').filter_by(field=field).filter_by(object_id=object_id).all()
    return render_template("logs.html", context=g.user_context, logs=logs)

@users.route('/<int:user_id>/login_info', methods=["GET"])
@is_logged_in
def show_user_login_info(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    return render_template("user/login_info/show.html", context=g.user_context, user=user)

@users.route('/<int:user_id>/login_info/edit', methods = ['GET', 'POST'])
@is_logged_in
def edit_user_login_info(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()

    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        # Burada mapper fonksiyo yazilmali.
        controller.update_login_info(
            user=user,
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            middle_name=form.middle_name.data,
            surname=form.surname.data,
            password=form.password.data,
            role_id=int(form.role_id.data)
        )
        flash("Giriş Bilgileri guncellendi.")
        return redirect(url_for('users.show_user_login_info', user_id=user.id))

    # Burada mapper fonksiyon yazilmali.
    form.username.data = user.username
    form.email.data = user.email
    form.first_name.data = user.first_name
    form.middle_name.data = user.middle_name
    form.surname.data = user.surname
    form.role_id.data = str(user.role_id)

    return render_template('user/login_info/edit.html', context=g.user_context, form=form, user=user)

@users.route('/auto_create', methods = ['GET', 'POST'])
@is_logged_in
def auto_create_users():
    if request.method == 'POST':
        file = request.files['file']
        myfile = file.read()

        myfile_json = eval(myfile.decode())
        for new_user in myfile_json['users']:
            new_user_general_info = new_user.get('general_info', None)
            new_user_highschool_info = new_user.get('highschool_info', None)
            new_user_population_info = new_user.get('population_info', None)
            new_user_university_info = new_user.get('university_info', None)
            try:
                created_user = controller.create_new_user(
                    new_user['username'],
                    new_user['password'],
                    new_user['first_name'],
                    new_user['middle_name'],
                    new_user['surname'],
                    new_user['email'],
                    int(new_user['role_id'])
                )
                if new_user_general_info:
                    created_user_general_info = controller.create_general_info(
                        user_id=created_user.id,
                        tc=new_user_general_info['tc'],
                        nationality=new_user_general_info['nationality'],
                        gender=new_user_general_info['gender'],
                        birthplace=new_user_general_info['birthplace'],
                        birthdate=new_user_general_info['birthdate'],
                        pension_fund=bool(new_user_general_info['pension_fund']),
                        military_service=bool(new_user_general_info['military_service']),
                        disability_status=new_user_general_info['disability_status'],
                        preference_order=new_user_general_info['preference_order'],
                        is_want_scholarship=bool(new_user_general_info['is_want_scholarship'])
                    )
                if new_user_highschool_info:
                    created_user_highschool_info = controller.create_highschool_info(
                        user_id=created_user.id,
                        school_name=new_user_highschool_info['school_name'],
                        school_department=new_user_highschool_info['school_department'],
                        diploma_success_note=new_user_highschool_info['diploma_success_note'],
                        diploma_course_branch=new_user_highschool_info['diploma_course_branch'],
                        foreign_language=new_user_highschool_info['foreign_language']
                    )
                if new_user_population_info:
                    created_user_population_info = controller.create_population_info(
                        user_id=created_user.id,
                        neighborhoodNvillage=new_user_population_info['neighborhoodNvillage'],
                        population_administration=new_user_population_info['population_administration'],
                        c_no=new_user_population_info['c_no'],
                        id_card_no=new_user_population_info['id_card_no'],
                        family_queue_no=new_user_population_info['family_queue_no'],
                        queue_no=new_user_population_info['queue_no']
                    )
                if new_user_university_info:
                    created_user_university_info = controller.create_university_info(
                        user_id=created_user.id,
                        university_student_no=new_user_university_info['university_student_no'],
                        faculty=new_user_university_info['faculty'],
                        department=new_user_university_info['department'],
                        teaching_style=new_user_university_info['teaching_style'],
                        student_score=new_user_university_info['student_score'],
                        completed_yok=new_user_university_info['completed_yok']
                    )
            except Exception as e:
                current_app.logger.info("Error: {}".format(e))
                flash("Duplicate user! {}".format(new_user['username']))
                return redirect(url_for('users.auto_create_users'))

        flash("Created User")
        return redirect(url_for('users.home'))

    if request.method == 'GET':
        return render_template('auto_create_users.html', context=g.user_context)


@users.route('/create', methods = ['GET', 'POST'])
@is_logged_in
@is_personal
def create():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            controller.create_new_user(
                form.username.data,
                form.password.data,
                form.first_name.data,
                form.middle_name.data,
                form.surname.data,
                form.email.data,
                int(form.role_id.data),
            )
        except Exception as e:
            flash("This username was taken")
            return render_template('user/create.html', context=g.user_context, form=form)

        flash("Created User")
        return redirect(url_for('users.home'))

    return render_template('user/create.html', context=g.user_context, form=form)

@users.route('/search', methods=['GET', 'POST'])
@is_logged_in
def search():
    page = request.args.get('page', 1, type=int)
    query = request.args.get('query', 'admin')
    user_list = User.query.filter(User.username.like("%" + query + "%")).paginate(page=page, per_page=PER_PAGE)
    #user_list = User.query.msearch(query).paginate(page=page, per_page=1)
    return render_template("users.html", users=user_list, context=g.user_context)

"""
@app.route('/users/<int:user_id>', methods = ['PUT', 'DELETE'])
def users_update_and_delete(user_id):
    if request.method == 'DELETE':
        user = models.User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        return redirect("/users")

    elif request.method == 'PUT':
        new_username = request.form.username
        new_email = request.form.email
        user = models.User.query.filter_by(id=user_id).first()
        user.username = new_username
        user.email = new_email
        db.session.commit()
        return redirect("/users")
"""