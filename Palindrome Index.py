def is_palindrome(s):
    return s==s[::-1]
    
def palindromeIndex(s):
    for i in range(len(s)):
        new_string = s[:i] + s[i+1:]
        if is_palindrome(new_string):
            return i
    return -1
        
