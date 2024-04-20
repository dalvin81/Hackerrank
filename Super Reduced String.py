def superReducedString(s):
    stack = []
  
    for char in s:
        if stack and stack[-1]==char:
            stack.pop()
        else:
            stack.append(char)
    res = "".join(stack)
  
    return res if res else 'Empty String'
