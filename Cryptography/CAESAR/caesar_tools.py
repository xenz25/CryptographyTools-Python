#-------------------------------------------------------------------------------
# Name:        CAESAR ENCRYPTOR AND DECRYPTOR PROJECT V 1.0.0
# Purpose:     HOBBY AND EDUCATION
#
# Author:      Jolo Catacutan
#
# Created:     25/02/2020
# Copyright:   (c) Jolo Catacutan 2020
# Licence:     MIT LICENSE
#-------------------------------------------------------------------------------

class Caesar_Tools():
    '''This module can encrypt and decrypt input caesar text automatically, on the
    encrypt mode you are required to enter the shift count where as on the
    decrypt mode has two options:
        (1) Automatic, (2) Manual.
    the automatic will iterate 26 times in different shift counts and outputs a resulting text
    for every iteration the one with a human readable text is the shift count that suites
    to the encrypted text. The manual mode will ask for the shift count and
    will decrypt the text using that shift count

    The Formula that I use here is based on my studies and own cipher cracking techniques. Most cryptogaphers
    uses Frequency analysis to crack Caesar Cipher but I discovered that this cipher has a pattern and can be
    inserted in a formula. The formula that I discovered can crack any Caesar Ciphers instantly for a short time.
    '''

    def __init__(self):
        self.entered_text = ""
        self.__temp_letter = ""
        self.encrypted_text = ""
        self.decrypted_text = ""
        self.__encrypted_text_list =[]
        self.__decrypted_text_list =[]
        self.__auto_decrypted_text_list = []
        self.spacer = 'null'
        self.encrypt_shift_count = 0
        self.decrypt_shift_count = 0
        self.total_letters = 26
        self.__iteration_count = 1
        self.__auto_shift_count = 1


    def get_caesar_encrypted_text(self):
        '''Returns the encrypted text after using the encryptor method.
        '''
        self.encrypted_text = self.encrypted_text.join(self.__encrypted_text_list)
        return self.encrypted_text

    def get_caesar_decrypted_text(self):
        '''Returns the decrypted text after using the manual decryptor method.
        '''
        self.decrypted_text = self.decrypted_text.join(self.__decrypted_text_list)
        return self.decrypted_text

    def get_auto_decrypt_text_list_caesar(self):
        '''Returns the list of auto_generated text after using auto decryptor method.
        '''
        return self.__auto_decrypted_text_list

    def caesar_encryptor_formula(self,letters, shift_count):
        '''Returns the LETTER for the encrypted input Letter if Return is True.
        letters must be of type char or single character
        '''
        self.__temp_letter = ord(letters.upper())+(shift_count%self.total_letters) #using the formula
        if self.__temp_letter > 90: #if bigger than 90
            self.__temp_letter = chr(((self.__temp_letter%90)-1)+65)
        elif self.__temp_letter < 65: #if lesser than 65
            self.__temp_letter += 26
            self.__temp_letter = chr(self.__temp_letter)
        else:
            self.__temp_letter = chr(self.__temp_letter) #if in bounds

        return self.__temp_letter

    def caesar_decryptor_formula(self,letters, shift_count):
        '''Returns the LETTER for the decrypted input Letter if Return is True.
        letters must be of type char or single character
        '''
        self.__temp_letter = ord(letters.upper())-(shift_count%self.total_letters) #using the formula
        if self.__temp_letter > 90: #if bigger than 90
            self.__temp_letter = chr(((self.__temp_letter%90)-1)+65)#short cut formula to get remainder if number is bigger than 90 i dont think if this will happen
        elif self.__temp_letter < 65: #if lesser than 65
            self.__temp_letter += 26
            self.__temp_letter = chr(self.__temp_letter)
        else:
            self.__temp_letter = chr(self.__temp_letter) #if in bounds

        return self.__temp_letter

    def caesar_encrypt(self,text_in, shift_count, Return = False):
        '''
        text_in  = String/ char type
        shift_count = int type
        Return = boolean
        returns a list type if Return is True else store the encrypted text to the encypted text list.
        get the text and the shift count. Iterate over
        each text and analyze them if space is detected the set self.spacer will
        be added to the encrypted text list
        else if the answer using the formula is out of bounds from 65 to 90:
            if bigger than 90, 26 is subtracted
            if lesser than 65, 26 is added
        else if in bounds of 65 to 90 the converted ascii number to character
        will be added to the encrypted text list
        '''

        self.__encrypted_text_list = []
        self.encrypted_text = ""
        self.entered_text = text_in.upper()
        if type(shift_count) == 'float':
            self.encrypt_shift_count = round(shift_count+0.5)
        else: self.encrypt_shift_count = shift_count

        for letters in self.entered_text:
            if letters == ' ' or letters == 'null' or letters == 'NULL':
                self.__encrypted_text_list.append(self.spacer) #if space
            else:
                result = self.caesar_encryptor_formula(letters,self.encrypt_shift_count) #using the encryptor method formula
                self.__encrypted_text_list.append(result) #appending the character
        if Return:
            return self.__encrypted_text_list #returning the list of encrypted chracters

    def caesar_auto_decrypt(self,text_in, Show = True):
        '''The auto decryptor prints resulting text with the predicted Shift count number every iteration if Show is True.
        text_in = String/char
        Show = boolean
        you cannot use the method get_decrypt_text() after this because nothing will be printed.
        instead you can use get_auto_decrypt_text_list_caesar() method to get the result in a LIST with its corresponding SHIFT COUNT.
        any readable resulting text is the possible encrypted text.
        '''
        self.entered_text = text_in.upper()
        self.__auto_decrypted_text_list = []

        while self.__iteration_count <= 26:
            for letters in self.entered_text:
                if letters == ' ' or letters == 'null' or letters == 'NULL':
                    self.__decrypted_text_list.append(self.spacer) #if space
                else:
                    result = self.caesar_decryptor_formula(letters,self.__auto_shift_count) #using the decryptor method formula
                    self.__decrypted_text_list.append(result) #appending the character

            #adding the result to decrypted text list including the shift count
            self.__auto_decrypted_text_list.append(str(self.__auto_shift_count) + " : " + self.decrypted_text.join(self.__decrypted_text_list))
            if Show:
                print("Shift Count of {} : {}".format(self.__auto_shift_count,self.decrypted_text.join(self.__decrypted_text_list)))
            self.__iteration_count+=1
            self.__auto_shift_count +=1
            self.__decrypted_text_list = []


    def caesar_manual_decrypt(self,text_in, shift_count, Show = True):
        '''The manual decryptor prints text with shift count and decrypted text if Show is True.
        text_in = String/char
        shift_count = int
        Show = boolean
        if show is False you can access the result using the method 'get_decrypt_text()'
        '''
        self.__decrypted_text_list = []
        self.decrypted_text = ""
        self.entered_text = text_in.upper()
        self.decrypt_shift_count = shift_count

        for letters in self.entered_text:
            if letters == ' ':
                self.__decrypted_text_list.append(self.spacer) #if space
            else:
                result = self.caesar_decryptor_formula(letters,self.decrypt_shift_count) #using the decryptor method formula
                self.__decrypted_text_list.append(result) #appending the character

        if Show:
            print("Shift Count of {} : {}".format(self.decrypt_shift_count,self.decrypted_text.join(self.__decrypted_text_list)))



