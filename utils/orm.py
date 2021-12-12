from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from urllib import parse
from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask.views import View
from flask import jsonify
from flask import request

USER = 'root'
PASSWORD = parse.quote_plus('django@2021')
HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'orm'

DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8'

engine = create_engine(DATABASE_URI, max_overflow=5)

Base = declarative_base()

class User(Base):
	__tablename__ = 'tbl_user_info'
	id = Column(Integer, primary_key=True)
	username = Column(String(10), unique=True)
	type_id = Column(Integer,ForeignKey('tbl_user_type.id'))
	user_type = relationship('UserType', backref='user_where_type')

class UserType(Base):
	__tablename__ = 'tbl_user_type'
	id = Column(Integer, primary_key=True)
	title = Column(String(10), unique=True)



def init_db():
	engine = create_engine(DATABASE_URI, max_overflow=5)
	Base.metadata.create_all(engine)

def drop_table():
	engine = create_engine(DATABASE_URI, max_overflow=5)
	Base.metadata.drop_all(engine)


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

Session = sessionmaker(engine)
session = Session()

@app.route('/user/<int:pk>')
@app.route('/user')
def get_user(pk=None):

	if pk is not None:
		user = session.query(User).filter(User.id==pk).first()
		print(user.user_type.title)
	
	users = session.query(User).all()

	userList = [ {
		'id': user.id,
		'username': user.username
	} for user in users ]

	return jsonify(userList)


@app.route('/user',methods=['POST'])
def add_user():
	
	user = User(**request.json)

	session.add(user)
	session.commit()

	return jsonify({'code': 200, 'msg': 'sucess'})



@app.route('/userType/<int:pk>')
@app.route('/userType', methods=['GET','POST'])
def add_user_type(pk=None):

	if request.method == 'GET':
		if pk is not None:
			ut = session.query(UserType).filter(UserType.id==pk).first()
			users = ut.user_where_type
			user_list = [{
				'id': user.id,
				'username': user.username
			} for user in users]

			return jsonify({'id': pk, 'title': ut.title, 'userList': user_list})

		uts = session.query(UserType).order_by('id').all()

		type_list = [{
			'id': ut.id,
			'title': ut.title 
		} for ut in uts ]

		return jsonify(type_list)

	elif request.method == 'POST':

		ut = UserType(**request.json)
		session.add(ut)
		session.commit()

		return jsonify({'code': 200, 'msg': 'sucess'})
	else:

		return jsonify({'code': 405, 'msg': 'Method Not Allowed'})







if __name__ == '__main__':
	# drop_table()
	# init_db()
	app.run()


# user = User(**{'username': 'alice', 'password': '123456'})

# session.add(user)
# session.commit()


# session.query(User).filter(User.username=='alice').update({'password': 'abc'})
# session.query(User).filter(User.username=='alice').update({User.password: User.username})

# session.commit()
# rs = session.query(User).filter(User.username=='sarah').all()



