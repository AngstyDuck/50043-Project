from app import create_app

"""
Types of modes to run app - local, remoteDev
"""

app = create_app()

if __name__ == "__main__":
    print("wsgi.py - app is created")
    app.run(host='0.0.0.0')

