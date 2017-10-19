import os

DIR_OUTPUT = "input"
FILE_OUTPUT = "security_table.tex"
PATH_OUTPUT = os.path.join(DIR_OUTPUT, FILE_OUTPUT)


if not os.path.isdir(DIR_OUTPUT):
    os.mkdir(DIR_OUTPUT)


problems = ["\\rotatebox{{90}}{{P{}.some-name}}".format(i) for i in range(14)]
solutions = ["S{}.some-name".format(i) for i in range(14)]

base_table = """
\\begin{{tabular}}{{{0}}}
 \\cline{{{1}-{2}}}
 \\multicolumn{{1}}{{c|}}{{}}{3}
 \\cline{{{1}-{2}}}
{4}
\\end{{tabular}}
"""

def make_table_row(item_list):
    item_list = ' & '.join(item_list)
    item_list += " \\\\"
    item_list += "\n"
    item_list += "\\hline"
    return item_list

option_tabular = ("| r "+"| c "*len(problems))+'|'
heading = make_table_row([' ']+problems)
content = '\n'.join(["{} & ".format(name)+\
        make_table_row(' '*len(problems)) for name in solutions])

with open(PATH_OUTPUT, 'w') as fp:
    fp.write(base_table.format(option_tabular, 2, 15, heading, content))
    fp.write('\n')
