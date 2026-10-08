from collections import Counter

# Take input from user
s = input("Enter string: ")

n = int(input("Enter number of words: "))

words = []
for i in range(n):
    word = input(f"Enter word {i + 1}: ")
    words.append(word)


def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count

    if total_len > len(s):
        return []

    word_freq = Counter(words)
    result = []

    # Try every possible starting offset
    for start in range(word_len):
        left = start
        right = start
        count = 0
        current_freq = {}

        while right + word_len <= len(s):
            word = s[right:right + word_len]
            right += word_len

            if word in word_freq:
                current_freq[word] = current_freq.get(word, 0) + 1
                count += 1

                # Too many occurrences of this word
                while current_freq[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    current_freq[left_word] -= 1
                    left += word_len
                    count -= 1

                # All words matched
                if count == word_count:
                    result.append(left)

            else:
                current_freq.clear()
                count = 0
                left = right

    return result


answer = findSubstring(s, words)

print("Starting indices:", answer)
