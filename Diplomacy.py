# Diplomacy.py
# contains diplomacy_read(), diplomacy_eval(), diplomacy_print(), and diplomacy_solve()
from io import StringIO
# --------------
# diplomacy_read
# --------------
def diplomacy_read(s):

    infile = StringIO(str(s))
    line = infile.readline()
    line = line.split()
    all_armies = []
    
    while line != []:
        all_armies.append(line)
        line = infile.readline()
        line = line.split()
    return all_armies

# --------------
# diplomacy_eval
# --------------
def diplomacy_eval(all_armies):

    # create dictionary of armies and actions
    army_dict = {}
    for army in all_armies:
        army_dict[army[0]] = army[1:]

    # execute actions in order: hold, move, support
    for actions in army_dict.values():
        if actions[1] == "Hold":
            del actions[1]
    for actions in army_dict.values():
        if actions[1] == "Move":
            actions[0] = actions[2]
            del army[1:3]
    for actions in army_dict.values():
        if actions[1] == "Support":
            # fix for list / indexing
            for army in armies:
                if len(army) > 2:
                    supporter = army[1]
                    in_city = 0
                    for army_again in armies:
                        if army[1] == supporter:
                            in_city += 1
                    # if army in supporting city --> cancel support
                    if in_city > 1:
                        del army_again[2:4]    
                    # if not army in supporting city --> continue support
                    else: # if in_city = 1
                        supported = army_again[3]
                        

            
##            #had army_dict[actions[2]]
##            supported = actions[2]
##            #if there is already support 
##            if army_dict.get(supported)[-1].isdigit():
##                army_dict.get(supported)[-1] += 1
##            else:
##                army_dict.get(supported).append(1)
##                
##    army_list = []
##    keylst = army_dict.keys()
##    for key in keylst:
##        lst = []
##        lst.append(key)
##        for actions in army_dict.get(key):
##            lst.append(actions)
        army_list.append(lst)
                
    return

# ---------------
# diplomacy_print
# ---------------
def diplomacy_print(w, result):
    """
    print one armies outcome
    w - a writer
    result - one armies result (either [dead] or their location)
    """
    for i in result:
        if result[i] == result[len(result) - 1]:
            w.write("\n")
        else:
            w.write(i + " ")       

# ---------------
# diplomacy_solve
# ---------------
def diplomacy_solve(r, w):

    # pre-condition / argument validity
    assert r != ""
    
    """
    r a reader
    w a writer
    """
    all_armies = diplomacy_read(r)
    after_war = diplomacy_eval(all_armies)

    # post-condition / return-value validity
    assert after_war != []
    
    for result in after_war:
        diplomacy_print(w, result)



