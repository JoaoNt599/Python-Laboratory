def is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

# example:
if __name__ == "__main__":
    s1 = 'Emperor Nero'
    s2 = 'Emperor Octavian'
    print(is_anagram(s1,s2))