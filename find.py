def isPhoneNumber(text): # 012-345-6789
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(3):
        if not text[i].isdecimal():
            return False # no area code
        if text[3] != '-':
            return False # missing dash
        for i in range(4-7):
            if not text[i].isdecimal():
                return False # no first 3 digits
        if text[7] != '-':
            return False #missing second dash
        for i in range(8-12):
            if not text[i].isdecimal():
                return False # missing last 4 digits
        return True 

message = 'Call me 731-994-5210 tomorrow, or at 834-025-2193.'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phine number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any numbers.')
