import os

table = [
        ("t.physical", "o.tamper a.location ",
            """
            Since the camera is assumed to be located at a position which is
            not reachable unassisted, unauthorized direct physical access to the unit should
            be rare. In the case of the camera being removed from its mounting
            position or opened, the tamper sensors will detect this and notify
            maintenance personnel.
            """),
        ("t.network", "o.trustzone_nx o.secure_comms o.two_ways_prot", "Explain why"),
        ("t.mismanage", "o.no_tamper \no.id a.no_adversarial", "Tamper detection will trigger if camera is not mounted correctly" \
        + " or case is not closed correctly when mounting or remounting. ID will help how?" \
        + " The background checks that are carried out on personnel are partly done to catch" \
        + "any potential criminal record but also to screen for persons that can perform well in their job."),
        ("t.adversarial", "o.pwr_out o.attest o.trustzone_nx o.two_ways_prot a.no_adversarial", "Attestation is carried out in order" \
        + " to check that the right firmware is loaded and that relevant PCRs (Platform Configuration Registers) in the TPM have" \
        + " the correct values (no changes made since last update). The Trustzone write xor execute functionality makes it harder" \
        + " to inject code. Lastly, here as well the assumption that background checks are carried out on personnel will in part" \
        + " mitigate this threat."),
        ("t.persistent", "o.pwr_out o.two_way_prot", "The two-way protection makes it difficult to intercept SRTP communications."),
        ("t.lost_asset", "o.no_tamper o.enc_data o.secure_comms", "The tamper detection will detect if camera is removed from wall and/or"\
        + " opened. The secure communications objective means user and video data are hard to steal. If an attacker removes flash"\
        + " memory the user data and video stored there are encrypted."),
        ("t.mng_test", "o.trustzone_nx o.decomm", ""),
        ("t.signed_fw", "o.tpm_key_strg o.trustzone_nx o.decomm o.no_tamper o.id", ""),
        ("t.srtp_recv", "o.decomm o.no_tamper o.pwr_out", "Security in real time? Sign me up!"),
        ("t.flash_intg", "o.trustzone_nx o.enc_data o.id", ""),
        ("t.jtag_abuse", "o.tpm_key_strg o.secure_comms", "Oh, so KGB?"),
       ]

row_format = "{} & \\parbox{{4.0cm}}{{\\vspace{{3.5pt}} {} }} &\\parbox{{6cm}}{{\\vspace{{3.0pt}} {} }} \\\\"
content = []
for obj, mitigated, rationale in table:
    content.append(row_format.format(obj.upper().replace('_','\\_'),
        mitigated.upper().replace('_','\\_'), ' '.join([r.strip() for r in
            rationale.split()])))
    content.append("\\hline")

with open(os.path.join('input','rationale.tex'), 'w') as fp:
   fp.write('\n'.join(content)+'\n')
