def ttt_begin():
    from IPython.display import clear_output
    clear_output(wait=True)
    print ('Hello.. Welcome to Tic-Tac-Toe Game ... ')
    p1name= input("Player 1 : Please enter your name : ")
    p2name= input("Player 2 : Please enter your name : ")
    p1key= input("{} : Please enter your key (X or O):".format(p1name))
    while p1key not in ['X','O']:
        print ('Incorrect Selection')
        p1key= input("{} : Please enter your key (X or O):".format(p1name))
    if p1key == 'X':
        p2key = 'O'
    else:
        p2key = 'X'
    print ('Best of Luck {} and {} .. May the best player win'.format(p1name,p2name))
    playerlist=[]
    l1=[p1name,p1key]
    l2=[p2name,p2key]
    playerlist=[l1,l2]
    mydict={p1name:p1key,p2name:p2key}
    pname=p1name
    blist=['9','8','7','6','5','4','3','2','1']
    board(blist)
    switch(playerlist,pname,blist)

def board(bl):
    print ('   {}  |  {}  |  {}'.format(bl[0],bl[1],bl[2]))
    print ('------------------')
    print ('   {}  |  {}  |  {}'.format(bl[3],bl[4],bl[5]))
    print ('------------------')
    print ('   {}  |  {}  |  {}'.format(bl[6],bl[7],bl[8]))

def selection(pkey,pname,bl,playerlist):
    from IPython.display import clear_output
    sel=input ('{} : Your Turn ... Please select your position (1-9):'.format(pname))
    while sel not in bl:
        print('Incorrect Position Selected or Position is already Assigned!!!')
        sel=input ('{} : Your Turn ... Please select your position (1-9):'.format(pname))
    bl[9-int(sel)]=pkey
    clear_output(wait=True)
    board(bl)
    check(bl,pname,pkey,playerlist)

def switch(playerlist,pname,blist):
    if playerlist[0][0] == pname:
        pname=playerlist[1][0]
        pkey=playerlist[1][1]
    else:
        pname=playerlist[0][0]
        pkey=playerlist[0][1]
    selection(pkey,pname,blist,playerlist)

def check(bl,pname,pkey,playerlist):
    if bl[0] == bl[1] == bl[2] == pkey:
        flag=1
    elif bl[3] == bl[4] == bl[5] == pkey:
        flag=1
    elif bl[6] == bl[7] == bl[8] == pkey:
        flag=1
    elif bl[0] == bl[3] == bl[6] == pkey:
        flag=1
    elif bl[1] == bl[4] == bl[7] == pkey:
        flag=1
    elif bl[2] == bl[5] == bl[8] == pkey:
        flag=1
    elif bl[0] == bl[4] == bl[8] == pkey:
        flag=1
    elif bl[2] == bl[4] == bl[6] == pkey:
        flag=1
    else:
        flag=0
    flag1=0
    for i in range(1,10):
        j = (str(i))
        if j in bl:
            flag1=2
            #print(flag)
        else:
            pass
    if flag == 1:
        print('YAY!!! {} ... You have Won'.format(pname))
        again=input("Do you want to play again?(Y/N)")
        while again not in ['Y','N']:
            print('Invalid Selection')
            again=input("Do you want to play again?(Y/N)")
        if again == 'Y':
            ttt_begin()
        else:
            print('Good Bye!!!')
    elif flag1 == 2:
        switch(playerlist,pname,bl)
    else:
        print('Its a Draw!!')
        again=input("Do you want to play again?(Y/N)")
        while again not in ['Y','N']:
            print('Invalid Selection')
            again=input("Do you want to play again?(Y/N)")
        if again == 'Y':
            ttt_begin()
        else:
            print('Good Bye!!!')


ttt_begin()

