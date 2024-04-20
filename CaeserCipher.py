def caesarCipher(s, k):
    shifted_string = ""
    for char in s:
        if char.isalpha():
            new_char = chr((ord(char)-ord('a')+k)%26+ord('a')) if char.islower() \
            else chr((ord(char)-ord('A')+k)%26+ord('A'))
            shifted_string += new_char
        else:
            shifted_string += char
    
    return shifted_string
