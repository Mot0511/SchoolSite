from flask import *

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forStudents')
def forStudents():
    return render_template('forStudents.html')

@app.route('/forParents')
def forParents():
    return render_template('forParents.html')

@app.route('/forTeachers')
def forTeachers():
    return render_template('forTeachers.html')

app.run()