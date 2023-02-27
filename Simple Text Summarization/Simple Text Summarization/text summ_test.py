from nltk.tokenize import WhitespaceTokenizer
file_name = input()
with open(file_name, "r", encoding="utf-8") as corpus:
    lines = corpus.read()
    tokens = WhitespaceTokenizer().tokenize(lines)
    # Tokenize a string on whitespace (space, tab, newline).
    # In general, users should use the string split() method instead.

def bigrams(tokens: list) -> list:
    bigram = []
    for i in range(len(tokens) - 1):
        result = tokens[i] + " " + tokens[i+1]
        bigram.append(result)
    return bigram

def bigram_statistics(bigram: list) -> None:
    all_bigrams = len(bigram)
    print(f"Number of bigrams: {all_bigrams}")
    while True:
        inp_index = input()
        if inp_index == "exit":
            break
        else:
            try:
                print("Head:", bigram[int(inp_index)].split()[0], "Tail:", bigram[int(inp_index)].split()[1])
            except IndexError:
                print("Index Error. Please input a value that is not greater than the number of all bigrams.")
                continue
            except ValueError:
                print("Type Error. Please input an integer.")
                continue

bigram_statistics(bigrams(tokens))