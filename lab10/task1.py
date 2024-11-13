def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


text = input("Enter a word or phrase: ")
print(f"Is palindrome: {is_palindrome(text)}")
