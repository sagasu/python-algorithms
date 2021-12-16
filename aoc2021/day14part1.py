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

k = {}

for q in lines[2:]:
    x, y = q.split(" -> ")
    k[x] = y

for _ in range(10):
    n = s[0]
    for c in s[1:]:
        n += k[n[-1] + c]
        n += c
    s = n

c = {}

for char in s:
    if char not in c: c[char] = 0
    c[char] += 1

print(max(c.values()) - min(c.values()))