import shelve

lib = shelve.open("my_library", writeback=True)
lib["Divergent trilogy"] = ["Divergent", "Insurgent", "	Allegiant"]
lib["The Lord of the Rings"] = ["The Fellowship of the Ring", "The Two Towers", "The Return of the King", "The Silmarillion"]

# write your code here
# del lib["The Lord of the Rings"][-1]
# temp = lib["The Lord of the Rings"]
# temp.pop(3)
# lib["The Lord of the Rings"] = temp
lib["The Lord of the Rings"].pop()
lib["The Lord of the Rings"] = lib["The Lord of the Rings"][:3]
print(len(lib["The Lord of the Rings"]))

lib.close()