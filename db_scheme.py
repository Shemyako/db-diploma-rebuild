from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class TypesOfLesson(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    content = Column(String(50), nullable=False)
    published = Column(String(200), nullable=False, unique=True)    
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class Advertisements(Base):
    pass


class Sessions(Base):
    pass


class Courses(Base):
    pass


class Places(Base):
    pass


class Staff(Base):
    pass


class StaffAuth(Base):
    pass


class Dogs(Base):
    pass


class Lessons(Base):
    pass


class UserDog(Base):
    pass


class DogCourse(Base):
    pass


