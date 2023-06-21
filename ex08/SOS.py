import sys
code_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}
def morse_message(message):
    encoded = []
    for char in message:
        if char == ' ':
            encoded.append('/')
        elif char.upper() in code_morse:
            encoded.append(code_morse[char.upper()])    
    return ' '.join(encoded)
if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
        print(morse_message(message))
    else:
        print('usage')                   
