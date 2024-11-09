def is_palindrome(s1):
    if s1.lower() == s1[::-1].lower():
        return True
    return False

# example:
if __name__ == "__main__":
    print(is_palindrome("gunpla"))