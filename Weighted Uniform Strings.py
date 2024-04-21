def weightedUniformStrings(s, queries):
    weights = {}
    current = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current:
            count += 1
        else:
            for j in range(1, count+1):
                weight = (ord(current) - 96) * j
                weights[current*j] = weight
            current = s[i]
            count = 1
            
    for j in range(1, count+1):
        weight = (ord(current) - 96) * j
        weights[current*j] = weight
    vals = list(weights.values())
    res = []
    
    for query in queries:
        if query in vals:
            res.append('Yes')
        else:
            res.append('No')
    return res
