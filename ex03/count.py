import string
import sys
def text_analyzer(text):

    

    if not isinstance(text,str):
        print("Error: The argument must be a string.")
        return

    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char in string.punctuation:
            punctuation_count += 1

    print("le nombre de characteres majuscule est:",upper_count)
    print("le nombre de characteres minuscules est:",lower_count)
    print("le nombre d'espace est:",space_count)
    print("le nombre de ponctuation est",punctuation_count)
if __name__=="__main__": 
    try :
        arguments = sys.argv[1]
        text_analyzer(arguments)
    except:
        text = input("Please enter a string: ")
        text_analyzer(text)

