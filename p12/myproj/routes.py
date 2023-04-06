from . import app, db
from .models import Something
from .forms import SomethingForm, UpdateSomething

from flask import render_template, send_from_directory, request, flash, url_for, redirect
from sqlalchemy.exc import IntegrityError

@app.route('/')
def index():
    objects = Something.query.all()
    # order_by(Something.created_at.desc())
    # paginate(page=???, per_page=???)
    return render_template('index.html', objects=objects)

@app.route('/<int:sid>/')
def get_something(sid):
    smth = Something.query.get_or_404(sid)
    return render_template('something.html', object=smth)

@app.route('/top/')
def top():
    rating = request.args.get('rating', 0, type=int)
    print(rating)
    somethings = Something.query.filter(Something.rating > rating)
    return render_template('top.html', objects=somethings)


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = SomethingForm()

    if form.validate_on_submit():
        name = form.name.data
        rating = form.rating.data
        print(type(rating))

        smth = Something(name=name, rating=rating)
        db.session.add(smth)
        db.session.commit()

        return redirect(url_for('index'))
    print(form._csrf)
    return render_template('create.html', form=form)


@app.route('/<int:sid>/edit/', methods=['GET', 'POST'])
def edit(sid):
    something = Something.query.get_or_404(sid)
    form = UpdateSomething()

    if form.validate_on_submit():
        something.rating = int(form.rating.data)
        try:
            db.session.commit()
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash('Произошла ошибка: такой объект уже есть в базе', 'error')
            return render_template('edit.html', form=form)
      
    elif request.method == 'GET':
        form.rating.data = something.rating

    return render_template('edit.html', form=form)      
