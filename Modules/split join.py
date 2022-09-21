ladies = input().split()  # lets split the input right away
new_ladies = []  # create an empty list we can append later on
for ladie in ladies:  # indexing out ladies list from our split
    if ladie.endswith('s'):  # if any word in list(ladies) ends with 's'
        new_ladies.append(ladie)  # if it endswith("s") append our new_ladies empty list above

print("_".join(new_ladies))  # print our newly joined list(new_ladies) with _