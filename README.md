# README

## Short description

This repository contains 2 executable python files:


`coder.py` - Encoder using **Burrows–Wheeler transform** algorithm + **MOVE-TO-FRONT** algorithm.

`decoder.py` - Decoder for **FANO** algorithm.

## Instructions

### Encoder

For executing `coder.py` script at first you need an alphabet in `coder_alphabet.txt` file, this file should contain all symbols used in data. You can see an example in this repo. For running script should use this command:
```shell
python3 coder.py
```

And then type data to be encoded. Result also saved in `encoded.txt` file.

Additionally you can use flag **`-d`** for result in decimal:
```shell
python3 coder.py -d
```

### Decoder

For executing `decoder.py` script at first you need an alphabet in `decoder_alphabet.txt` file, this file should contain all symbols used in data and probabilities for each symbol. You can see an example in this repo. For running script should use this command:
```shell
python3 decoder.py
```

And then type data to be decoded. Result will appear in therminal.
