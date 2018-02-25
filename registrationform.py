from flask import Flask, render_template, redirect, request, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "Key"

@app.route('/')
def main_page():

    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process_validation():

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['password_confirm'] = request.form['password_confirm']

    validation_failed = False

    if len(session['first_name']) < 1:
        flash("First name is required!", 'error')
        validation_failed = True
    else:
        if not session['first_name'].isalpha():
            flash("First name can only include alphabetical characters!", 'error')
            validation_failed = True

    if len(session['last_name']) < 1:
        flash("Last name is required!", 'error')
        validation_failed = True
    else:
        if not session['last_name'].isalpha():
            flash("Last name can only include alphabetical characters!", 'error')
            validation_failed = True

    if len(session['email']) < 1:
        flash("Email is required!", 'error')
        validation_failed = True
    elif not EMAIL_REGEX.match(session['email']):
        flash("Please enter a valid email", 'error')
        validation_failed = True


    if len(session['password']) < 1:
        flash("Password is required!", 'error')
        validation_failed = True
    elif len(session['password']) < 8:
        flash("Password must be at least 8 characters!", 'error')
        validation_failed = True


    if len(session['password_confirm']) < 1 or session['password_confirm'] != session['password']:
        flash("Password confirmation must match!", 'error')
        validation_failed = True





    if validation_failed == False:
        flash("Success!", 'success')

    return redirect('/')



app.run(debug=True)
