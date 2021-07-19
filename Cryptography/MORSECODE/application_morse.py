from morse_tools import Morse_Tools

morse_try1 = Morse_Tools()

result1 = morse_try1.morse_encrypt("Python Is Fun")
print(result1)

result1_decrypted = morse_try1.morse_decrypt(result1)

print(result1_decrypted)
morse_try1.play_morse(result1)

#morse_try1.show_morse_library()
