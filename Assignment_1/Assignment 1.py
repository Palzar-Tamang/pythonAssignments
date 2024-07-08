def is_sator_square(tablet):
    L=len(tablet)
    c=0
    for i in range(L):
        for j in range(L):
            if tablet[i][j]==tablet[j][i] and tablet[i][j]==tablet[-1-j][-1-i]:
                pass
                c=c+1
                #print(c)
            else:
                break
    print(c)
    if c==(L*L):
        return True
    else:
        return False

