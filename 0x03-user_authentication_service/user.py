import sqlalchemy 

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	email = Column(String(250))
	hashed_password = Column(String(250))
	session_id = Column(String(250))
	reset_token = Column(String(250))
	def __repr__(self):
		return "<User(name='%s', fullname='%s', nickname='%s')>" % (
						self.name, self.fullname, self.nickname)
