from collections import Counter

text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

freq_counter = Counter(text.split())
# num = int(input())
num = 7

for word, count in freq_counter.most_common(num):
    print(f'{word} {count}')

for x in freq_counter.most_common(num):
    print(*x)

for pair in freq_counter.most_common(num):
    print(" ".join(map(str, pair)))

numbers = {"first": 1, "second": 2, "third": 3, "fourth": 4}

print(numbers.get(4))

print(numbers.get("fourth"))

print(numbers.pop("fourth"))

print(numbers.popitem())

print(numbers.get(4, "4"))

# print(numbers.pop())

student = {'name': 'Kate', 'age': 20, 'specialty': 'biology'}
student.update(degree = 'bachelor')
print(student.get('age'))
print(student.pop('specialty'))
print(student.popitem())