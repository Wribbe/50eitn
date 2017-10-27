import os

table = [
        ("A Report structure", "2", "1"),
        ("B Product description + design requirements", "3", "1"),
        ("C Assumptions", "3", "1"),
        ("\\textbf{D High-level architectural overview}", "", ""),
        ("D1 General", "4", "2"),
        ("D2 TOE and ST", "5", "1"),
        ("\\textbf{E Security evaluation of design + summary}", "", ""),
        ("E1 General", "5", "0"),
        ("E2 Evaluation", "4", "0"),
       ]

row_format = "\\parbox{{8cm}}{{\\vspace{{3.0pt}} {} }} & {} & {} \\\\"
content = []

content = content
for desc, maxp, award in table:
    content.append(row_format.format(desc, maxp, award))
    content.append("\\hline")

content.append("\\hline")
content.append(row_format.format("Total:", "26", "6"))
content.append("\\hline")
content.append(row_format.format("Score:", "8", "2"))
content.append("\\hline")

with open(os.path.join('input','peer1.tex'), 'w') as fp:
   fp.write('\n'.join(content)+'\n')

