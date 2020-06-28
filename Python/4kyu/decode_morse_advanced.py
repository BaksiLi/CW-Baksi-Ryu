#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Decode the Morse code, advanced
# https://www.codewars.com/kata/54b72c16cd7f5154e9000457/solutions/python


def decode_bits(bitstr: str) -> str:
    bitstr_ = bitstr.strip('0')
    u = len(
        sorted(set(bitstr_.split('1') + bitstr_.split('0')) - {''}, key=len)[0]
    )
    return bitstr_.replace('111' * u, '-').replace('1' * u, '.').replace(
        '0000000' * u, '  '
    ).replace('000' * u, ' ').replace('0' * u, '')


def decode_morse(morsecode: str):
    decoded = ''

    for word in morsecode.split('  '):
        for letter in word.split(' '):
            decoded += MORSE_CODE[letter]
        decoded += ' '

    return decoded.strip()


# MORSE_CODE is given as
MORSE_CODE = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.----.': "'",
    '-.-.--': '!',
    '-..-.': '/',
    '-.--.': '(',
    '-.--.-': ')',
    '.-...': '&',
    '---...': ':',
    '-.-.-.': ';',
    '-...-': '=',
    '.-.-.': '+',
    '-....-': '-',
    '..--.-': '_',
    '.-..-.': '"',
    '...-..-': '$',
    '.--.-.': '@',
    '...---...': 'SOS'
}
