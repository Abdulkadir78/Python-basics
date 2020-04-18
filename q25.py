'''
Assuming that we have some email addresses in the
"username@companyname.com" format, please write program to
print the company name of a given email address. Both user names
and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
google
'''

email = input('Enter the email id: ')
tl = email.split('@')
l = tl[1].split('.')
print(f'Company name: {l[0]}')


'''
ALTERNATE SOLUTION :

import re

email = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2, email)
print(r2.group(2))
'''
