import string
def text_analyzer(text):
    if text is None:
        text = input("Please enter a string: ")

    if not isinstance(text):
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
    ("text_analyser")
    print("le nombre de characteres majuscule est:")