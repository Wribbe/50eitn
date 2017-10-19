import os

table = [
        ("t.physical", "o.tpm_key_strg o.trustzone_nx o.decomm o.tamper a.location ", " The tamper detection notifies User and Maintenance Personnel if camera is taken down from wall and/or if someone is trying to open up camera, this will make the camera serve its purpose: detect intruders. The camera is also assumed to be positioned at above average human height on wall, thus minimising risk for casual vandalisation."),
        ("t.network", "o.trustzone_nx o.secure_comms", "Explain why"),
        ("t.mismanage", "o.id o.no_tamper a.adversarial", "Wait, but why?"),
        ("t.adversarial", "o.pwr_out o.attest o.trustzone_nx o.two_ways_prot a.adversarial", "This is because."),
        ("t.persistent", "o.pwr_out o.two_way_prot", "I know this!"),
        ("t.lost_asset", "o.no_tamper o.secure_comms", "Commies are good."),
        ("t.mng_test", "o.trustzone_nx o.decomm", "I changed my mind. Capitalism ftw!"),
        ("t.signed_fw", "o.tpm_key_strg o.trustzone_nx o.decomm o.id o.no_tamper", "Lots of good things here."),
        ("t.srtp_recv", "o.decomm 0.no_tamper o.pwr_out", "Security in real time? Sign me up!"),
        ("t.flash_integrity", "o.trustzone_nx o.id", "Adobe flash <3"),
        ("t.jtag_abuse", "o.tpm_key_strg o.secure_comms", "Oh, so KGB?"),
       ]

row_format = "{} & \\parbox{{4.0cm}}{{\\vspace{{3.5pt}} {} }} &\\parbox{{6cm}}{{\\vspace{{3.0pt}} {} }} \\\\"
content = []
for obj, mitigated, rationale in table:
    content.append(row_format.format(obj.upper().replace('_','\\_'),
        mitigated.upper().replace('_','\\_'), rationale))
    content.append("\\hline")

with open(os.path.join('input','rationale.tex'), 'w') as fp:
   fp.write('\n'.join(content)+'\n')
