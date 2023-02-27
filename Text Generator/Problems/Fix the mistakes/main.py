# text = input()
text = "WWW.GOOGLE.COM uses 100-percent renewable energy sources and www.ecosia.com plants a tree for every 45 searches!"
words_list = text.split()
for i in range(len(words_list)):
    if 'www.' in words_list[i].casefold() or 'https://' in words_list[i].casefold() or 'http://' in words_list[i].casefold():
        print(words_list[i])


text = input().split()
print("\n".join(url for url in text if url.lower().startswith(('www.', 'https://', 'http://'))))