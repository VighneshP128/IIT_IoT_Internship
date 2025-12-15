def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


def count_consonants(s):
    count = 0
    for ch in s:
        if ch.isalpha() and ch.lower() not in "aeiou":
            count += 1
    return count


def vowel_consonant_ratio(vowels, consonants):
    if consonants == 0:
        return 0
    return vowels / consonants

string = input("Enter a string: ")

vowels = count_vowels(string)
consonants = count_consonants(string)
ratio = vowel_consonant_ratio(vowels, consonants)

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Vowel to Consonant Ratio:", ratio)