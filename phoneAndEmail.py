#! pyhton3

import re,pyperclip

#Create a regex for phone numbers

phoneRegex = re.compile(r'''

# 731-994-5210, 994-5210, (731) 994-5210, 994-5210 ext 12345, ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?               # area code (optional)
(\s|-)                                 # first seperator
(\d\d\d)                               # first 3 digits
-                                      # seperator
(\d\d\d\d)                             # last 4 digits
(((ext(\.)?\s)|x)                      # extension word-part(optional)
(\d{2,5}))?                            # extension number-part(optional)
)
''',re.VERBOSE )

#todo: create a regex for email addresses

emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+             # name part
@                          # @ symbol
[a-zA-Z0-9_.+]+          # domain name part

''', re.VERBOSE)

#todo: Get the text off the clipboard
text = pyperclip.paste()

#todo: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
    
#todo: Copy yhe extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers)+ '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
