from flask import session, redirect, flash, url_for, request, g
from functools import wraps
from datetime import datetime

from app.models import Role
from app.blueprints.users.models import User

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in session:
            username = session.get('username')
            user = User.query.filter_by(username=username).first()
            context = {
                'ip': request.remote_addr,
                'user': user,
                'login_date': datetime.now()
            }
            g.user_context = context
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))

    return wrap

# Ogretmen mi?
def is_teacher(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if g.user_context['user'].role_id == 2:
            return f(*args, **kwargs)
        else:
            flash('You are not teacher, Please login', 'danger')
            return redirect(url_for('login'))

    return wrap

# Idari personal mi?
def is_personal(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if g.user_context['user'].role_id == 1:
            return f(*args, **kwargs)
        else:
            flash('You are not personal, Please login', 'danger')
            return redirect(url_for('login'))

    return wrap
