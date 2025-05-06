# Check if a string is palindrome

def is_palindrome(s):
    return s == s[:: -1]

print("is palindrome =  ",is_palindrome("MadaM"))
print("is palindrome =  ",is_palindrome("Suns"))