# Diplomacy.py
# contains diplomacy_read(), diplomacy_eval(), diplomacy_print(), and diplomacy_solve()
from io import StringIO
# --------------
# diplomacy_read
# --------------
def diplomacy_read(s):

    r = io.StringIO(s)
    line = r.readline()
    line = line.split()
    lst = []
    
    while line != []:
        lst.append(line)
        line = r.readline()
        line = line.split()
    return lst

# --------------
# diplomacy_eval
# --------------
def diplomacy_eval(lst):

    return

# ---------------
# diplomacy_print
# ---------------
def diplomacy_print(w, lst):
    w = ""
    for i in lst:
        w += (str(i) + " ")
    w += "\n"
    print(w)

# ---------------
# diplomacy_solve
# ---------------
def diplomacy_solve(r, w):

    return