def main():
    #"DAHLOKIAKJASWJPAZPKGEHHIADAHLLHAWOADAHL"
    #"nkrvyuskutkcgtzkjzuqorrsknkrvvrkgyknkrv"
    #"HELPSOMEONEWANTEDTOKILLMEHELPPLEASEHELP"
    test_text = "nkrvyuskutkcgtzkjzuqorrsknkrvvrkgyknkrv"
    test_text2 = "HELPSOMEONEWANTEDTOKILLMEHELPPLEASEHELP"
    test_char = "H"
    caesar_test1 = Caesar_Tools()
    caesar_test1.spacer = ' '

    #using the encryptor method
    caesar_test1.caesar_encrypt(test_text2, 500, Return = False)
    x1 = caesar_test1.get_caesar_encrypted_text()
    print("Encrypted text result:",x1)

    print('\n')
    #using the auto_decryptor method
    caesar_test1.caesar_auto_decrypt(test_text, Show = True)
    print('\n')

    #using the manual_decryptor method
    caesar_test1.caesar_manual_decrypt(test_text, 500, Show = True)
    print("1st manual decryptor test:",caesar_test1.get_caesar_decrypted_text())

    #using the decryptor formula only
    x = caesar_test1.caesar_decryptor_formula(test_char,256)
    print("decryptor formula:",x)

    #using the encryptor formula only
    x = caesar_test1.caesar_encryptor_formula(test_char,256)
    print("encryptor formula:",x)

    #using the manual_decryptor method
    caesar_test1.caesar_manual_decrypt(x1, 100, Show = True)
    print("2nd manual decryptor test:",caesar_test1.get_caesar_decrypted_text())

if __name__ == '__main__':
    main()
