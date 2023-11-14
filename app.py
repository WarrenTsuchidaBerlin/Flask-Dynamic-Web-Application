from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")


if __name__ == '__main__':
    #optional: default port is 5000 anyway
    #debug=True so that whenever a change is made to files, the app will automatically refresh so we don't have to keep rerunning the script unless we have any syntax errors or if the script crashes.
    app.run(debug=True, port=5000)