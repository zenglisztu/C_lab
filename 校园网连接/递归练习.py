
def ts(ls,lt):
    for i in ls:
        if isinstance(i,list):
            ts(i,lt)
        else:
            lt.append(i)
    return(lt)

def hanoi(n,A,B,C):
    if n == 1:
        print(f'{A} -> {C}  {n}' )
    else:
        hanoi(n-1,A,C,B)
        print(f'{A} -> {C}  {n}')
        hanoi(n-1,B,A,C)



if __name__ == '__main__':

    ls = [1,2,[3,4,5,[6,7,[8,9,[10],11,12],13,14],15,[16],17,[18,[19]]],20]
    print(ts(ls,[]))


    hanoi(4,"A",'B','C')