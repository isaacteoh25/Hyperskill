import argparse
import re
import statistics
import math


def count_syllables(word):
    word = word.strip(",.!?;:")
    n_syllables = 0
    if word[-1] == "e":
        word = word[:-1]
    previous_letter = None
    for i, letter in enumerate(word):
        if letter in VOWELS and (i == 0 or previous_letter not in VOWELS):
            n_syllables += 1
        previous_letter = letter
    if n_syllables < 1:
        n_syllables = 1
    return n_syllables


def ari(chars, wds, sents):
    return round(4.71 * (len(chars) / len(wds)) + 0.5 * (len(wds) / len(sents)) - 21.43, 2)


def fk(sylls, wds, sents):
    return round(0.39 * (len(wds) / len(sents)) + 11.8 * (sum(sylls) / len(wds)) - 15.59, 2)


def smog(polysylls, sents):
    return round(1.043 * (len(polysylls) * 30 / len(sents)) ** 0.5 + 3.1291, 2)


def cl(chars, wds, sents):
    return round(0.0588 * (100 * len(chars) / len(wds)) - 0.296 * (100 * len(sents) / len(wds)) - 15.8, 2)


def pb(dif_wds, wds, sents):
    score = 0.1579 * (amnt_dif := (len(dif_wds) / len(wds))) * 100 + 0.0496 * (len(wds) / len(sents))
    return round(score if amnt_dif < 0.05 else score + 3.6365, 2)


VOWELS = {"a", "e", "i", "o", "u", "y"}
LEVELS = {1: 6, 2: 7, 3: 9, 4: 10, 5: 11, 6: 12, 7: 13, 8: 14, 9: 15, 10: 16, 11: 17, 12: 18, 13: 24, 14: 25}
PB_LEVELS = {4: 10, 5: 12, 6: 14, 7: 16, 8: 18, 9: 24}
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infile")
parser.add_argument("-w", "--words")
args = parser.parse_args()
easy_words = []
with open(args.words) as words_file:
    for line in words_file:
        easy_words.extend(line.strip(",.?!;: \n()").split(" "))
with open(args.infile) as file:
    text = "\n".join(file.readlines()).strip()
    sentences = re.split(r"(?<=[.!?])[ \n\t]", text)
    words = [word.lower() for sentence in sentences for word in re.split(r"[ \n\t]", sentence)]
    difficult_words = [word.strip(",.?!;: \n()").lower() for word in words if word.strip(",.?!;: \n()").lower() not in easy_words]
    syllables = [count_syllables(word) for word in words]
    polysyllables = [syllable for syllable in syllables if syllable > 2]
    characters = [character for word in words for character in word]

    print(f"""The text is:
    {text}

    Words: {len(words)}
    Difficult words: {len(difficult_words)}
    Sentences: {len(sentences)}
    Characters: {len(characters)}
    Syllables: {sum(syllables)}
    Polysyllables: {len(polysyllables)}""")
    score_type = input("Enter the score you want to calculate (ARI, FK, SMOG, CL, PB, all): ")
    ages = []
    if score_type in ["ARI", "all"]:
        print(
            f"\nAutomated Readability Index: {(a := ari(characters, words, sentences))} (about {(age := LEVELS.get(round(a)) or LEVELS[14])}-year-olds).")
        ages.append(age)
    if score_type in ["FK", "all"]:
        print(
            f"Flesch–Kincaid readability tests: {(a := fk(syllables, words, sentences))} (about {(age := LEVELS.get(round(a)) or LEVELS[14])}-year-olds).")
        ages.append(age)
    if score_type in ["SMOG", "all"]:
        print(
            f"Simple Measure of Gobbledygook: {(a := smog(polysyllables, sentences))} (about {(age := LEVELS.get(round(a)) or LEVELS[14])}-year-olds).")
        ages.append(age)
    if score_type in ["CL", "all"]:
        print(
            f"Coleman–Liau index: {(a := cl(characters, words, sentences))} (about {(age := LEVELS.get(round(a)) or LEVELS[14])}-year-olds).")
        ages.append(age)
    if score_type in ["PB", "all"]:
        print(
            f"Probability-based score: {(a := pb(difficult_words, words, sentences))} (about {(age := PB_LEVELS.get(math.floor(a)) or PB_LEVELS[9])}-year-olds).")
        ages.append(age)
    if score_type == "all":
        print(f"\nThis text should be understood in average by {round(statistics.mean(ages), 0)} year olds.")