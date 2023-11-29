from flask import Flask,render_template, request
from werkzeug.utils import secure_filename
from dbfuncs import save_work_to_database,get_works_from_database



app = Flask(__name__)

@app.route('/')
def index():
    works = get_works_from_database()
    return render_template("index.html",works=works)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'abc123':
            name = request.form['name']
            text = request.form['text']
            photo = request.files['photo']
            photo_name = secure_filename(photo.filename)
            photo.save('/home/JonPlayGo/portfoliosite/static/workslogo/' + photo_name)
            selected_checkboxes = request.form.getlist('checkbox')
            data = {}
            for checkbox in selected_checkboxes:
                input_text = request.form.get(f'text_{checkbox}')
                data[checkbox] = input_text
            save_work_to_database(name,text,photo_name,data)
            return data
        else:
            return 'Неправильный пароль!'
    else:
        return render_template('admin.html')
