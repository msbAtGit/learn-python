#Counting the number of characters 
# in a string using collections library
# in python

from collections import Counter

text = "Example string"
character_count = Counter(text)

print(character_count)


text = "example string"
character_count = Counter(text)
max_occurrence = character_count.most_common(1)[0]

print("The maximum occurring character is:", max_occurrence[0])