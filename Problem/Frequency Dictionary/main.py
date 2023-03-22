
# text = [v.lower() for v in input().split()]

text = "a aa abC aa ac abc bcd a"

# convert text to list of words
text_list = text.lower().split()
freq_dict = {}

for k, v in {v: text_list.count(v) for v in text_list}.items():
    print(f"{k} {v}")

for word in text_list:
    # set the default value to 0
    freq_dict.setdefault(word, 0)
    # increment the value by 1
    freq_dict[word] += 1

for key,value in freq_dict.items():
    print(key,value)


fruit_dictionary = {}
fruit_dictionary.setdefault("apple", "green")
fruit_dictionary.setdefault("banana", "yellow")
fruit_dictionary.setdefault("orange", "orange")

print(fruit_dictionary.setdefault("apple", "red"))