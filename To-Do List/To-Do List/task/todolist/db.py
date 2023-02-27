# Write your code here
# todo=['Do yoga', 'Make breakfast', 'Learn basics of SQL', 'Learn what is ORM']
# print("Today:")
# for index in range(len(list)):
#         print(f'{index + 1}) {list[index]}')
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    # id = Column(Integer, primary_key=True)
    # task = Column(String, default='default_value')
    # deadline = Column(Date, default=datetime.today())
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date)
    def __repr__(self):
        return self.task

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_row = Task(task='This is string field!',
               deadline=datetime.strptime('01-24-2020', '%m-%d-%Y').date())
session.add(new_row)
session.commit()

rows = session.query(Task).all()

first_row = rows[0]  # In case rows list is not empty

print(first_row.task)  # Will print value of the string_field
print(first_row.id)  # Will print the id of the row.
print(first_row)  # Will print the string that was returned by __repr__ method

