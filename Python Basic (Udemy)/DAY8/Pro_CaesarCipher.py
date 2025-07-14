import CaesarArt
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l','m', 'n', 'o', 'p','q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']

def ceasar(StartText, shiftAmount, cipharDirection) :
    cipherText = ""
    for letter in StartText :
        if letter >= 'a' and letter <= 'z' :
            position = alphabet.index(letter)
            if cipharDirection == "encode" :
                newPostion = (position + shiftAmount) % 26
            elif cipharDirection == "decode" :
                newPostion = (position - shiftAmount) % 26
            newLetter = alphabet[newPostion]
            cipherText += newLetter
        else :
            cipherText += letter
    print(f"Here's the {cipharDirection} result : {cipherText}")

print(CaesarArt.logo)

ShouldContinue = "yes"
while ShouldContinue == "yes" :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n").lower()
    text = input("Type your message : \n").lower()
    shift = int(input("type the shift number : \n"))
    ceasar(StartText=text, shiftAmount=shift, cipharDirection=direction)
    ShouldContinue = input("Type 'yes' if you want to go again, Otherwise type 'no'. \n").lower()

print("Goodbye\n") 