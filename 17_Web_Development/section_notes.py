"""

Virtual Environment
- Use a virtual environment to manage the dependencies for your project, both 
  in development and in production.
- Virtual environments are independent groups of Python libraries, one for each 
  project.
- Packages installed for one project will not affect other projects or the 
  operating system’s packages.
- Python comes bundled with the 'venv' module to create virtual environments.  

- Create an environment
    Create a project folder and a venv folder within:
      $ mkdir my_project
      $ cd my_project
      $ py -m venv venv   # the 2nd venv is the directory name we wish to store
      the virtual environment files in.
- Activate the environment
    Before you work on your project, activate the corresponding environment:
      $ source venv/Scripts/activate

- Install flask
  Within the activated environment, use the following command to install Flask:
  $ pip install flask

  in .py script:

  from flask import Flask

  app = Flask(__name__)

  __name__ this is needed so that Flask knows where to look for resources such 
  as templates and static files.
  - We then use the route() decorator to tell Flask what URL should trigger our 
  function.
  - The function returns the message we want to display in the user’s browser.
  - The default content type is HTML, so HTML in the string will be rendered by 
    the browser.

  decorator:
  @app.route("/")
  def homepage():
    return "This is homepage"
  
  o run the application, use the flask command or python -m flask. Before you 
  can do that you need to tell your terminal the application to work with by 
  exporting the FLASK_APP environment variable:

  $ export FLASK_APP=server.py
  $ flask run  OR $python -m flask run

- Debug Mode on/off
   By enabling debug mode, the server will automatically reload if code changes, 
   and will show an interactive debugger in the browser if an error occurs 
   during a request.
  
   Warning:  Do not run the development server or debugger in a production 
   environment, it represents a major security risk.
  
   $ export FLASK_ENV=development
   $ flask run

  - redirct("/html page") 
    redirct() unlike render_template, takes no variable
    
"""

