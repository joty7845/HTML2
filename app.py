from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class StudentDataForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    grades = SelectField('Grades', choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
    satisfaction = SelectField('Satisfaction', choices=[('1', '1'), ('2', '2'), ('3', '3')])
    suggestions = TextAreaField('Suggestions')

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = StudentDataForm()
    if form.validate_on_submit():
        with open('data.txt', 'a') as f:
            f.write(f"{form.name.data}, {form.student_number.data}, {form.email.data}, {form.grades.data}, {form.satisfaction.data}, {form.suggestions.data}\n")
        return 'Data submitted'
    return render_template('data_collection.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

