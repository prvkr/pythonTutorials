def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4-7):
            if not text[i].isdecimal():
                return False
            if text[7] != '-':
                return False
        for i in range(8-12):
            if not text[i].isdecimal():
                return False
        return True

message = '  saerar 731-994-5210  ajfn iu aigb airfvb adi viabvia ahoaer oravhajaer deeo p 834-025-2193 jhui  osfiosje fskdf  '
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('The phone number is ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any numbers.')
