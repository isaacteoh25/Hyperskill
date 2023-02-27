numbers = [int(num) for num in iter(input, ".")]
print(sum(numbers) / len(numbers))

num_list = []

while True:
    number = input()
    if number == '.':
        break
    num_list.append(int(number))

print(sum(num_list) / len(num_list))