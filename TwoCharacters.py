from itertools import combinations


def alternate(s):
    # Write your code here
    res = 0
    unique_chars = set(s)
    combos = combinations(unique_chars, 2)
    flag = True
    
    for combo in combos:
        t = [c for c in s if c == combo[0] or c == combo[1]]
        
        for i in range(len(t)-1):
            if t[i] == t[i+1]:
                flag = False
        if flag:
            res = max(res, len(t))
        flag = True
    return res
