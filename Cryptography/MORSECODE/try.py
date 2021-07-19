text = "aba"

x = {"A":".-- ", "B":"...--- ", " " : " "}
morse_code = ""

for te in text.upper():
    morse_code += x[te]


text2 = ".-- ...--- .--  .-- " 
temp_morse_code_store = ""
decrypted_text = ""

print(morse_code)


for letters in text2:
    temp_morse_code_store += letters
    print(">>", temp_morse_code_store)
    
    if letters == ' ':
        print(True)
        for key, val in x.items():
            if temp_morse_code_store == val:
                decrypted_text += key
        temp_morse_code_store = ""

        
            
print(decrypted_text)

morse_library_alpha = {
            "A" : ".- ", "B" : "-... ", "C" : "-.-. ", "D" : "-.. ",
            "E" : ". ", "F" : "..-. ", "G" : "--. ", "H" : ".... ",
            "I" : ".. ", "J" : ".--- ", "K" : "-.- ", "L" : ".-.. ",
            "M" : "-- ", "N" : "-. ", "O" : "--- ", "P" : ".--. ",
            "Q" : "--.- ", "R" : "-.- ", "S" : "... ", "T" : "- ",
            "U" : "..- ", "V" : "...- ", "W" : ".-- ", "X" : "-..- ",
            "Y" : "-.-- ", "Z" : "--.. ", " " : " "
        }
morse_library_digit = {
            "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....",
            "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----. ", "0" : "-----"
        }
combined_morse_library = {**morse_library_alpha,**morse_library_digit}

print(combined_morse_library)


    
