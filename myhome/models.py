from myhome import db

class dataBase(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	city_name = db.Column(db.String(128), unique = True, index = True)
	city_rank = db.Column(db.Integer, unique = True)

	def __repr__(self):
                return f'<citydb {self.city_name} : {self.city_rank}>'

	

   

		

	