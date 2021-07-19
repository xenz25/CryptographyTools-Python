#-------------------------------------------------------------------------------
# Name:        ATBASH CIPHER TOOLS
# Purpose:      HOBBY AND EDUCATION
#
# Author:      Jolo Catacutan
#
# Created:     27/03/2020
# Copyright:   (c) Jolo Catacutan 2020
# Licence:     MIT LICENSE
#-------------------------------------------------------------------------------

class Atbash_Tools():
    def __init__(self):
        '''ATBASH is a special case type of AFINE cippher. What it does is reversing the ALPHABETS,
        substituting the firsl letter to the last letter the second letter to the second last letter and so on and so forth.
        There are two formula that I discovered while cracking this cipher:
            (1) By Alphabet Number Formula
            (2) By ASCII Code of Capital letters Formula

        This Module uses the 1st formula by default but I also include a Method where you can use the second formula.
        I discovered that the encryptor formula and decryptor formula for ATBASH cipher is the same.
        '''
        self.text = ""
        self.atbash_encrypted_text = ""
        self.atbash_decrypted_text = ""
        self.__encrypted_atbash_text_list = []
        self.__decrypted_atbash_text_list = []
        self._atbash_spacer = ' '
        self.__space_count = 0

    def atbash_encryptor_formula1(self, letter_in):
        '''
        This formula encrypt input text using the ALPHABET number formula.
        This method will ignore numbers.

        letter_in = char
        '''
        try: #checking for correct input
            letter_in = letter_in.upper()
        except:
            print("Error: Expected character type for \'letter_in\' but \'{}\' of type {} found.".format(letter_in, type(letter_in)))
        else:
            self.__temp_atbash_letter_encrypt = ""

            if letter_in.isdigit(): pass #ignoring numbers
            elif letter_in == ' ' and self.__space_count == 0:
                self.__space_count += 1
                self.__encrypted_atbash_text_list.append(self._atbash_spacer) #if space is detected spacer will be added
            elif letter_in == ' ' and self.__space_count == 1: pass #removing double spaces
            else:
                self.__space_count = 0
                # the ord(letter) - 64 will get the corresponding equivalent number for a letter ex. A = 1, Z = 26,
                #The diference to 27 will get the equivalent letter of the resulting number
                self.__temp_atbash_letter_encrypt = chr((27 - (ord(letter_in)-64))+ 64) #after getting the equivalent number +64 was again added to get the
                                                                                #equivalent asccii of that number and convert it to letter using chr()
            return self.__temp_atbash_letter_encrypt #returning the encrypted letter

    def atbash_decryptor_formula1(self, letter_in):
        '''This formula decrypt input text using the ALPHABET number formula.
        This method will ignore numbers.

        letter_in = char
        '''
        try: #checking for correct input
            letter_in = letter_in.upper()
        except:
            print("Error: Expected character type for \'letter_in\' but \'{}\' of type {} found.".format(letter_in, type(letter_in)))
        else:
            self.__temp_atbash_letter_decrypt = ""

            if letter_in.isdigit(): pass #ignoring numbers
            elif letter_in == ' ' and self.__space_count == 0:
                self.__space_count += 1
                self.__decrypted_atbash_text_list.append(self._atbash_spacer) #if space is detected spacer will be added
            elif letter_in == ' ' and self.__space_count == 1: pass #removing double spaces
            else:
                self.__space_count = 0
                 # the ord(letter) - 64 will get the correspomdimg equivalent number for a letter ex. A = 1, Z = 26,
                 #The diference to 27 will get the equivalent letter of the resulting number
                self.__temp_atbash_letter_decrypt = chr((27 - (ord(letter_in)-64))+ 64) #after getting the equivalent number +64 was again added to get the
                                                                                #equivalent asccii of that number and convert it to letter using chr()
            return self.__temp_atbash_letter_decrypt #returning the decrypted letter

    def atbash_encryptor_formula2(self, letter_in):
        '''This formula encrypt input text using the ASCII CODE formula.
        This method will ignore numbers.

        letter_in = char
        '''
        try: #checking for correct input
            letter_in = letter_in.upper()
        except:
            print("Error: Expected character type for \'letter_in\' but \'{}\' of type {} found.".format(letter_in, type(letter_in)))
        else:
            self.__temp_atbash_letter_encrypt2 = ""

            if letter_in.isdigit(): pass #ignoring numbers
            elif letter_in == ' ' and self.__space_count == 0:
                self.__space_count += 1
                self.__encrypted_atbash_text_list.append(self._atbash_spacer) #if space is detected spacer will be added
            elif letter_in == ' ' and self.__space_count == 1: pass #removing double spaces
            else:
                self.__space_count = 0
                self.__temp_atbash_letter_encrypt2 = chr(ord(letter_in)+(ord(letter_in)-(40+(3*(ord(letter_in)-65))))) #using the ASCII CODE formula

            return self.__temp_atbash_letter_encrypt2 #returning the encrypted letter

    def atbash_decryptor_formula2(self, letter_in):
        '''This formula decrypt input text using the ASCII CODE formula.
        This method will ignore numbers.

        letter_in = char
        '''
        try: #checking for correct input
            letter_in = letter_in.upper()
        except:
            print("Error: Expected character type for \'letter_in\' but \'{}\' of type {} found.".format(letter_in, type(letter_in)))
        else:
            self.__temp_atbash_letter_decrypt2 = ""

            if letter_in.isdigit(): pass #ignoring numbers
            elif letter_in == ' ' and self.__space_count == 0:
                self.__space_count += 1
                self.__decrypted_atbash_text_list.append(self._atbash_spacer) #if space is detected spacer will be added
            elif letter_in == ' ' and self.__space_count == 1: pass #removing double spaces
            else:
                self.__space_count = 0
                self.__temp_atbash_letter_decrypt2 = chr(ord(letter_in)+(ord(letter_in)-(40+(3*(ord(letter_in)-65))))) #using the ASCII CODE formula

            return self.__temp_atbash_letter_decrypt2 #returning the decrypted letter

    def get_atbash_encrypted_text(self):
        '''Returns current encrypted text.'''
        return self.atbash_encrypted_text

    def get_atbash_decrypted_text(self):
        '''Returns current decrypted text.'''
        return self.atbash_decrypted_text

    def atbash_encrypt(self, text_in, Return = True):
        '''This method will encrypt a given text.
        If Return is True the method will return the encryption result, else if False the result will be accessible using the:
            get_atbash_encrypted_text() method.

        text_in = String/char
        Return = boolean
        '''
        try: #checking for correct input
            self.text = text_in.upper().strip()
        except:
            print("Error: Expected character type or string type for \'text_in\' but \'{}\' of type {} found.".format(text_in, type(text_in)))
        else: #resseting
            self.atbash_encrypted_text = ""
            self.__encrypted_atbash_text_list = []
            self.__temp_letter_encrypt = ""

            for letters in self.text: #iterating over each letters
                self.__temp_letter_encrypt = self.atbash_encryptor_formula1(letters) #passing the letters to encryptor formula 1
                self.__encrypted_atbash_text_list.append(self.__temp_letter_encrypt) #appending the encrypted letter to encrypted list

            #joining the list and assigning it to atbash_encrypted_text
            self.atbash_encrypted_text = self.atbash_encrypted_text.join(self.__encrypted_atbash_text_list)

            if Return:
                return self.atbash_encrypted_text #returning the encrypted text

    def atbash_decrypt(self, text_in, Return = True):
        '''This method will decrypt a given text.
        If Return is True the method will return the decryption result, else if False the result will be accessible using the:
            get_atbash_decrypted_text() method.

        text_in = String/char
        Return = boolean
        '''
        try: #checking for correct input
            self.text = text_in.upper().strip()
        except: #resseting
            print("Error: Expected character type or string type for \'text_in\' but \'{}\' of type {} found.".format(text_in, type(text_in)))
        else:
            self.atbash_encrypted_text = ""
            self.__decrypted_atbash_text_list = []
            self.__temp_letter_decrypt = ""

            for letters in self.text: #iterating over each letters
                self.__temp_letter_decrypt = self.atbash_decryptor_formula1(letters) #passing the letters to decryptor formula 1
                self.__decrypted_atbash_text_list.append(self.__temp_letter_decrypt)  #appending the encrypted letter to decrypted list

            #joining the list and assigning it to atbash_decrypted_text
            self.atbash_decrypted_text = self.atbash_decrypted_text.join(self.__decrypted_atbash_text_list)

            if Return:
                return self.atbash_decrypted_text #returning the decrypted text



def main():
    test_text = "     hel787lo w345orld 12312 hello people     "
    test_char = 'A'
    atbash1 = Atbash_Tools()

    # using the atbash encryptor formula 1
    x_ = atbash1.atbash_encryptor_formula1(test_char)
    print(x_)

    # usiing the atbash decryptor formula 1
    x_1 = atbash1.atbash_decryptor_formula1(x_)
    print(x_1)

    # using the atbash encryptor method
    encrypted = atbash1.atbash_encrypt(test_text)
    print("encryption result:", encrypted)

    # using the atbash get encryptor method
    print(atbash1.get_atbash_encrypted_text())

    # using the atbash decryptor method
    decrypted = atbash1.atbash_decrypt(encrypted)
    print("decryption result:", decrypted)
    # using the atbash get decryptor method
    print(atbash1.get_atbash_decrypted_text())

    # using the atbash encryptor formula 2
    x1 = atbash1.atbash_encryptor_formula2(test_char)
    print(x1)

    # using the atbash decryptor formula 2
    x2 = atbash1.atbash_encryptor_formula2(x1)
    print(x2)


if __name__ == '__main__':
    main()
