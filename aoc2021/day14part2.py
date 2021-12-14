lines = ["VFHKKOKKCPBONFHNPHPN",
"",
"VS -> B",
"HK -> B",
"FO -> P",
"NC -> F",
"VN -> C",
"BS -> O",
"HS -> K",
"NS -> C",
"CV -> P",
"NV -> C",
"PH -> H",
"PB -> B",
"PK -> K",
"HF -> P",
"FV -> C",
"NN -> H",
"VO -> K",
"VP -> P",
"BC -> B",
"KK -> S",
"OK -> C",
"PN -> H",
"SB -> V",
"KO -> P",
"KH -> C",
"KS -> S",
"FP -> B",
"PV -> B",
"BO -> C",
"OS -> H",
"NB -> S",
"SP -> C",
"HN -> N",
"FN -> B",
"PO -> O",
"FS -> O",
"NH -> B",
"SO -> P",
"OB -> S",
"KC -> C",
"OO -> H",
"BB -> V",
"SC -> F",
"NP -> P",
"SH -> C",
"BH -> O",
"BP -> F",
"CC -> S",
"BN -> H",
"SS -> P",
"BF -> B",
"VK -> P",
"OV -> H",
"FC -> S",
"VB -> S",
"PF -> N",
"HH -> O",
"HC -> V",
"CH -> B",
"HP -> H",
"FF -> H",
"VF -> V",
"CS -> F",
"KP -> F",
"OP -> H",
"KF -> F",
"PP -> V",
"OC -> C",
"PS -> F",
"ON -> H",
"BK -> B",
"HV -> S",
"CO -> K",
"FH -> C",
"FB -> F",
"OF -> V",
"SN -> S",
"PC -> K",
"NF -> F",
"NK -> P",
"NO -> P",
"CP -> P",
"CK -> S",
"HB -> H",
"BV -> C",
"SF -> K",
"HO -> H",
"OH -> B",
"KV -> S",
"KN -> F",
"SK -> K",
"VH -> S",
"CN -> S",
"VC -> P",
"CB -> H",
"SV -> S",
"VV -> P",
"CF -> F",
"FK -> F",
"KB -> V"]
s = lines[0]

pc = {}

for x, y in zip(s, s[1:]):
    if x + y not in pc: pc[x + y] = 0
    pc[x + y] += 1

k = {}

for q in lines[2:]:
    x, y = q.split(" -> ")
    k[x] = y

for _ in range(40):
    npc = {}
    for p in pc:
        q = k[p]
        if p[0] + q not in npc: npc[p[0] + q] = 0
        npc[p[0] + q] += pc[p]
        if q + p[1] not in npc: npc[q + p[1]] = 0
        npc[q + p[1]] += pc[p]
    pc = npc

hc = {}
tc = {}

for p in pc:
    if p[0] not in hc: hc[p[0]] = 0
    if p[1] not in tc: tc[p[1]] = 0
    hc[p[0]] += pc[p]
    tc[p[1]] += pc[p]

c = {x: max(hc.get(x, 0), tc.get(x, 0)) for x in set(hc) | set(tc)}

print(max(c.values()) - min(c.values()))