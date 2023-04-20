from flask import Blueprint, render_template, request, flash
import re
from datetime import *

views = Blueprint('views', __name__)
EMAIL_PATTERN = re.compile(r".+\@.+\..+")
DATE_FORMAT = '%Y-%m-%d'
MIN_YEAR = 18

@views.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        firstName = data.get('first_name')
        lastName = data.get('last_name')
        birthdate = datetime.strptime(data.get('birthdate'), DATE_FORMAT)
        today = date.today()

        age = (today.year - birthdate.year) - ((today.month, today.day) < (birthdate.month, birthdate.day))

        # Validates inputs
        # Email matches the pattern
        # First name and last name does not match
        # birthdate is older than 18 years
        if re.match(EMAIL_PATTERN, email) == None:
            flash('Email is not valid.', category='error')
        elif firstName == lastName:
            flash('First name cannot be the same as last name.', category='error')
        elif age < MIN_YEAR:
            flash('User must be older than 18 to sign up', category='error')
        else:
            flash("User has successfully signed up!", category='success')
    
    return render_template("home.html")
    