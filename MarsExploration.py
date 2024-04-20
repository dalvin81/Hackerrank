def marsExploration(s):
    ref = 'SOS'
    res = 0
    for i in range(0, len(s), 3):
        for char1, char2 in zip(ref, s[i:i+3]):
            if char1 != char2:
                res += 1
    return res
