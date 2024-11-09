def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


print(is_palindrome("Racecar"))   
print(is_palindrome("Hello"))     
print(is_palindrome("A man a plan a canal Panama"))  # True