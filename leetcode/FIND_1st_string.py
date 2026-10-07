def strStr(haystack, needle):
    return haystack.find(needle)


haystack = input("Enter haystack: ")
needle = input("Enter needle: ")

result = strStr(haystack, needle)

print("Index:", result)