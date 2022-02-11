# -*- coding: utf-8 -*-

"""
Set the arguments with the following conditions and execute them in the terminal.

The first argument is an integer greater than or equal to 6, which is the number of characters in the password to be generated.
For the first argument, enter the number of characters of the password you want to generate as an integer.
For the second argument, enter 1 if you want to use uppercase letters, or 0 if you don't want to.
The third argument is 1 if the symbol is to be used, and 0 if it is not to be used.

Execution example --> gen_pass.py 12 1 1
"""

import sys
from random import sample, randrange

def UserInput():
    input_data = sys.argv[1:]

    if not len(input_data):
        print("Please specify an argument")

        return 0
    else:
        pass_len   = input_data[0] if input_data[0].isdigit() and int(input_data[0]) >= 6 else ""
        up_case    = input_data[1] if input_data[1] == "0" or input_data[1] == "1" else ""
        symbol     = input_data[2] if input_data[2] == "0" or input_data[2] == "1" else ""

    if pass_len and up_case and symbol:
        return CreateParameter(int(pass_len), int(up_case), int(symbol))
    else:
        print("The number of characters in the password is less than 6,\n or the other arguments are set to something other than 0 or 1.")

        return 0

def CreateParameter(pass_len, up_case, symbol):
    upcase_count      = pass_len // 4 if up_case else up_case
    symbol_count      = pass_len // 4 if symbol else symbol
    lowcase_num_count = pass_len - (upcase_count + symbol_count)
    lowcase_count     = lowcase_num_count // 2 if lowcase_num_count % 2 == 0 else lowcase_num_count // 2 + 1
    num_count         = lowcase_num_count // 2   
    
    return WordList(upcase_count, symbol_count, lowcase_count, num_count)

def WordList(upcase_count, symbol_count, lowcase_count, num_count):
    lowcase_list  = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
    num_list      = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    upcase_list   = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
    symbol_list   = ["@","#","=","/","$","%"]
    
    lowcae_choice = CreateWordList(lowcase_list, lowcase_count) 
    num_choice    = CreateWordList(num_list, num_count)
    upcase_choice = CreateWordList(upcase_list, upcase_count)
    symbol_choice = CreateWordList(symbol_list, symbol_count)

    join_word_list = lowcae_choice + num_choice + upcase_choice + symbol_choice

    return GeneratePassWord(join_word_list)
    

def CreateWordList(w_list, count_nm):
    if count_nm:
        return [w_list[randrange(len(w_list))] for i in range(count_nm)]
    else:
        return []

def GeneratePassWord(join_word_list):
    shuffle_list = sample(join_word_list, len(join_word_list))
    result_words = ''.join(shuffle_list)

    print(result_words)
    
    return 0


if __name__ == "__main__":
    UserInput()


