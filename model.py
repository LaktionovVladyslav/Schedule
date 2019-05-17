from app import db
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table


schedule_date = Table('schedule_date', db.Model.metadata,
                      Column('schedule', Integer, ForeignKey('employment.id')),
                      Column('employment_id', Integer, ForeignKey('schedule.id'))
                      )


class Discipline(db.Model):
    __tablename__ = 'discipline'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Classroom(db.Model):
    __tablename__ = 'classroom'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Time(db.Model):
    __tablename__ = 'couple'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    time_of_couple = DateTime()


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    first_middle_last_name = Column(String(250), nullable=False)
    additional_info = Column(String(250), nullable=False)


class Group(db.Model):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    faculty = Column(String(250), nullable=False)


class Employment(db.Model):
    __tablename__ = 'employment'
    id = Column(Integer, primary_key=True)
    time = Column(Integer, ForeignKey(Time.id), primary_key=True)
    discipline = Column(Integer, ForeignKey(Discipline.id), primary_key=True)
    category = Column(Integer, ForeignKey(Category.id), primary_key=True)
    classroom = Column(Integer, ForeignKey(Classroom.id), primary_key=True)
    teacher = Column(Integer, ForeignKey(Teacher.id), primary_key=True)


class Schedule(db.Model):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    date = DateTime()
    group = Column(Integer, ForeignKey(Group.id), primary_key=True)

