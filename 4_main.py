(f, l, c) = (open("4_input.txt", "r").readlines() +  ["\n"], [], "")
for ll in f:
    if ll == "\n":
        l.append(c[1:])
        c = ""
    else:
        c += " " + ll[:-1]

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # Ignoring cid

def is_valid(f, v):
    b = True
    b = b and ((f == "byr") <= (v.isdigit() and int(v) >= 1920 and int(v) <= 2002))
    b = b and ((f == "iyr") <= (v.isdigit() and int(v) >= 2010 and int(v) <= 2020))
    b = b and ((f == "eyr") <= (v.isdigit() and int(v) >= 2020 and int(v) <= 2030))
    b = b and ((f == "hgt") <= (v[-2:] in ["cm", "in"]))
    vv = v[:-2]
    b = b and ((f == "hgt" and v[-2:] == "cm") <= (vv.isdigit() and int(vv) >= 150 and int(vv) <= 193))
    b = b and ((f == "hgt" and v[-2:] == "in") <= (vv.isdigit() and int(vv) >= 59 and int(vv) <= 76))
    b = b and ((f == "hcl") <= (len(v) == 7 and v[0] == "#"))
    b = b and ((f == "hcl") <= (all((x.isdigit() or x == "a" or x == "b" or x == "c" or x == "d" or x == "e" or x == "f") for x in v[1:])))
    b = b and ((f == "ecl") <= (v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]))
    b = b and ((f == "pid") <= (len(v) == 9 and v.isdigit()))
    return b

(c1, c2) = (0, 0)
for x in l:
    done = set()
    (b_done, b_valid) = (True, True)
    for xx in x.split(" "):
        xxx = xx.split(":")
        (ff, vv) = (xxx[0], xxx[1])
        done.add(ff)
        b_valid = b_valid and is_valid(ff, vv)
    for ff in required_fields:
        b_done = b_done and ff in done
    c1 += b_done
    c2 += (b_done and b_valid)

print(c1, c2)
