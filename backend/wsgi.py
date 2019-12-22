from app import create_app

"""
The backend code follows Flask's app factory code style. This uses the app as a global object, and ties functions (in the form of Flask's "Blueprints") and environment variables to this object to be accessible across different parts of the code logic.
For more information: https://hackersandslackers.com/demystifying-flask-application-factory/
"""

app = create_app()

if __name__ == "__main__":
    print("wsgi.py - app is created")
    app.run(host='0.0.0.0')

