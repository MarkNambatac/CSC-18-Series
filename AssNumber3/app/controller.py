from app import app
import models
from flask import render_template, redirect, request
from forms import UserForm, DeleteForm, UpdateForm, SearchForm
import MySQLdb


@app.route('/')
def index():
    users = models.Users.all()
    return render_template('index.html', data=users)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(id_no=form.id_no.data, name=form.name.data, course=form.course.data)
        user.add()
        return redirect('/')
    else:
        return render_template('signup.html', form=form)

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    form = DeleteForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(id_no = form.del_id.data)
        user.delete()
        return redirect('/')
    else:
        return render_template('delete.html', form = form)

@app.route('/update', methods = ['POST', 'GET'])
def update():
    form = UpdateForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(id_no = form.new_id.data, name = form.new_name.data, course = form.new_course.data)
        user.update()
        return redirect('/')
    else:
        return render_template('update.html', form = form)

@app.route('/search', methods= ['POST', 'GET'])
def search():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(id_no = form.search_id.data)
        data = user.search()
        return render_template('profile.html', data = data)
    else:
        return render_template('search.html', form = form)
