from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class UserForm(Form):
    id_no = StringField('Id No',  validators = [InputRequired("Id Number is Required")])
    name = StringField('Name',  validators = [InputRequired("Name is Required")])
    course = StringField('Course',  validators = [InputRequired("Course is Required")])
    submit = SubmitField("Submit")

class DeleteForm(Form):
    del_id = StringField('Id Number', validators =[InputRequired("Make sure you enter an Id Number you want to delete!")])
    submit = SubmitField("Submit")

class UpdateForm(Form):
    new_id = StringField('Id No', validators = [InputRequired("Id Number is Required")])
    new_name = StringField('New Name', validators = [InputRequired("Hey You Forget the Name! :)")])
    new_course = StringField('New Course', validators = [InputRequired("Make sure to input something in the course section!")])
    submit = SubmitField("Submit")

class SearchForm(Form):
    search_id = StringField('Id No of The Student',  validators = [InputRequired("Id Number is Required")])
    submit = SubmitField("Submit")