from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
# import calendar
engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()

weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    # deadline = Column(Date)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


class TaskList:
    def __init__(self):
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def run(self):
        while True:
            c = input("\n1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit\n")
            if c == "1":
                self.print_list()
            if c == "2":
                self.print_week_list()
            if c == "3":
                self.print_all_list()
            elif c == "4":
                self.missed_list()
            elif c == "5":
                self.add_task()
            elif c == "6":
                self.delete_list()
            elif c == "0":
                break
            # else:
            #     print("Please enter one of the displayed options")

    def print_list(self):
        d = datetime.today()
        today = d.date()
        rows = self.session.query(Task).filter(Task.deadline == today).all()
        if not rows:
            print("Nothing to do!")
        else:
            print("Today:")
            for i in range(len(rows)):
                print(f"{i + 1}) {rows[i]}")
    def print_week_list(self):
        d = datetime.today()
        today = d.date()
        rows = self.session.query(Task).all()
        # rows = self.session.query(Task).filter(Task.deadline.between(str(today), str(today + timedelta(days=7)))).all()
        # rows = self.session.query(Task).filter(Task.deadline <= str(today)).filter(Task.deadline >= str(today + timedelta(days=7))).all()
        # if not rows:
        #     print("Nothing to do!")
        # else:
        for i in range(7):
            rows = self.session.query(Task).filter(Task.deadline == str(today + timedelta(days=i))).all()
            print(f"\n{weekdays[(today + timedelta(days=i)).weekday()]} {(today + timedelta(days=i)).strftime('%d %b')}:")
            if not rows:
                print("Nothing to do!")
            else:
                for i in range(len(rows)):
                    print(f"{i + 1}) {rows[i]}")
    def print_all_list(self):
        rows = self.session.query(Task).all()
        if not rows:
            print("Nothing to do!")
        else:
            print("All tasks:")
            for i in range(len(rows)):
                print(f"{i + 1}) {rows[i].task}.{rows[i].deadline.strftime('%d %b')}")
    def add_task(self):
        item = input("Enter task\n")
        deadline = input("Enter deadline\n")
        if deadline =='':
            new_task = Task(task=item)
        else:
            new_task = Task(task=item, deadline =datetime.strptime(deadline, '%Y-%m-%d').date())
        self.session.add(new_task)
        self.session.commit()
        print("The task has been added!\n")

    def missed_list(self):
        d = datetime.today()
        today = d.date()
        rows = self.session.query(Task).filter(Task.deadline < today).order_by(Task.deadline).all()
        if not rows:
            print("Nothing is missed!")
        else:
            print("Missed tasks:")
            for i in range(len(rows)):
                print(f"{i + 1}) {rows[i].task}. {rows[i].deadline.strftime('%d %b')}")

    def delete_list(self):
        rows = self.session.query(Task).order_by(Task.deadline).all()
        if not rows:
            print("Nothing to do!")
        else:
            print("Chose the number of the task you want to delete:")
            for i in range(len(rows)):
                print(f"{i + 1}) {rows[i].task}. {rows[i].deadline.strftime('%d %b')}")
        # delete a specific row
        i = int(input())
        specific_row = rows[i - 1]  # in case rows is not empty
        self.session.delete(specific_row)

        # don't forget to commit changes
        self.session.commit()
        print("The task has been deleted!")
my_list = TaskList()
my_list.run()

