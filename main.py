from bs4 import BeautifulSoup
from functools import reduce
from operator import concat
import sys
import requests

def to_morse(s):
    EXCLUDED_CHARS = ['.', ',', '-']

    s = s.upper()
    morse_chart = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
    }
    morse = ''
    for char in s:
        if morse_chart.get(char) is not None:
            morse += morse_chart[char] + ' '
        elif char in EXCLUDED_CHARS:
            continue
        else:
            morse += char
    return morse

res = requests.get(input('URL to "Read this book online: HTML"'))
if not res.ok:
    print('Something went wrong while downloading the web')
    sys.exit(1)

soup = BeautifulSoup(res.text)
text = reduce(concat, [p.text for p in soup.body.find_all('p')])

with open('output.txt', 'w') as out:
    out.write(to_morse(text))
