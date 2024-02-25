import string
letters = string.ascii_letters
code_letter = {}
shift = 6
message = "The goal keeper saved our ass."
new_message = ""
i = 1
for letter in range(0,len(letters)):
    if letter<26:
        if letter+shift > 25:
            code_letter[letters[letter]] = code_letter.get(letters[letter],letters[letter+shift-26])
        else:
            code_letter[letters[letter]] = code_letter.get(letters[letter],letters[letter+shift])
    else:
        if letter+shift > 51:
            code_letter[letters[letter]] = code_letter.get(letters[letter],letters[letter+shift-26])
        else:
            code_letter[letters[letter]] = code_letter.get(letters[letter],letters[letter+shift])
for letter in message:
    if letter in string.ascii_letters:new_message += code_letter[letter]
    else:new_message+=letter

print(code_letter)
print(new_message)

