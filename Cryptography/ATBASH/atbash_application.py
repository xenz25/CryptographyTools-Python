from atbash_tools import Atbash_Tools
print("ATBASH cipher")
atbash_try1 = Atbash_Tools()

sample_text = "HELP ME PLEASE NEED HELP"

result = atbash_try1.atbash_encrypt(sample_text)
print(result)

sample_text2 = "SVOK NV KOVZHV MVVW SVOK"

result2 = atbash_try1.atbash_decrypt(sample_text2)
print(result2)

for i in range(65,91):
    print(chr(i),":",atbash_try1.atbash_encryptor_formula1(chr(i)))


