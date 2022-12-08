### BWT + MTF

import sys
import os

def get_sort_key(word):
    key = 0
    for letter in word:
        key *= 10
        key += alphabet.index(letter)
    return key


def BWT(data):
    bwt = []

    for ind in range(len(data)):
        bwt.append(data[-ind:] + data[:-ind])


    bwt_sorted = sorted(bwt, key=get_sort_key)


    output = ""
    for word in bwt_sorted:
        output += word[-1]
    index = bwt_sorted.index(data) + 1
    return output, index

def MTF(data, alphabet, binary=False):
    result = []
    for letter in data:
        ind = alphabet.index(letter)
        if binary:
            
            result.append(bin(ind).replace("0b", ""))
        else:
            result.append(str(ind))
        
        alphabet = alphabet[ind:ind+1] + alphabet[:ind] + alphabet[ind+1:]
    return result


def main(binary=True):
    global alphabet
    if os.path.exists("coder_alphabet.txt"):
        with open("coder_alphabet.txt", "r") as file:
            alphabet = file.read().upper().split(", ")
    else:
        raise Exception('No "coder_alphabet.txt" file found')
    print(f"Alphabet from file:\n{alphabet}\n")
    data = input("Input data string:\n").upper()
    # data = "МАМА_МЫЛА_РАМУ"
    assert len(data) != 0, "Input is empty"
    for letter in list(set(data)):
        assert letter in alphabet, f'Letter "{letter}" not in the alphabet'
    
    output, index = BWT(data)

    print(f"Encoded by BTW sequence is:\n{output}\n{index}\n")

    result = MTF(output, alphabet, binary)

    print(f"Encoded by MTF sequence is:\n{' '.join(result)}\n")

    print('Results are saved in "encoded.txt"')

    with open("encoded.txt", "w") as file:

        file.write(" ".join(result) + "\n" + str(index))


if __name__ == "__main__":
    args = sys.argv[1:]
    if "-d" in args:
        main(binary=False)
    else:
        main()

    



    


