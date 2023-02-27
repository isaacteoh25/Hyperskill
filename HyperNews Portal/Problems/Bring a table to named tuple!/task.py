from collections import namedtuple

# the subclass is named 'Person' in our case
student = namedtuple('Student', ['name', 'age', 'department'])
# field values can be defined either positionally or using the field names
# alina = Student('Alina', str('22'), 'linguistics')
# alex = Student('Alex', str('25'), 'programming')
# kate = Student(name='Kate', age=str('19'), department='age')
alina = student('Alina', '22', 'linguistics')
alex = student('Alex', '25', 'programming')
kate = student('Kate', '19', 'art')
# print(alina.name)  # Mary
# print(alex)  # person(name='David', age='33', occupation='lawyer')
# # the elements can also be accessed by their index, as in a regular tuple
# print(kate[2])
print(alina)
print(alex)
print(kate)