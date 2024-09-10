x = "aebcbda"

chars_to_remove = {'e', 'd'}


result = ''.join(char for char in x if char not in chars_to_remove)

print(result)
