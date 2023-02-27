import re
# a = input()
# a= "#How Long Does# It ###Take### #To #Learn #Python?"
# a = "#How Long!Do.#es #It ###Take### #To #Lea#rn #Python?"
# hash =re.split(', |\!|\?|\.| ', a)
# hash = re.findall(r"[\w']+", a)
# word = hash.replace('#',"").split()
# for w in word:
#     print(w)
# characters_to_remove = "#.,!?"
# for w in hash:
#     if re.findall("^#",w) and '#'not in w[1:]:
#         new_string = w
#         for character in characters_to_remove:
#             new_string = new_string.replace(character, "")
#         print(new_string)
x = input().split(" ")
for i in x:
    if i.startswith("#") == True and i.endswith("#") == False and "##" not in i:
        print(i.strip("#?!.,"))

def hashtag(word):
    hash_count, hash_id = 0, 0
    for i, v in enumerate(word):
        if v == "#":
            hash_id = i
            hash_count += 1
        if v in [".", " ", "!", "?", ","]:
            if hash_count == 1 and hash_id + 1 != i:
                print(word[hash_id + 1:i])
            hash_count = 0

hashtag(input())