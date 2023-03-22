# color_list = ['cyan', 'magenta', 'yellow', 'key color']
#
# cymk_file = open('CMYK.txt', 'w', encoding='utf-8')
# cymk_file.writelines(color_list)
# cymk_file.close()
file = open('animals.txt')
n_file = open('new_animals.txt', 'w')
text = file.readlines()
for n in text:
    if n[-1] != "\n":
        n_file.writelines(n)
    else:
        n_file.writelines(n[0:-1] + " ")
file.close()
n_file.close()