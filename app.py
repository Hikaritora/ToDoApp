from flask import Flask, render_template, request, redirect, session
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
import logging

# configure application
app = Flask(__name__)

# set the secret key for the app
app.secret_key = 'qwertyuiop'

# configure the Flask-Session extension
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")

#######################tasks = db.execute("SELECT * FROM tasks")

# configure the Flask-Session extension
Session(app)


# define a route for the home page
@app.route('/home')
def index():
    # check if the user is logged in
    if 'user_id' not in session:
        # if not, redirect the user to the login page
        return redirect('/')

    # retrieve all tasks from the database for the logged in user
    tasks = db.execute("SELECT * FROM tasks WHERE user_id = :user_id AND completed = 0", user_id=session['user_id'])

    # retrieve all completed tasks from the database for the logged in user
    completed_tasks = db.execute("SELECT * FROM tasks WHERE user_id = :user_id AND completed = 1", user_id=session['user_id'])

    # render the index.html template and pass the tasks and completed_tasks lists to the template
    return render_template('index.html', tasks=tasks, completed_tasks=completed_tasks)


# define a route for adding a new task
@app.route('/add-task', methods=['POST'])
def add_task():
    # get the task title and due date from the form submission
    task_title = request.form['task-title']
    due_date = request.form['due-date']

    # check if the task title is not empty
    if task_title:
        # get the user's id
        user_id = session['user_id']

        # insert a new task into the database
        db.execute("INSERT INTO tasks (title, due_date, user_id) VALUES (:title, :due_date, :user_id)",
                   title=task_title, due_date=due_date, user_id=user_id)

    # redirect the user back to the index page
    return redirect('/home')


# define a route for completing a task
@app.route('/complete-task/<task_id>', methods=['POST'])
def complete_task(task_id):
    # check if the user is logged in
    if 'user_id' not in session:
        # if not, redirect the user to the login page
        return redirect('/')

    # get the user's id
    user_id = session['user_id']

    # update the task's completed status in the database
    db.execute("UPDATE tasks SET completed = 1 WHERE id = :id AND user_id = :user_id", id=task_id, user_id=user_id)

    # redirect the user back to the index page
    return redirect('/home')


# define a route for deleting a task
@app.route('/delete-task/<task_id>', methods=['POST'])
def delete_task(task_id):
    # check if the user is logged in
    if 'user_id' not in session:
        # if not, redirect the user to the login page
        return redirect('/')

    # get the user's id
    user_id = session['user_id']

    # delete the task from the "tasks" table
    db.execute("DELETE FROM tasks WHERE id = :id AND user_id = :user_id", id=task_id, user_id=user_id)

    # delete the task from the "completed tasks" table
    db.execute("DELETE FROM tasks WHERE id = :id AND user_id = :user_id AND completed = 1", id=task_id, user_id=user_id)

    # redirect the user back to the index page
    return redirect('/home')


# define a route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    # if the user is submitting the login form
    if request.method == 'POST':
        # retrieve the username and password from the form submission
        username = request.form['username']
        password = request.form['password']

        # query the database for the user's data
        user = db.execute("SELECT * FROM users WHERE username = :username", username=username)

        # if the user exists and the password is correct
        if user and check_password_hash(user[0]['password'], password):
            # set the user_id session variable
            session['user_id'] = user[0]['id']
            # redirect the user to the home page
            return redirect('/home')
        # if the login credentials are invalid
        else:
            # render the login.html template with an error message
            return render_template('login.html', error='Invalid login credentials')
    # if the user is accessing the login page
    else:
        # render the login.html template
        return render_template('login.html')


# define a route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    # if the user is submitting the registration form
    if request.method == 'POST':
        # retrieve the username and password from the form submission
        username = request.form['username']
        password = request.form['password']

        # query the database for the user's data
        user = db.execute("SELECT * FROM users WHERE username = :username", username=username)

        # if the user already exists
        if user:
            # render the register.html template with an error message
            return render_template('register.html', error='Username already exists')

        # if the user does not exist
        else:
            # hash the password
            hashed_password = generate_password_hash(password)

            # insert a new user into the database
            db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
                       username=username, password=hashed_password)

            # redirect the user to the login page
            return redirect('/')

    # if the user is accessing the registration page
    else:
        # render the register.html template
        return render_template('register.html')



# check if the user is logged in
def check_login():
    # if the user is not logged in
    if 'user_id' not in session:
        # redirect the user to the login page
        return redirect('/login')


# define a route for the logout page
@app.route('/logout', methods=['POST'])
def logout():
    # clear the session
    session.clear()
    # redirect the user to the login page
    return redirect('/')

