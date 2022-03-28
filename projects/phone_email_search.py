'''
    Get the text off the clipboard.
    Find all phone numbers and email addresses in the text.
    Paste them onto the clipboard.
'''

import re
import pyperclip

# learning about regex
# https://automatetheboringstuff.com/2e/chapter7/

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                 # username
    @                                 # @ symbol
    [a-zA-Z0-9.-]+                    # domain name
    (\.[a-zA-Z]{2,4})                 # dot-something
    )''', re.VERBOSE)


text = str(pyperclip.paste())
match = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    match.append(phone_num)

for groups in email_regex.findall(text):
    match.append(groups[0])

if len(match) > 0:
    result = '\n'.join(match)
    pyperclip.copy(result)
    print('Copied to clipboard')
    print(result)
else:
    print('no phone number or email found')
