# To-Do App
#### Description:
This To-Do app is a web application that allows users to manage their tasks and mark them as completed. The app has a login system, and each user has their own personal task list. Users can add new tasks with due dates, mark tasks as completed, and delete tasks from their list.

The app is built using the Flask framework in Python and uses a SQLite database to store the tasks. The front-end is built using HTML, CSS, and Bootstrap.

https://imgur.com/a/h2HJhiR

Here is a list that describes all of the files in the project:

#### app.py
This file contains the main logic for the to-do app. The file sets up the Flask application and defines routes for the different pages and actions in the app.

The index route displays the home page for the app, which shows a list of tasks that need to be completed and a list of completed tasks for the logged in user. It also renders the index.html template, which contains the HTML for the home page.

The add_task route handles the form submission for adding a new task. It gets the task title and due date from the form submission and inserts a new task into the database for the logged in user.

The complete_task route updates the completed status of a task in the database when the user clicks the "Complete" button for a task.

The delete_task route deletes a task from the "tasks" table in the database when the user clicks the "Delete" button for a task.

#### index.html
The index.html file is an HTML template file that is rendered by the app.py script to generate the user interface for the to-do app. It contains the HTML markup for the layout and design of the app, as well as Jinja template tags that are used to render the tasks from the database.

The file also contains a form for adding a new task, which submits a POST request to the /add-task route in the app.py script. It also contains buttons for completing and deleting tasks, which also submit POST requests to the app.py script.

#### login.html
This template is used for the login page of the application. It includes a simple form with two input fields for the user's username and password, and a submit button. When the form is submitted, the input values are sent to the /login route defined in the app.py file. If the login is successful, the user is redirected to the home page. If the login is unsuccessful, an error message is displayed to the user.

#### register.html
This template is used for the registration page of the application. It includes a form with three input fields for the user's username and password. It also includes a submit button. When the form is submitted, the input values are sent to the /register route defined in the app.py file. If the registration is successful, the user is redirected to the login page. If the registration is unsuccessful, an error message is displayed to the user.

#### database.db
The database.db file is a SQLite database file that is used to store the tasks and user data for the to-do app. It contains two tables: users and tasks.

The users table stores the user's id, username, and hashed password. It is used for authenticating and identifying the user when they log in to the app.

The tasks table stores the task's id, title, due date, completion status, and the user's id. It is used to store and retrieve the tasks that the user adds to their to-do list.

By using a database, the app is able to persist the tasks and user data even after the app has been closed, allowing the user to access their tasks the next time they log in to the app.

#### requirements.txt
requirements.txt is a text file that lists all of the Python packages that are required for the to-do app to run


## Design choices
There are a few design choices that can be noted in the project:

* The use of a database to store the tasks: This allows for the tasks to be persistent and accessible to the user even after they log out or close the application. It also allows for multiple users to use the application and have their own separate task lists.

* The use of a login system: This allows for multiple users to use the application and have their own separate task lists. It also allows for secure access to the application, as only registered users can log in and access their tasks.

* The use of Flask and the Jinja template engine: Flask is a lightweight web framework that allows for the creation of dynamic web applications. Jinja is a template engine that allows for the insertion of dynamic content into HTML files, making it easier to create and maintain a consistent layout across the application.

* The use of Bootstrap for styling: Bootstrap is a front-end framework that provides a set of predefined CSS styles and layout components, making it easier to create a visually appealing and responsive application.

* The use of form validation: Form validation is used to ensure that the user enters the required information when adding or updating a task. This helps to prevent errors and ensure that the application functions as intended.

Overall, these design choices were made to create a functional and user-friendly to-do list application.
