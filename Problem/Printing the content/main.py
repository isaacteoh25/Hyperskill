import shelve

lib = shelve.open("my_library")
lib["Twilight Saga"] = ["Twilight", "New Moon", "Eclipse", "Breaking Dawn"]

# write your code here
# lib = shelve.open("my_library", flag="c", writeback=True)
# print(lib["Twilight Saga"])
for key in lib:
    print(key + ": " + str(lib[key]))

lib.close()
