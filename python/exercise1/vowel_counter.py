#!/usr/bin/env python3

def num_vowels(text):
    """Return the number of vowels in string."""
    vowels = "aeiouy"
    num = 0
    for v in vowels:
        num += text.lower().count(v)        
    return num

def num_consonants(text):
    consonants= "bcdfghjklmnpqrstvwxz"
    num = 0
    for letter in text:
           num1 += text.lower().count(c)
    return num
    
text = str(input("Enter a sentence: "))
print("Number of vowels", num_vowels(text))
print("Number of consonants", num_consonants(text))
print("Number of vowels", num_vowels(text))
print("Number of consonants", num_consonants(text))


