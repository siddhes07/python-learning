
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        result = []
        i = 0

        while i < len(words):
            j = i
            line_length = 0

            # Find words that fit in the current line
            while j < len(words) and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            # Number of words in the line
            num_words = j - i

            # Last line or only one word
            if j == len(words) or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                total_spaces = maxWidth - line_length
                gaps = num_words - 1

                spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (spaces + (1 if k - i < extra_spaces else 0))

                line += words[j - 1]

            result.append(line)
            i = j

        return result
