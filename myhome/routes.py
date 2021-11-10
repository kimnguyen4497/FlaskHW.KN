from myhome import flaskhw
from flask import render_template, request, flash, redirect
from myhome.forms import TopCities
from myhome import db
from myhome.models import dataBase



@flaskhw.route("/", methods = ['GET' , 'POST'])
def home():
	name = 'KIMMMY'
	title = 'Top Cities'
	form =  TopCities()
	db.create_all()
	cities = dataBase.query.all()
	if form.validate_on_submit():

		
		
		
		if db.session.query(citydb).filter_by(city_rank = form.city_rank.data).first():
			flash(f'{form.city_name.data} was added')			
			name = request.form['city_name']
			rank = len(dataBase)
			city = dataBase(name, rank)
			db.session.add(city)
			db.session.commit()
			return redirect('/')

		name = request.form['city_name']
		rank = request.form['city_rank']
		flash(f'{form.city_name.data} was added')			
		city = dataBase(name, rank)		
		db.session.add(city)
		db.session.commit()	
		return redirect('/')


	return render_template('home.html',name=name,title=title,form=form,cities=cities)
