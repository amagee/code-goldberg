from io import StringIO
import random
from bs4 import BeautifulSoup
import time
import math


d = {
    '_': [
        1, 5, 12, 14, 43, 49, 51, 111, 116, 117, 118, 125, 126, 127, 131,
        132, 139, 140, 141, 142, 143, 146, 148, 149, 154, 155, 165,
        171, 180, 196, 202, 203, 209, 225, 226, 234, 250, 263, 267, 271,
        275, 278, 279, 280, 282, 284, 287, 288, 289, 296, 299, 303,
        304, 305, 308, 313, 316, 317, 319, 321
    ],
    '\n': [53, 107, 161, 215, 269],
    '|': [
        54, 56, 58, 60, 65, 67, 69, 96, 98, 102, 104, 106, 108,
        110, 112, 114, 119, 121, 123, 150, 152, 156, 158, 160, 162, 168,
        175, 177, 199, 204, 206, 212, 214, 216, 218, 220, 222, 229, 231,
        237, 253, 255, 258, 260, 264, 266, 268, 272, 274, 281, 283,
        285, 307, 309, 312, 314
    ],
    '/': [169, 178, 189, 192, 194, 207, 227, 247, 276, 290, 297, 300, 306],
    '\\': [173, 182, 185, 187, 190, 198, 240, 270, 277, 286, 295, 298, 302, 315],
    "'": [201],
    '`': [210],
    '(': [233, 249, 262, 320],
    ')': [235, 251, 322],
    'V': [242, 245],
    ',': [318]
}


l = [" "] * 323

for k, v in d.items():
    for i in v:
        l[i] = k

s = "".join(l)

lines = s.split("\n")
max_line_length = max([len(l) for l in lines])

sio = StringIO()

for line in lines:
    sio.write('<div class="line">')
    for char in line:
        sio.write(f'<span data-char="{char}" />')
    sio.write('</div>')

soup = BeautifulSoup(sio.getvalue(), 'html.parser')

pretty = soup.prettify()


bold = "\x1b[1m";

curlyboi_colours = [
 "\x1b[38;5;112m", # green
 "\x1b[38;5;11m", # yellow
 "\x1b[38;5;214m", # orange
 "\x1b[38;5;1m", # red
 "\x1b[38;5;17m", # blue
]


rand_colours = [
    '\033[95m',
    '\033[94m',
    '\033[92m',
    '\033[93m',
    '\033[91m',
]
                           

characters = []

line_index = 0
char_index = 0
for line in pretty.split("\n"):
    if line.startswith("</div>"):
        line_index += 1
        char_index = 0
    elif "data-char" in line:
        char = line[line.index('"') + 1]
        characters.append((line_index, char_index, char))
        char_index += 1


class CurlyBoiColourGetter:
    def __init__(self, num_curlybois):
        self.curlybois = curlyboi_colours * num_curlybois

    def __call__(self, line_index, char_index, char):
        return self.curlybois[math.floor(char_index * len(self.curlybois) / max_line_length)]


def get_colour_2(line_index, char_index, char):
    return random.choice(rand_colours)


random.shuffle(characters)

print("\n" * 10)
print("\033[s", end="") # save

for i in range(0, 10):
    for color_getter in (CurlyBoiColourGetter(random.randint(1, 5)), get_colour_2):
        for line_index, char_index, char in characters:
            print("\033[u", end="") # restore
            print("\033[s", end="") # save
            print(f"\033[{7 - line_index}A", end="") # up
            print("\033[999D", end="") # 999 left
            print(f"\033[{char_index + 1}C", end="") # right

            colour = color_getter(line_index, char_index, char)
            print(bold, end='')
            print(colour, end='')
            print(char, end="", flush=True)
            time.sleep(0.003)
        time.sleep(0.5)

print("\n" * 7)

