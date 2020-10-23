sequence = "GGGGGGGGC"
a_amt = 0
t_amt = 0
g_amt = 0
c_amt = 0
invalid = False
for i in range(0, len(sequence)):
    if sequence[i] == "A":
        a_amt += 1
    elif sequence[i] == "T":
        t_amt += 1
    elif sequence[i] == "G":
        g_amt += 1
    elif sequence[i] == "C":
        c_amt += 1
    else:
        invalid = True
        print("invalid")
        break
if not invalid :
    print(a_amt, c_amt, g_amt, t_amt)
