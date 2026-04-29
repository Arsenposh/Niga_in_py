s = input()

s = s.replace("ZER", "0")
s = s.replace("ONE", "1")
s = s.replace("TWO", "2")
s = s.replace("THR", "3")
s = s.replace("FOU", "4")
s = s.replace("FIV", "5")
s = s.replace("SIX", "6")
s = s.replace("SEV", "7")
s = s.replace("EIG", "8")
s = s.replace("NIN", "9")

res = str(eval(s))
result = ""

for d in res:
    if d == "0": result += "ZER"
    if d == "1": result += "ONE"
    if d == "2": result += "TWO"
    if d == "3": result += "THR"
    if d == "4": result += "FOU"
    if d == "5": result += "FIV"
    if d == "6": result += "SIX"
    if d == "7": result += "SEV"
    if d == "8": result += "EIG"
    if d == "9": result += "NIN"

print(result)