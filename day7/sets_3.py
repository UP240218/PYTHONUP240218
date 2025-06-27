# 1. Convert the ages to a set and compare lengths
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print("Original list length:", len(age))
print("Set length:", len(age_set))
# The list is longer because it includes duplicates

# 2. Explain differences between string, list, tuple, and set
explanation = """
- String: An ordered, immutable sequence of characters. e.g., "hello"
- List: Ordered, mutable collection that allows duplicates. e.g., [1, 2, 2]
- Tuple: Ordered, immutable collection that allows duplicates. e.g., (1, 2, 3)
- Set: Unordered, mutable collection of unique items. e.g., {1, 2, 3}
"""
print(explanation)

# 3. Unique words in the sentence
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
