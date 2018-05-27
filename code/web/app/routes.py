from flask import render_template, jsonify, request, make_response, redirect, flash, url_for, session, logging, abort, g
import datetime
from run import app, db
from app.forms import LoginForm
from app.decorators import is_logged_in, is_teacher, is_personal
from app import models
from app import controller
from app.blueprints.users.controller import (
    create_new_user
)
from app.blueprints.users.models import (
    User
)

@app.route('/show_all_consultancy' , methods = ['GET'])
@is_logged_in
def show_all_consultancy():
    all_relation = models.Consultancy.query.all()

    return render_template('pages/show_all_consultancy.html', context=g.user_context, relation_list=all_relation)

@app.route('/assign_consultant', methods = ['GET', 'POST'])
@is_logged_in
def assign_consultant():

    if request.method == "POST":
        teacher = request.form['teacher']
        student = request.form['student']

        t_id = User.query.filter_by(username=teacher).first()
        t_id = t_id.id

        s_id = User.query.filter_by(username=student).first()
        s_id = s_id.id
        try:

            r = controller.create_consultancy_relation(t_id, s_id)

            flash("Danışman ataması yapıldı")

        except:
            flash("Danışman ataması yapılamadı")

        return redirect(url_for('assign_consultant'))

    if request.method == 'GET':
        teachers = User.query.filter_by(role_id=2).all()
        students = User.query.filter_by(role_id=3).all()
        return render_template('pages/assign_consultant.html', context=g.user_context, teachers=teachers, students=students)


@app.route('/opinion_db', methods = ['GET'])
def create_opinion_db():
    created_opinion = controller.create_opinion(1,"content","date")
    created_opinion = controller.create_opinion(2,"content","date")
    created_opinion = controller.create_opinion(3,"content","date")
    created_opinion = controller.create_opinion(4,"content","date")
    return "opinions created"

@app.route('/make_opinion/<int:user_id>', methods = ['GET', 'POST'])
@is_logged_in
def make_opinion(user_id):
    if request.method == "POST":
        content = request.form['content']
        student = user_id
        teacher = g.user_context['user'].id
        date = "test zamani"

        c_id = models.Consultancy.query.filter_by(teacher_id=teacher,student_id=student).first()
        c_id = c_id.id

        controller.create_opinion(c_id,content,date)

        return redirect(url_for('show_opinions',user_id=user_id))

    if request.method == "GET":
        return render_template('pages/make_opinion.html', context=g.user_context, student_id=user_id)


@app.route('/opinions/<int:user_id>', methods = ['GET'])
@is_logged_in
def show_opinions(user_id):
    if request.method == 'GET':
        c_id = models.Consultancy.query.filter_by(student_id=user_id,teacher_id=g.user_context['user'].id).first()
        c_id = c_id.id
        app.logger.info(c_id)

        opinion_list = models.Opinion.query.filter_by(consultancy_id=c_id).all()
        app.logger.info(opinion_list)

        return render_template('pages/show_opinions.html', context=g.user_context, opinion_list=opinion_list)

@app.route('/consultancy_db', methods = ['GET'])
def create_consultancy_db():
    created_realition = controller.create_consultancy_relation(1, 2)
    created_realition = controller.create_consultancy_relation(1, 3)
    created_realition = controller.create_consultancy_relation(2, 3)
    created_realition = controller.create_consultancy_relation(1, 4)
    return "consultancy created!!"

@app.route('/consultancy/<int:user_id>', methods = ['GET'])
@is_logged_in
def show_consultancy(user_id):
    response = models.Consultancy.query.filter_by(teacher_id=user_id).all()

    app.logger.info(response)
    result = []

    for tmp in response:
        student = User.query.filter_by(id=tmp.student_id).first()

        result.append(student)

    #return jsonify(result)
    return render_template('pages/my_consultancy_list.html', context=g.user_context, users=result)

# Index Page
@app.route('/', methods = ['GET'])
@is_logged_in
def home():
    return render_template('pages/home.html', context=g.user_context)

# Mysql Version
@app.route('/mysql', methods = ['GET'])
def mysql_test():
    data = models.get_mysql_info()
    print(data)

    return jsonify({"status": "okey", "content": data}), 200

@app.route("/initial_db", methods=["GET"])
def initial_db():
    ### Drop All tables
    db.reflect()
    db.drop_all()
    ### Clear sessions
    session.clear()
    session.pop('username', None)
    ### Create Tables
    db.create_all()
    ### Create Roles
    administrative_staff = models.Role(name='IdariPersonel')
    teacher = models.Role(name='Ogretmen')
    student = models.Role(name='Ogrenci')
    db.session.add(administrative_staff)
    db.session.add(teacher)
    db.session.add(student)
    db.session.commit()

    ### Create Role Funcs
    func_create_user = models.RoleFuncs(name='CreateUser', role_id=administrative_staff.id)
    func_see_all_user = models.RoleFuncs(name='SeeAllUser', role_id=administrative_staff.id)
    db.session.add(func_create_user)
    db.session.add(func_see_all_user)
    db.session.commit()

    func_danisman_ata = models.RoleFuncs(name='AssignCons', role_id=administrative_staff.id)
    db.session.add(func_danisman_ata)
    db.session.commit()

    ###################### Create Administrative Staff
    new_administrative_staff = create_new_user(
        uname="admin",
        password="admin123",
        fname= "Mustafa",
        mname= "Kemal",
        sname= "Ataturk",
        email= "admin@gmail.com",
        role_id=administrative_staff.id
    )
    return '<a href="/">Ok!</a>'

# User Login
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        try:
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                session['logged_in'] = True
                session['username'] = user.username
                flash('You are now logged in', 'success')
                return redirect(url_for('home'))
            else:
                flash("Invalid Login")
                return render_template('pages/login.html', form=form)

        except Exception as e:
            app.logger.info("Failed to log in {}".format(e))
            abort(500)

    return render_template("pages/login.html", form=form)

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    session.pop('username', None)
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/error/404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('pages/error/500.html'), 500