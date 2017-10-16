import os

DIR_OUTPUT = "input"
FILE_OUTPUT = "security_table.tex"
PATH_OUTPUT = os.path.join(DIR_OUTPUT, FILE_OUTPUT)


if not os.path.isdir(DIR_OUTPUT):
    os.mkdir(DIR_OUTPUT)


problems = ["P{}".format(i) for i in range(13)]
solutions = ["S{}".format(i) for i in range(13)]

base_table = """
\\begin{{tabular}}{{{}}}
 \\hline
  {}
 \\hline
{}
\\end{{tabular}}
"""

def make_table_row(item_list):
    item_list = ' & '.join(item_list)
    item_list += " \\\\"
    item_list += "\n"
    item_list += "\\hline"
    return item_list

option_tabular = ("| r |"+"| c "*len(problems))+'|'
heading = make_table_row([' ']+problems)
content = '\n'.join(["S{} & ".format(i)+make_table_row(' '*len(problems)) for
    i, row in enumerate(solutions)])

with open(PATH_OUTPUT, 'w') as fp:
    fp.write(base_table.format(option_tabular, heading, content))
    fp.write('\n')
