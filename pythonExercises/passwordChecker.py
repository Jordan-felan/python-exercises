username = input("What is your username?")
password = input('What is your password')
pass_length = len(password)
starred_pass = '*' * pass_length

print(f'Hello, {username}! Your password {starred_pass} is {pass_length} characters long!')