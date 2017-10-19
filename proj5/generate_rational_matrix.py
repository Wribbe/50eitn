import os

table = [
        ("t.physical", "o.tamper, a.location", "The tamper detection.."),
        ("t.network", "o.1, a.1", ""),
        ("t.mismanage", "o.1, a.1", ""),
        ("t.adversarial", "o.1, a.1", ""),
        ("t.persistent", "o.1, a.1", ""),
        ("t.lost_asset", "o.1, a.1", ""),
        ("t.mng_test", "o.1, a.1", ""),
        ("t.signed_fw", "o.1, a.1", ""),
        ("t.srtp_recv", "o.1, a.1", ""),
        ("t.flash_integrity", "o.1, a.1", ""),
        ("t.jtag_abjuse", "o.1, a.1", ""),
       ]

row_format = "{} & \\parbox{{2.8cm}}{{ {} }} &\\parbox{{3cm}}{{\\vspace{{3.0pt}} {} }} \\\\"
content = []
for obj, mitigated, rationale in table:
    content.append(row_format.format(obj.upper().replace('_','\\_'),
        mitigated.upper(), rationale))
    content.append("\\hline")

with open(os.path.join('input','rationale.tex'), 'w') as fp:
   fp.write('\n'.join(content)+'\n')
