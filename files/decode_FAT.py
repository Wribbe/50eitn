import re

FAT1 = \
"""
f0ff f003 4000 0560 0007 8000 09a0 000b
c000 0de0 000f 0001 1120 0113 4001 1560
0117 8001 19a0 011b c001 1de0 011f 0002
2120 0223 4002 2560 0227 8002 29a0 022b
c002 2de0 022f 0003 3120 0333 4003 3560
0337 8003 39a0 033b c003 3de0 033f 0004
4120 0443 4004 4560 0447 8004 49a0 044b
c004 4de0 044f 0005 5120 0553 4005 5560
0557 8005 59a0 055b c005 5de0 055f 0006
6120 0663 4006 6560 0667 8006 69a0 066b
c006 6da0 036f 0007 7120 0773 4007 7560
0777 8007 79a0 077b c007 7de0 077f 0008
8120 0883 4008 8560 0887 8008 89a0 088b
c008 8de0 088f 0009 9120 0993 4009 9560
0997 8009 99a0 099b c009 9de0 099f 000a
a120 0aa3 400a a560 0aa7 800a a9a0 0aab
c00a ade0 0aaf 000b b120 0bb3 400b b560
0bb7 800b b9a0 0bbb c00b bde0 0bbf 000c
c120 0cc3 400c c560 0cc7 800c c9a0 0ccb
c00c cde0 0ccf 000d d120 0dd3 400d d560
0dd7 800d d9a0 0ddb c00d dde0 0ddf 000e
e120 0ee3 400e e560 0ee7 800e e9a0 0eeb
c00e ede0 0eef 000f f120 0ff3 400f f560
0ff7 800f f9a0 0fff ffff ffff ff00 0000"""

root  = """
  00002600: 464f 5245 4e53 4943 5320 2008 0000 0000  FORENSICS  .....
  00002610: 0000 0000 0000 038a 1e31 0000 0000 0000  .........1......
  00002620: 4f55 5450 5554 2020 5458 5420 1817 118f  OUTPUT  TXT ....
  00002630: 1e31 1e31 0000 dd9b a130 0200 b2f1 0100  .1.1.....0......
  00002640: 4147 0072 006f 0075 0070 000f 0001 3000  AG.r.o.u.p....0.
  00002650: 3100 0000 ffff ffff ffff 0000 ffff ffff  1...............
  00002660: 4752 4f55 5030 3120 2020 2010 0051 368f  GROUP01    ..Q6.
  00002670: 1e31 1e31 0000 378f 1e31 fb00 0000 0000  .1.1..7..1......
  00002680: 4147 0072 006f 0075 0070 000f 0011 3000  AG.r.o.u.p....0.
  00002690: 3200 0000 ffff ffff ffff 0000 ffff ffff  2...............
  000026a0: 4752 4f55 5030 3220 2020 2010 000e 398f  GROUP02    ...9.
  000026b0: 1e31 1e31 0000 3a8f 1e31 fb00 0000 0000  .1.1..:..1......
  000026c0: e547 0072 006f 0075 0070 000f 00a1 3000  .G.r.o.u.p....0.
  000026d0: 3300 0000 ffff ffff ffff 0000 ffff ffff  3...............
  000026e0: e552 4f55 5030 3320 2020 2010 002b 3b8f  .ROUP03    ..+;.
  000026f0: 1e31 1e31 0000 3c8f 1e31 fd00 0002 0000  .1.1..<..1......
  00002700: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002710: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002720: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002730: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002740: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002750: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002760: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002770: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002780: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002790: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  000027a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  000027b0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  000027c0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  000027d0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  000027e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  000027f0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002800: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002810: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002820: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002830: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002840: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002850: 0000 0000 0000 0000 0000 0000 0000 0000  ................
  00002860: e552 4f55 5030 3920 2020 2010 0012 4e8f  .ROUP09    ...N.
  00002870: 1e31 1e31 0000 4f8f 1e31 0301 0002 0000  .1.1..O..1......
  00002880: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 """

def format_as_bytes(text):
    return [ ''.join([a,b]) for a,b in zip(text[0::2], text[1::2])]

def hexdump_to_bytes(text):
    hex_string = ""
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        tokens = re.split(r'\s+', line)
        hexes = tokens[1:8]
        hex_string += ''.join(hexes)
    return format_as_bytes(hex_string)

string = hexdump_to_bytes(root)

def hex_to_char(hexvalue):
    return chr(int(hexvalue, 16))

def bytelist_to_char(byte_list):
    return ''.join([hex_to_char(value) for value in byte_list])

def parse_dict_attributes(byte_list):
    return "NOT IMPLEMENTED"

def get_time(byte_list):
    return "NOT IMPLEMENTED"

def get_date(byte_list):
    return "NOT IMPLEMENTED"

def get_cluster(byte_list):
    return "NOT IMPLEMENTED"

def get_size(byte_list):
    return "NOT IMPLEMENTED"

directorie_structure = [
( 0, 8, "Filename", bytelist_to_char),
( 8, 3, "Extension", bytelist_to_char),
(11, 1, "Attributes", parse_dict_attributes),
(12, 2, "Reserved", None),
(14, 2, "Creation Time", get_time),
(16, 2, "Creation Date", get_date),
(18, 2, "Last Access Date", get_date),
(20, 2, "Ignore", None),
(22, 2, "Last Write Time", get_time),
(24, 2, "Last Write Date", get_date),
(26, 2, "First Logical Cluster", get_cluster),
(28, 4, "File Size (in bytes)", get_size),
]

dict_file = {}
for _, length, description, parsing_method in directorie_structure:
    # Extract bytes.
    attrib_byte_list = string[:length:]
    # Remove bytes from string.
    string = string[length:]
    if parsing_method:
        dict_file[description] = parsing_method(attrib_byte_list)

print(dict_file)
