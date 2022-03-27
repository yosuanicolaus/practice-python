import string
import random

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = '1234567890'
specials = '~`! @#$%^&*()_-+={[}]|\:;"\'<,>.?/'

key = uppercase + lowercase + numbers + specials
pw_length = 16

password = ''.join(random.sample(key, pw_length))
print(password)
