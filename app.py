from flask import Flask
application = Flask(__name__)

@application.route("/")
def home():
    return "✅ Version 1 deployed via CodeDeploy!"


if __name__ == '__main__':
    application.run(host=0.0.0.0,port=80)
