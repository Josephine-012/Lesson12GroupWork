def reverse_string(text):
    reversed_text = ""
    for letter in text:
        reversed_text = letter + reversed_text
    return reversed_text

print(reverse_string("Hello"))
