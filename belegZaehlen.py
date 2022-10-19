

def count(liste, lstDbl):
    for el in liste:
        if el not in lstDbl:
            x = el
            cnt = 0
            dbl=""
            for ele in liste:
                if ele == x:
                    cnt+=1
                    dbl=ele
                    if ele not in lstDbl:
                        lstDbl.append(ele)
                        print("Belegnummer {} kommt {} mal vor".format(dbl,cnt))
            if cnt > 2:
                print("Belegnummer {} kommt {} mal vor ".format(dbl, cnt))
                




