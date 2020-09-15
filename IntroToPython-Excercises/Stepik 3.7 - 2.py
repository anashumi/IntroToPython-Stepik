initial_alph = str(input())
encryption_alph = str(input())
string_to_encrypt = str(input())
string_to_decode = str(input())

# encode 3rd string
# encode means replace all letters of initial_alph with same index letters of encryption_alph
encrypted_list = []
for letter in string_to_encrypt:
    letter_index = initial_alph.find(letter)
    encrypted_list.append(encryption_alph[letter_index])

# decode 4th string
# decode means replace all letters of encryption_alph with same index letters of initial_alph
decoded_list = []
for letter in string_to_decode:
    letter_index = encryption_alph.find(letter)
    decoded_list.append(initial_alph[letter_index])

# print results
print("".join(elem for elem in encrypted_list))
print("".join(elem for elem in decoded_list))