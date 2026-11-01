def validanagram(s, t):
    if len(s) != len(t):
        return False
    count = {}

    for char in s:
        count[char] = count.get(char,0)+1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1

    return all(value == 0 for value in count.values())
        
s = "anagram"
t = "nagaram"
print(validanagram(s,t))

