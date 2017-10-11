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
  \\caption{{Representation of the stack created by the ROP.}}
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

instructions = [l.strip() for l in open('all_instructions.txt').readlines()]
print(instructions)
