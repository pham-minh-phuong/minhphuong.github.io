vowels = ['a', 'e', 'i', 'o', 'u']
letter = str(input())
if letter in vowels:
    print("letter is a vowel")
elif letter == "y":
    print("sometimes y is a vowel, and sometimes y is a consonant")
else:
    print("letter is a consonant")