print("\n======= SMART TEXT ANALYZER =======\n")

user_text = input(
    "Enter any sentence or paragraph: "
)

total_characters = len(user_text)

split_words = user_text.split()
total_words = len(split_words)

sentence_count = (
    user_text.count(".") +
    user_text.count("!") +
    user_text.count("?")
)

largest_word = ""

for word in split_words:
    if len(word) > len(largest_word):
        largest_word = word

print("\n====== TEXT ANALYSIS REPORT ======\n")

print(
    f"Total Characters : "
    f"{total_characters}"
)

print(
    f"Total Words : "
    f"{total_words}"
)

print(
    f"Sentence Count : "
    f"{sentence_count}"
)

print(
    f"Longest Word : "
    f"{largest_word}"
)

if total_words > 10:
    print("Text Quality : Detailed ✅")
else:
    print("Text Quality : Short ⚠️")
