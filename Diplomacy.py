# Diplomacy.py
# contains diplomacy_eval(), diplomacy_print(), and diplomacy_solve()

from io import StringIO

# helper functions to kill armies in eval()
def killArmies(locationDict, location, army_indices):

    # creates variable to find the index of the max value later on
    maximum = ["", -1]
    values = locationDict.get(location)

    for val in values:
        if val[1] > maximum[1]:
            maximum = [val[0],val[1]]

    # start to kill armies by assigning them a value of -1 if they are dead
    for val in values:
        # if current max army has more support, opponent army dies
        if maximum[1] > val[1]:
            val[1] = -1
        # if current max army has the same support as opponent AND they are not the same army, both armies die
        if (maximum[1] == val[1]) and (maximum[0] != val[0]):
            val[1] = -1
            # returns the index of the current max army in the values and kills them too
            index = [i for i, lst in enumerate(values) if maximum[0] in lst][0]
            values[index][1] = -1
    return values

# helper function to change support values of (-1) to "[dead]" in eval()
def convertDead(locationDict):
    for location in locationDict.keys():
        values = locationDict.get(location)
        for val in values:
            if val[1] == -1:
                val[1] = "[dead]"
    return locationDict
                
# --------------
# diplomacy_eval
# --------------
def diplomacy_eval(all_armies):

    # create dictionary of armies and corresponding indices
    army_indices = {}
    index = 0
    for army in all_armies:
        army_indices[army[0]] = index
        index += 1
    # execute actions in order: hold, move, support
    # hold action
    for army in all_armies:
        if army[2] == "Hold":
            del army[2]
            
    # move action
    for army in all_armies:
        try:
            if (army[2] == "Move"):
                army[1] = army[3]
                del army[2:4]
        except IndexError:
            continue
            
    # support action
    for army in all_armies:
        try:
            if (army[2] == "Support"):
                supporter = army[1]
                in_city = 0
                for army_again in all_armies:
                    if army_again[1] == supporter:
                        in_city += 1

                # if army in supporting city --> cancel support
                if in_city > 1:
                    del army[2:4]    
                # if not army in supporting city --> continue support
                else: # if in_city = 1
                    supported = army[3] # supported = actions[2]
                    index = army_indices.get(supported)
                    # if there is already support 
                    if (all_armies[index][-1]).isdigit(): 
                        (all_armies[index][-1]) += 1
                        del army[2:4]
                    # if no prior support
                    else:
                        all_armies[index].append(1)
                        del army[2:4]
        except IndexError:
            continue

    # WAR

    # group armies by location
    locationDict = {}
    for army in all_armies:
        if army[1] not in locationDict:
            if len(army) > 2:
                locationDict[army[1]] = [[army[0], army[2]]]
            else:
                locationDict[army[1]] = [[army[0], 0]]
        else: # if in locationDict
            val = locationDict.get(army[1])
            if len(army) > 2:
                val.append([army[0], army[2]])
            else:
                val.append([army[0], 0])
            locationDict[army[1]] = val

    # kill appropriate armies at each location
    for location in locationDict.keys():
        after_war = killArmies(locationDict, location, army_indices)
        locationDict[location] = after_war

    # convert -1 in locationDict to "[dead]"
    after_war_dict = convertDead(locationDict)
    return after_war_dict
    
# ---------------
# diplomacy_print
# ---------------
def diplomacy_print(w, result):
    """
    print one armies outcome
    w - a writer
    result - a sorted dictionary of locations and the armies results (either [dead] or their support)
    """

    result_lst = []
    for key in result.keys():
        try:
            values = result.get(key)
            for val in values:
                if val[1] == "[dead]":
                    result_lst.append(val[0] + " " + val[1])
                else:
                    result_lst.append(val[0] + " " + key)
        except IndexError:
            result_lst.append(val[0] + " " + key)

    for i in result_lst:
        w.write(i + "\n")
    
# ---------------
# diplomacy_solve
# ---------------
def diplomacy_solve(r, w):
    """
    r a reader
    w a writer
    """

    # pre-condition / argument validity
    assert r != ""

    # read-ish
    all_armies = []
    for i in r:
        i = i.split()
        all_armies.append(i)

    # eval
    after_war = diplomacy_eval(all_armies)

    # post-condition / return-value validity
    assert after_war != {}
    diplomacy_print(w, after_war)
