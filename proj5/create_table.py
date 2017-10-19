import os

DIR_OUTPUT = "input"
FILE_OUTPUT = "security_table.tex"
PATH_OUTPUT = os.path.join(DIR_OUTPUT, FILE_OUTPUT)


if not os.path.isdir(DIR_OUTPUT):
    os.mkdir(DIR_OUTPUT)


obj_assumpt = ["\\rotatebox{{90}}{{O.{}}}".format(name.upper()).replace('_','\\_')
        for name in [
                "TPM_KEY_STRG",
                "TRUSTZONE_NX",
                "DECOMM",
                "ID",
                "NO_TAMPER",
                "PWR_OUT",
                "ATTEST",
                "SECURE_COMMS",
                "TWO_WAY_PROT",
            ]
        ]
threats = ["T.{}".format(name.upper()).replace('_','\\_') for name in
        [
            "physical",
            "network",
            "mismanage",
            "adversarial",
            "persistent",
            "lost_asset",
            "management_testing",
            "signed_firmware",
            "srtp_recv",
            "flashmem_integrity",
            "jtag_abuse",
        ]
      ]


markings = [set(l) for l in [
          [0,1,2],
          [1],
          [3,4],
          [5,6],
          [5,8],
          [4,7],
          [1,2],
          [0,1,2,3,4],
          [2,4,5],
          [1,3],
          [0,7],
        ]
      ]

base_table = """
\\begin{{tabular}}{{{0}}}
 \\cline{{{1}-{2}}}
 \\multicolumn{{1}}{{c|}}{{}}{3}
{4}
\\end{{tabular}}
"""

def make_table_row(item_list):
    item_list = ' & '.join(item_list)
    item_list += " \\\\"
    item_list += "\n"
    item_list += "\\hline"
    return item_list

option_tabular = ("| l "+"| c "*len(obj_assumpt))+'|'
heading = make_table_row([' ']+obj_assumpt)

content_rows = []
for it, row in enumerate(threats):
    row_buffer = []
    for io, assump in enumerate(obj_assumpt):
        if io in markings[it]:
            row_buffer.append("X")
        else:
            row_buffer.append(" ")
    content_rows.append(row_buffer)

content = '\n'.join(["{} & ".format(name)+\
        make_table_row(content_rows[i]) for i, name in enumerate(threats)])


with open(PATH_OUTPUT, 'w') as fp:
    fp.write(base_table.format(option_tabular, 2, len(obj_assumpt)+1, heading, content))
    fp.write('\n')
