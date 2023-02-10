from flask import Blueprint, render_template, flash
from melomane.views.authorisation.forms import RegisterForm, LoginForm
from melomane.models.users import User
from melomane.extensions import db

auth_blueprint = Blueprint('auth', __name__, template_folder="templates")

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("authorisation/login.html", form=form)


@auth_blueprint.route("/registration", methods =["GET", "POST"])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        user_username = form.username.data
        user_email = form.email.data
        user_password = form.password.data
        person = User(username=user_username, email=user_email, password=user_password)
        db.session.add(person)
        db.session.commit()


        flash("succesfully registered")
    else:
        print(form.errors)

        return render_template("authorisation/registration.html", register_form=form)


    return render_template("authorisation/registration.html", register_form=form)
