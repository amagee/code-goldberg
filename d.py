from io import StringIO
import random
from bs4 import BeautifulSoup

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

sio = StringIO()

for line in lines:
    sio.write('<div class="line">')
    for char in line:
        sio.write(f'<span data-char="{char}" />')
    sio.write('</div>')

soup = BeautifulSoup(sio.getvalue(), 'html.parser')

pretty = soup.prettify()


colours = dict(
    header = '\033[95m',
    okblue = '\033[94m',
    okgreen = '\033[92m',
    warning = '\033[93m',
    fail = '\033[91m',
    endc = '\033[0m',
    bold = '\033[1m',
)


"""
# Not yet
print("\n" * 5)
print("\033[s", end="") # save
print("\033[5A", end="") # 5 up
print("\033[999D", end="") # 999 left
print("hello", end="")
print("\033[u", end="") # restore
print("\033[3A", end="") # 5 up
print("\033[999D", end="") # 999 left
print("\033[10C", end="") # 10 right
print("bye", end="")
"""


for line in pretty.split("\n"):
    if line.startswith("</div>"):
        print("")
    elif "data-char" in line:
        print(random.choice(list(colours.values())), end='')
        print(line[line.index('"') + 1], end='')

