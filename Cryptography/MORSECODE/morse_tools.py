#-------------------------------------------------------------------------------
# Name:        MORSE CODE TOOLS
# Purpose:      HOBBY AND EDUCATION
#
# Author:      Jolo Catacutan
#
# Created:     26/03/2020
# Copyright:   (c) Jolo Catacutan 2020
# Licence:     MIT LICENSE
#-------------------------------------------------------------------------------
import winsound
import time

class Morse_Tools():
    '''Morse tools is a module that enables you to:
        (1) play morse code
        (2) encrypt text to morse
        (3) decrypt morse code
    '''
    def __init__(self):
        self._short_freq = 500
        self._long_freq = 800
        self._short_dur = 60
        self._long_dur = 600
        self._sec_per_letter = 2
        self._morse_library_alpha = {
            "A" : ".- ", "B" : "-... ", "C" : "-.-. ", "D" : "-.. ",
            "E" : ". ", "F" : "..-. ", "G" : "--. ", "H" : ".... ",
            "I" : ".. ", "J" : ".--- ", "K" : "-.- ", "L" : ".-.. ",
            "M" : "-- ", "N" : "-. ", "O" : "--- ", "P" : ".--. ",
            "Q" : "--.- ", "R" : ".-. ", "S" : "... ", "T" : "- ",
            "U" : "..- ", "V" : "...- ", "W" : ".-- ", "X" : "-..- ",
            "Y" : "-.-- ", "Z" : "--.. "
        }
        self._morse_library_digit = {
            "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....",
            "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----. ", "0" : "-----"
        }
        self.combined_morse_library = {**self._morse_library_alpha,**self._morse_library_digit} #combined library of morse_code symbols
        self.text = ""
        self.morse_in = ""
        self.__encrypted_text = ""
        self.morse_decrypted_text= ""
        self.morse_encrypted_text = ""
        self.morse_spacer = ' '
        self.__do_play = True

    def short_beep(self):
        '''plays a short beep by the default parameters of short frequency and short duration'''
        try:
            winsound.Beep(self._short_freq,self._short_dur)
        except KeyboardInterrupt as e:
            self.__do_play = False

    def long_beep(self):
        '''plays a long beep by the default parameters of long frequency and long duration'''
        try:
            winsound.Beep(self._long_freq,self._long_dur)
        except KeyboardInterrupt as e:
            self.__do_play = False

    def letter_delay(self):
        '''pause the program for a default number of seconds when in between letter spaces'''
        try:
            time.sleep(self._sec_per_letter)
        except KeyboardInterrupt as e:
            self.__do_play = False

    def get_morse_code(self):
        '''returns the morse_code after using morse_encryptor method'''
        return self.morse_encrypted_text

    def get_decrypted_morse(self):
        '''returns the decrypted morse_code after using morse_decryptor method'''
        return self.morse_decrypted_text

    def show_morse_library(self):
        '''This will print the chart of morse code symbols for ALPHABETS and NUMBERS.'''
        print("ALPHABETS: ")
        for i in range(65,91):
            print(" {} : {}".format(chr(i),self.morse_encrypt(chr(i))))
        print("\nNUMBERS: ")
        for i in range(48,58):
            print(" {} : {}".format(chr(i),self.morse_encrypt(chr(i))))

    def morse_encrypt(self,text_in, Return = True):
        '''encrypts text_in parameter into equivalent morse_code. If Return is True it will return the morse_code.

        text_in = "String/char"
        Return = boolean
        '''
        self.text = text_in.upper()
        self.morse_encrypted_text = ""
        self.__encrypted_text = ""

        for letters in self.text:
            if letters == ' ': #excluding spaces
                pass
            else:
                if letters.isalpha(): #if letters use the morse library for alpha
                    self.__encrypted_text += self._morse_library_alpha[letters]
                elif letters.isdigit(): #if numbers use the morse library for digits
                    self.__encrypted_text += self._morse_library_digit[letters]
                else: #if none use the default spacer may cause some error if default spacer is change
                    self.__encrypted_text += self.morse_spacer
        self.morse_encrypted_text = self.__encrypted_text #assigning the final encrypted text to instance morse_encrypted_text

        if Return: #if Return is true the method will return the morse_code
            return self.__encrypted_text

    def morse_decrypt(self, morse_in, Return = True):
        '''decrypts morse_in parameter into equivalent letters or numbers. If Return is True it will return the decrypted text.

        morse_in = "String of morse_code"
        Return = boolean
        '''
        self.morse_in = morse_in #assigning the morse_in parameter to morse_in instance
        self.__temp_morse_store = "" #temporary storage of each symbols per iteration
        self.morse_decrypted_text = ""

        for symbols in self.morse_in: #iterating on each symbols
            self.__temp_morse_store += symbols #concatenating those symbols until a space is reached

            if symbols == ' ': #if spaced is reached, it is an indication that one symbol is stored and ready to be converted
                for morse_code_key, morse_code_val in self.combined_morse_library.items(): #iterating to combined library of morse codes
                    if self.__temp_morse_store == morse_code_val: #if the stored symbol matches one value of the combined library the key of that value will be assigned
                        self.morse_decrypted_text += morse_code_key #the key of the particular value will be concatenated to the morse_decrypted_text
                self.__temp_morse_store = "" #resetting the temporary symbol storage to accept new symbol

        if Return: #if Return is true it will return the decrypted text
            return self.morse_decrypted_text

    def play_morse(self,morse_in,show_interpreter = True, show_end = True):
        '''Uses winsound module of python, plays long and short beeps according to default methods short_beep and long_beep
        analyze the entered morse_code and play its equiavalent beep.
        the default frequencies and duration of each beep can be changed by accessing the short_freq and short_dur for short_beep,
        and long_freq and long_dur for long_beep. the default number of seconds for each character spaces can also be modified, but be careful of changing values.
        if show_end is True "END OF MORSE CODE" will be printed.
        if show_interpreter is True every analyzed symbol will be printed.

        morse_in = "String of morse_code"
        show_interpreter = boolean
        show_end = boolean

        '''
        self.morse_in = morse_in #assigning the morse_in to instance morse_in

        for symbols in morse_in.strip(): #iterating over each symbols
            if symbols == " ": #if character space pause the execution
                if show_interpreter:
                    print("space")
                self.letter_delay()
            elif symbols == ".": #if dot play short_beep()
                if show_interpreter:
                    print("dot")
                self.short_beep()
            elif symbols == "-": #if dash play long_beep()
                if show_interpreter:
                    print("dash")
                self.long_beep()

            if self.__do_play == False: #if execution suddenly stops the playing of morse will end and text will be printed
                print("=== PLAYING INTERRUPTED ===")
                break

        if self.__do_play and show_end: #if indicator show_end is True this will be printed
            print("=== END OF MORSE CODE ===")

def main():
    morse1 = Morse_Tools()

    #using the morse encryptor
    morse1.morse_encrypt("help me please")
    #getting the encrypted text
    x = morse1.get_morse_code()
    print(x)

    #using the morse decryptor
    print(morse1.morse_decrypt(x))

    #playing the morse_code
    morse1.play_morse(x)

    #using the morse encryptor
    morse1.morse_encrypt("meet me today")
    #getting the encrypted text
    y = morse1.get_morse_code()
    print(y)

    print(morse1.morse_decrypt(y,True))

    #playing the morse
    morse1.play_morse(y,False,False)

if __name__ == '__main__':
    main()
