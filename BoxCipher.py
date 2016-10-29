from time import sleep

def encrypt():
    instr = ''
    instr = input("\nEnter the Text to Encrypt: ")
    width = int(input("\nEnter the box width of your cipher : "))
    instr += '$'* (width - len(instr)%width) #Making the string to fit box size
    enc = ''
    for x in range(0,width):
        for i in range(x,len(instr),width):
            enc += instr[i]
    
    sleep(3)
    print("\nEncrypted Text: "+enc+'\n')

    
def decrypt():
    instr = input("\nEnter the Text to Decrypt: ")
    Len = len(instr)
    width = int(input("\nEnter the box width of your cipher : "))

    #To set the box size according to the Encrypted text
    if Len%width != 0:
        width = int(Len/width)
        width += 1
    else:
        width = int(Len/width)
    dec = ''
    for x in range(0,width):
        for i in range(x,Len,width):
            if instr[i] == '$':
                continue
            dec += instr[i]
    sleep(3)
    print("\nDecrypted Text: "+dec+'\n')
    
if __name__ == "__main__": 
    flag = 1
    while flag:
        print("\n\t\t   Encrypt/Decrypt Text using Caeser Box Cipher\n")
        sleep(2)
        choice = input("\nEnter whether to 'encrypt' or 'decrypt': ")
        if choice.lower() == 'encrypt':
              encrypt()
              flag = 0
        elif choice.lower() == 'decrypt':
              decrypt()
              flag = 0
        else:
              print("\nWrong Choice !\n")
              flag = 1

    
