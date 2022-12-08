### FANO DECODING

import os

def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__, reverse=True)




def split(p, root="", r_ind=0):
    global dictionary
        
    if len(p) == 1:
        if root == "" and r_ind == 0:
            dictionary[alphabet[0]: "0"]
            return 1
        
        dictionary[alphabet[r_ind]] = root
        return 1

    ind = 1
    while abs(sum(p[:ind]) - sum(p[ind:])) > abs(sum(p[:ind+1]) - sum(p[ind+1:])):
        ind += 1
    split(p[:ind], root+"1", r_ind=r_ind)
    split(p[ind:], root+"0", r_ind=r_ind + ind)



def main():
    global dictionary 
    global alphabet

    if os.path.exists("decoder_alphabet.txt"):
        with open("decoder_alphabet.txt", "r") as file:
            alphabet = file.readline().split()
            p = file.readline().replace(",", ".").split()
            p = list(map(float, p))

    else:
        raise Exception('File "decoder_alphabet.txt" not found')

    assert len(p) == len(alphabet), "Length of probabilities and alphabet are not equal"
    sorted_ind = argsort(p)
    p = [p[ind] for ind in sorted_ind]
    alphabet = [alphabet[ind] for ind in sorted_ind]
    print(f"Alphabet from file is:\n {', '.join(alphabet)}\n")
    print(f"Alphabet probabilities from file is:\n {p}\n")
    dictionary = {}
    split(p)
    print(f"Dictionary, calculated from given alphabet is:\n{dictionary}\n")
    dictionary = {value: key for key,value in dictionary.items()}
    data = input("Input data for decoding:\n")
    result = ""
    start = 0
    for ind in range(1, len(data)+1):
        symbol_bin = data[start:ind]
        symbol = dictionary.get(symbol_bin)
        if symbol:
            result += symbol
            start = ind
    if start != ind:
        raise Exception("Alphabet doesn't contains symbols for given data")
    
    print(f"Data decoded:\n{result}")


if __name__=="__main__":
    
    main()
    
