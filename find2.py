import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
print(phoneNumRegex.findall('Call me 731-994-5210 tomorrow, or at 834-025-2193.'))
