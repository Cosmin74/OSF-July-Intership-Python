from flask import Flask, render_template
from database import db
from tasks import task_bp
from users import users_bp

app = Flask(__name__)
app.register_blueprint(task_bp)
app.register_blueprint(users_bp)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

# Run the Flask application
if __name__ == '__main__':
    with db:
        app.run(debug=True)