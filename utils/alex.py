from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, func
from pathlib import Path
from datetime import datetime
from flask import Flask
from flask import jsonify
from flask import request

BASE_DIR = Path(__file__).resolve().parent
Base = declarative_base()


class User(Base):
	__tablename__ = 'tbl_user_info'
	id = Column(Integer, primary_key=True, comment='用户id')
	first_name = Column(String(10), unique=True, nullable=False)
	last_name = Column(String(10))
	name = Column(String(20), unique=True)
	# create_time = Column(DateTime, server_default=datetime.now)
	create_time = Column(DateTime, default=func.now())
	update_time = Column(DateTime, default=func.now(), onupdate=func.now())

	def get_fullname(self):
		if self.last_name is None:
			return self.first_name
		return f'{self.first_name}.{self.last_name}'


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

DB_URI = f"sqlite:///{str(BASE_DIR / 'user.db')}"
engine = create_engine(DB_URI)

Session = sessionmaker(engine)
session = Session()

@app.route('/user', methods=['POST'])
def add_user():
	user = User(**request.json)

	session.add(user)
	session.commit()

	return jsonify({'code': 200, 'msg': 'success'})

@app.route('/user', methods=['GET'])
def get_user():
	objs = session.query(User).order_by('id').all()
	users = [{
		'id': obj.id,
		'firstNmme': obj.first_name,
		'last_name': obj.last_name,
		'name': obj.name,
		'create_time': obj.create_time,
		'update_time': obj.create_time
	} for obj in objs] 

	return jsonify({'code': 200, 'msg': '', 'data': users})



if __name__ == '__main__':
	# Base.metadata.create_all(engine)
	app.run()





