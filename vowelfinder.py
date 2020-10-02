VOWELS = "aeiou"

letter = input('Enter a letter: ').lower()
if letter in VOWELS:
    print("Vowel")
elif 'a' < letter <= 'z':
    print("Consonant")
else:
    print("Invalid")
