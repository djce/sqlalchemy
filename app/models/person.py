# from sqlalchemy.sql.schema import ForeignKey
# from .base import db
# from sqlalchemy import Column, Integer, String, DateTime, Text
# from sqlalchemy import func
# from sqlalchemy.orm import relationship

# class Person(db.Model):
#     __tablename__ = 'tbl_person_info'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(20))
#     first_name = Column(String(20))
#     last_name = Column(String(20))
#     comment = Column(Text)
#     tag_id = Column(Integer, ForeignKey('tbl_person_tag.id'))
#     create_time = Column(DateTime(timezone=True), server_default=func.now())
#     update_time = Column(DateTime(timezone=True), server_default=func.now(),
#                         server_onupdate=func.now())
#     tag = relationship('Tag', backref='person_where_tag')

# class Tag(db.Model):
#     __tablename__ = 'tbl_person_tag'
#     id = Column(Integer, primary_key=True)
#     title = Column(String(10))
#     create_time = Column(DateTime(timezone=True), server_default=func.now())
#     update_time = Column(DateTime(timezone=True), server_default=func.now(),
#                         server_onupdate=func.now())

# class Poem(db.Model):
#     __tablename__ = 'tbl_classic_poem'
#     title = db.Column(db.String(20))
#     content = db.Column(db.Text)
#     author_id = db.Column(db.Integer, db.Foreignkey('author.id'))
#     author = db.relationship('Author', backref='poem_where_author')
#     create_time = db.Column(db.DateTime, default=datetime.now)
#     update_time = db.Column(db.DateTime, 
#                             default=datetime.now,
#                             onupdate=datetime.now)

# class Author(db.Model):
#     __tablename__ = 'tbl_poem_author'
#     name = db.Column(db.String(20), unique=True)
#     dynasty = db.Column(db.String(10))