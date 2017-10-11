import os

OUTPUT_PATH="input"

stack_base = \
"""
\\begin{{figure}}[!h]
  \\centering
  \\begin{{tikzpicture}}
{}
  \\end{{tikzpicture}}
\\end{{figure}}
"""

elements =  [
    "This",
    "Is",
    "A",
    "Stack",
    "Of",
    "Elements",
]

current_x = 0.0
current_y = 0.0

rect_width = 3.0
rect_height = 0.5

internal_code_buffer = []

fmt_draw_rect = "    \\draw ({},{}) rectangle ({},{});"
fmt_text_node = "    \\node at ({:.4},{:.4}) {{{}}};"

for elem in reversed(elements):

    x1 = current_x
    y1 = current_y
    x2 = x1+rect_width
    y2 = y1+rect_height

    internal_code_buffer.append(fmt_draw_rect.format(x1,y1,x2,y2))

    nx = (x2-x1)/2
    ny = current_y+((y2-y1)/2)

    internal_code_buffer.append(fmt_text_node.format(nx,ny,elem))

    current_y += rect_height

if not os.path.isdir(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

with open(os.path.join(OUTPUT_PATH, 'stack_before.tex'), 'w') as fp:
    fp.write(stack_base.format('\n'.join(internal_code_buffer))+"\n")
