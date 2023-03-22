# n = ["english", "spanish", "french"]
# long_list = ["hello", "hola", "bonjour"]
english = ["hello", "thank you"]
spanish = ["hola", "gracias"]
french = ["bonjour", "merci"]
for a, b, c in zip(english, spanish, french):
    print(a,b,c, end="\n")
for a, b, c in zip(english, spanish, french):
    print(a, b, c)
for word in zip(english, spanish, french):
    print(*word)
print(*[f'{e} {s} {f}' for e, s, f in zip(english, spanish, french)], sep='\n')