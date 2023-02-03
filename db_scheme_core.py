"""
Models were rewrited to SQLAlchemy Core from ORM, so it could work with async
"""


from sqlalchemy import Table, Integer, String, Boolean, \
    Column, DateTime, Date, ForeignKey, Float, BigInteger, MetaData
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

metadata = MetaData()


Base = declarative_base()

typesOfLesson = Table('types_of_lesson', metadata,
    # '''
    # Table for types of lessons. For ex., group lesson or personal lesson

    # id
    # name - name of lesson
    # client_price - amount, that client must pay for that type of lesson
    # staff_payment - amount, that staff will have for this type of lesson
    # is_actual
    # '''
    
    Column("id", Integer(), primary_key=True),
    Column("name", String(100), nullable=False),
    Column("client_price", Float),
    Column("staff_payment", Float),
    Column("is_actual", Boolean, nullable=False)
)


dogs = Table('dogs', metadata,
    # '''
    # Dogs info

    # staff_id - instructor's id
    # place_id - default place for lesson. It helps to autofill field lessons.place_id
    # '''
    Column("id", Integer(), primary_key=True),
    Column("name", String(20), nullable=False),
    Column("breed",String(20), nullable=False),
    Column("is_learning", Boolean(), nullable=False)    ,
    Column("staff_id", Integer(), ForeignKey('staff.id')),
    Column("place_id", Integer(), ForeignKey('places.id'))
)


userDog = Table('user_dog', metadata,
    # '''
    # Many to many table. One dog may have many owners and vice versa
    # '''
    Column("id", Integer, primary_key=True),
    Column("staff_id", Integer, ForeignKey('staff.id')),
    Column("dog_id", Integer, ForeignKey('dogs.id'))
)
   

lessons = Table('lessons', metadata,
    # '''
    # Table for lessons. Connects staff, dog, place, type of lesson
    # '''
    Column("id", Integer, primary_key=True),
    Column("date", DateTime(), nullable=False),   
    Column("dog_id", Integer, ForeignKey('dogs.id'), nullable=False),
    Column("place_id", Integer, ForeignKey('places.id'), nullable=False),
    Column("type_of_lesson_id", Integer, ForeignKey('types_of_lesson.id'), nullable=False),
    Column("staff_id", Integer, ForeignKey('staff.id'), nullable=False)
)


staff = Table('staff', metadata,
    # '''
    # Information about all users (customers and staff)
    
    # id
    # name - person's name
    # role - (-1)-3 (customer without adv/ customer with adv/ instuctor/ administrator/ sen. administrator)
    # ...
    # '''
    Column("id", Integer, primary_key=True),
    Column("name", String(20), nullable=False),
    Column("role", Integer, nullable=False),
    Column("phone", String(15), nullable=False),
    Column("date_of_birth", Date()),
    Column("tg_id", Integer),
    Column("e_mail", String(100))
)

places = Table('places', metadata,
    # '''
    # Information about places, where lessons run
    # '''
    Column("id", Integer, primary_key=True),
    Column("address", String(255), nullable=False),
    Column("name", String(30), nullable=False),
    Column("is_actual", Boolean, nullable=False)    
)


advertisements = Table('advertisements', metadata,
    # '''
    # Table for advertisements. Advertisements will be sended by tg or e-mail

    # id
    # name - name of adv (information for staff)
    # created_by - staff, that created this adv
    # date_to_post
    # topic - for e-mail
    # text
    # send_to - 1/2/3 (tg/e-mail/both)
    # '''
    Column("id", Integer, primary_key=True),
    Column("name", String(20), nullable=False),
    Column("created_by", Integer, ForeignKey('staff.id'), nullable=False),
    Column("date_to_post", DateTime(), default=datetime.now, nullable=False),
    Column("topic", String(100), nullable=False),
    Column("text", String(255), nullable=False),
    Column("send_to", String(2), nullable=False) 
)


users = Table('users', metadata,
    # '''
    # StaffAuth more correct name for this table. Kepps passwords for staff
    # '''
    Column("id", Integer, primary_key=True),
    Column("password", String(100), nullable=False),
    Column("staff_id", Integer, ForeignKey('staff.id'), nullable=False)
)


courses = Table('courses', metadata,
    # '''
    # Information about courses, that customers may buy

    # id
    # name - name of course
    # lesson_amount - amount of lessons, that customer may attend
    # price
    # is_actual
    # '''
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("lesson_amount", Integer, nullable=False),
    Column("price", Float, nullable=False),
    Column("is_actual", Boolean, nullable=False) 
)


dogCourse = Table('dog_course', metadata,
    # '''
    # Many to many table. For one dog may be bought many courses and vice versa
    # '''
    Column("id", Integer, primary_key=True),
    Column("dog_id", Integer, ForeignKey('dogs.id'), nullable=False),
    Column("course_id", Integer, ForeignKey('courses.id'), nullable=False),
    Column("date", Date(), nullable=False)
)


sessions = Table('sessions', metadata,
    # '''
    # Table to keep sessions

    # id
    # user_id
    # token
    # time - unix time
    # ip
    # mac
    # '''
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey('users.id')),
    Column("token", String(40), nullable=True),
    Column("time", BigInteger, nullable=False),
    Column("ip", String(40), nullable=False),
    Column("mac", String(20), nullable=False)
)