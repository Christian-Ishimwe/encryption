import logo
letter = ["A", "B", "C", "D","E","F","G","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A", "B", "C", "D","E","F","G","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A", "B", "C", "D","E","F","G","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#importing my logo
logo.mine()
bol=True
#allowing the user to enter the text
def cypher_continue():
    text = input("What text to encode:\n").upper()
    #user for choosing the shifting number
    shift=int(input("What shift number:\n"))
    shift=shift%26
    #method of encryption
    hook = input("Write 'encode' or 'decode':\n")

    def caesar(start_text,shift_amount,direct):
        word=""
        for lett in start_text:
            if lett in letter:
                position=letter.index(lett)
                #if direction id encode
                if direct=="encode":
                    new_position=position+shift
                #if the direction is decode
                elif direct=="decode":
                    new_position=position-shift
                reserve=letter[new_position]
                word+=reserve
            else:
                word+=reserve
        print(f"Your {direct} is: {word}")
    caesar(start_text=text,shift_amount=shift,direct=hook)
    cont=input("Do you want to continue: 'yes' or 'no':\n")
    if cont=="yes":
        bol=True
    else:
        bol=False
cypher_continue()
if bol==True:
    cypher_continue()
elif bol==False:
    print("thank you!")


'''after minimising the code by using 
functions input 
'''
# def encrypt(plain_text, shift_amount):
#     word=""
#     for lett in plain_text:
#         position=letter.index(lett)
#         new_position = position+shift
#         encrypt_word= letter[new_position]
#         word+=encrypt_word
#     print(f"Your encrypted message is: {word}")
# encrypt(plain_text=text,shift_amount=shift)

# def decrypt(plain_text,shift_amount):
#     word=""
#     for lett in plain_text:
#         position=letter.index(lett)
#         new_position=position-shift
#         decrypt_word=letter[new_position]
#         word+=decrypt_word
#     print(f"Your decoded word of {text} is: {word}")

# if hook=="encode":
#     encrypt(plain_text=text,shift_amount=shift)
# elif hook=="decode":
#     decrypt(plain_text=text,shift_amount=shift)









# def encry(new_text,shift_number):
#     new_word=""
#     for lett in new_text:
#         position = letter.index(lett)
#         new_position = position+shift_number
#         encr_word = letter[new_position]
#         new_word +=encr_word
#     print(f"The encryipted message is {new_word}")
# encry(new_text=text,shift_number=shift)

# def decry(old_text,return_shift):
#     for lett in 