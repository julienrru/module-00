import string

def print_words_with_length(S, N):
    
    if not isinstance(S, str) or not isinstance(N, int):
        print("Error: Incorrect arguments")
        return   
    S = S translate(str.maketrans("",string.punctuation))   
    words = [word for word in S.split() if len(word) - word.count(string.punctuation) > N]
    print(words)