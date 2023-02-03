from sqlalchemy import Table, Integer, String, Boolean, \
    Column, DateTime, Date, ForeignKey, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class TypesOfLesson(Base):
    '''
    Table for types of lessons. For ex., group lesson or personal lesson

    id
    name - name of lesson
    client_price - amount, that client must pay for that type of lesson
    staff_payment - amount, that staff will have for this type of lesson
    is_actual
    '''
    __tablename__ = 'types_of_lesson'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    client_price = Column(Float)
    staff_payment = Column(Float)
    is_actual = Column(Boolean, nullable=False)


class Dogs(Base):
    '''
    Dogs info

    staff_id - instructor's id
    place_id - default place for lesson. It helps to autofill field lessons.place_id
    '''
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    breed = Column(String(20), nullable=False)
    is_learning = Column(Boolean, nullable=False)    
    staff_id = Column(Integer, ForeignKey('staff.id'))
    place_id = Column(Integer, ForeignKey('places.id'))


class UserDog(Base):
    '''
    Many to many table. One dog may have many owners and vice versa
    '''
    __tablename__ = 'user_dog'
    id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    dog_id = Column(Integer, ForeignKey('dogs.id'))
    

class Lessons(Base):
    '''
    Table for lessons. Connects staff, dog, place, type of lesson
    '''
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(), nullable=False)   
    dog_id = Column(Integer, ForeignKey('dogs.id'), nullable=False)
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)
    type_of_lesson_id = Column(Integer, ForeignKey('types_of_lesson.id'), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'), nullable=False)


class Staff(Base):
    '''
    Information about all users (customers and staff)
    
    id
    name - person's name
    role - (-1)-3 (customer without adv/ customer with adv/ instuctor/ administrator/ sen. administrator)
    ...
    '''
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    role = Column(Integer, nullable=False)
    phone = Column(String(15), nullable=False)
    date_of_birth = Column(Date())
    tg_id = Column(Integer)
    e_mail = Column(String(100))


class Places(Base):
    '''
    Information about places, where lessons run
    '''
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True)
    address = Column(String(255), nullable=False)
    name = Column(String(30), nullable=False)
    is_actual = Column(Boolean, nullable=False)    


class Advertisements(Base):
    '''
    Table for advertisements. Advertisements will be sended by tg or e-mail

    id
    name - name of adv (information for staff)
    created_by - staff, that created this adv
    date_to_post
    topic - for e-mail
    text
    send_to - 1/2/3 (tg/e-mail/both)
    '''
    __tablename__ = 'advertisements'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    created_by = Column(Integer, ForeignKey('staff.id'), nullable=False)
    date_to_post = Column(DateTime(), default=datetime.now, nullable=False)
    topic = Column(String(100), nullable=False)
    text = Column(String(255), nullable=False)
    send_to = Column(String(2), nullable=False) 
    

class Users(Base):
    '''
    StaffAuth more correct name for this table. Kepps passwords for staff
    '''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    password = Column(String(100), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'), nullable=False)
    

class Courses(Base):
    '''
    Information about courses, that customers may buy

    id
    name - name of course
    lesson_amount - amount of lessons, that customer may attend
    price
    is_actual
    '''
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    lesson_amount = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    is_actual = Column(Boolean, nullable=False) 


class DogCourse(Base):
    '''
    Many to many table. For one dog may be bought many courses and vice versa
    '''
    __tablename__ = 'dog_course'
    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer, ForeignKey('dogs.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    date = Column(Date(), nullable=False)


class Sessions(Base):
    '''
    Table to keep sessions

    id
    user_id
    token
    time - unix time
    ip
    mac
    '''
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    token = Column(String(40), nullable=True)
    time = Column(BigInteger, nullable=False)
    ip = Column(String(40), nullable=False)
    mac = Column(String(20), nullable=False)   