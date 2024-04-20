def hackerrankInString(s):
    target = 'hackerrank'
    index = 0
    s = s.lower()
    
    for char in s:
        if char == target[index]:
            index +=1
        if index == len(target):
            return "YES"
            
    return "NO"
    
