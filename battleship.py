while True:

#%%
    # Import packages
    import random
    
    
    #%%
    def set_board(): #initialise a 8x8 board
    
        global com_sur_board  # visual elements for user and computer board are kept in a list variable
        global com_und_board
        global user_sur_board
        global user_und_board
        com_sur_board = []   # visual elements for user and computer board are kept in a list variable
        com_und_board = []
        user_sur_board =[]
        user_und_board =[]
    
        for i in range(1,9):
            com_und_board.append([str(i)," ","   |","   |","   |","   |","   |","   |","   |","   |",])
            com_sur_board.append([str(i)," ","   |","   |","   |","   |","   |","   |","   |","   |",])
            user_sur_board.append([str(i)," ","   |","   |","   |","   |","   |","   |","   |","   |",])
            user_und_board.append([str(i)," ","   |","   |","   |","   |","   |","   |","   |","   |",])    
        
    def computer_board(): #Print our the board using list variables defined.
        print('The computer\'s board looks like this')
        print('   1   2   3   4   5   6   7   8 ')
        print('Surface')        
        for row in com_sur_board:
            print("".join(row))
            print("   -------------------------------")
        print('Underwater')
        for row in com_und_board:
            print("".join(row))
            print("   -------------------------------")
    def user_board():
        print('The user\'s board looks like this')
        print('   1   2   3   4   5   6   7   8 ')
        print('Surface')
        for row in user_sur_board:
            print("".join(row))
            print("   -------------------------------")    
        print('Underwater')
        for row in user_und_board:
            print("".join(row))
            print("   -------------------------------")   
    
    #%%
    
    
    def place_sub(): #place a submarine by user
        
        while True:
            print('Welcome to Battleship+')
            print(f'Placing a/an SUBMARINE')
            print('Please enter coordinates following this format (row,col,depth). E.g. 3,4,1 (row = 3, col = 4, and depth =1).')
            print('Note: depth = 0 represents the subsea layer, and depth = 1 represents the surface level.')
            srow, scol, sdepth = [int(x) for x in input("Enter coordinates: ").split(",")]
            orientation = input('vertical or horientationzontal (v,h)? ')
    
            global sur_sub_coor
            global und_sub_coor
            global s_dep
            s_dep = sdepth
            sur_sub_coor = []
            und_sub_coor = []
    
            
           
            if not srow <9 and scol <9:
                print('Cannot place a ship there. \nPlease take a look at the board and try again.')
                input('Press Enter to continue')
                continue
        
            if orientation =='h':
                if scol<7:
                    if sdepth ==1:
                        for x in range(srow,srow+1):
                            for y in range(scol,(scol+3)):
                                user_sur_board[x-1][y+1] = ' S |'
                                sur_sub_coor.append([x,y])
                    if sdepth ==0:
                        for x in range(srow,srow+1):
                            for y in range(scol,(scol+3)):
                                user_und_board[x-1][y+1] = ' S |'
                                sur_sub_coor.append([x,y])
                else: 
                    print('Cannot place a ship there. \nPlease take a look at the board and try again.')
                    input('Press Enter to continue')
                    continue

            if orientation == 'v':
                if srow<7:
                    if sdepth == 1:
                        for x in range(srow,srow+3):
                            for y in range(scol,scol+1):
                                user_sur_board[x-1][y+1] = ' S |'
                                sur_sub_coor.append([x,y])
                    if sdepth == 0:
                        for x in range(srow,srow+3):
                            for y in range(scol,scol+1):
                                user_und_board[x-1][y+1] = ' S |'
                                und_sub_coor.append([x,y])
                else:  
                    print('Cannot place a ship thereee. \nPlease take a look at the board and try again.')
                    input('Press Enter to continue')
                    continue

            break
           
    
        #print(sur_sub_coor) # Do we need to print coodinates here?
        #print(und_sub_coor)
    
    
    # In[7]:
    
    
    def place_des():
    
        while True:
            print(f'Placing a/an Destroyer')
            print('Please enter coordinates following this format (row,col,depth). E.g. 3,4,1 (row = 3, col = 4, and depth =1).\n Note:\
                Destroyer can only be placed at surface level')
            print('Note: depth = 0 represents the subsea layer, and depth = 1 represents the surface level.')
    
            drow, dcol, ddepth = [int(x) for x in input("Enter coordinates: ").split(",")]
            global d_depth
            d_depth=ddepth
            orientation = input('vertical or horientationzontal (v,h)? ')
            global des_coor 
            des_coor = []
            
            if ddepth ==1:
                if drow<7 and dcol<9:
                    if orientation == 'v':
                        for x in range(drow,drow+3):
                            for y in range(dcol,dcol+1):
                                des_coor.append([x,y])
                    else: 
                        print('Cannot place a destroyer there. \nPlease take a look at the board and try again')
                        input('Press Enter to continue')
                        continue
                elif drow<9 and dcol<7:
                    if orientation == 'h':
                        for x in range(drow,drow+1):
                            for y in range(dcol,(dcol+3)):                                
                                des_coor.append([x,y])
                    else: 
                        print('Cannot place a destroyer there. \nPlease take a look at the board and try again')
                        input('Press Enter to continue')
                        continue
            else:
                print('Cannot place a destroyer there. \nPlease take a look at the board and try again')
                input('Press Enter to continue')
                continue
            
            if not (any(x in des_coor for x in sur_sub_coor) == False):
                print('Cannot place a destroyer there. \nPlease take a look at the board and try again. \nHit ENTER to continue')
                continue
            
                                         
            else:
              
                break
        #after checking that the coordinates are valid we print the destroyers on the board
        if orientation == 'h':
            for x in range(drow,drow+1):
                for y in range(dcol,(dcol+3)):    
                    user_sur_board[x-1][y+1] = ' D |'
    
        elif orientation == 'v' :
            for x in range(drow,drow+3):
                for y in range(dcol,dcol+1):    
                    user_sur_board[x-1][y+1] = ' D |'
        user_board()
    
    
    
    # In[11]:
    
    #after user placed the ship, it's computer's turn
    
     
    def com_place_sub():             
        global com_sur_sub_coor
        global com_und_sub_coor
        global cdep
        global cusub

        com_sur_sub_coor = [] #computer surface submarine coordinates
        com_und_sub_coor = [] #computer underwater submarine coordinates
        
        print('Computer is placing a/an submarine')      
        orientation1 = random.choice(['v','h'])    
        if orientation1 == 'h':
            cs_row, cs_col, cs_depth =random.randint(1,8), random.randint(1,6), random.randint(0,1)
            if cs_depth == 1:
                for x in range(cs_row,cs_row+1):
                    for y in range(cs_col,(cs_col+3)):            
                        com_sur_sub_coor.append([x,y])
            elif cs_depth == 0:
                for x in range(cs_row,cs_row+1):
                    for y in range(cs_col,(cs_col+3)):
                        com_und_sub_coor.append([x,y])
        elif orientation1 == 'v':
            cs_row, cs_col, cs_depth =random.randint(1,6), random.randint(1,8), random.randint(0,1)
            if cs_depth == 1:
                for x in range(cs_row,cs_row+3):
                    for y in range(cs_col,cs_col+1):                            
                        com_sur_sub_coor.append([x,y])
            elif cs_depth == 0:
                for x in range(cs_row,cs_row+3):
                    for y in range(cs_col,cs_col+1):            
                        com_und_sub_coor.append([x,y])
        print(com_und_sub_coor)
        cusub = com_und_sub_coor
        print(com_sur_sub_coor)
        print(cs_row, cs_col, cs_depth,orientation1)
           
        cdep = cs_depth    
   
    # In[12]:
    
    def com_place_des(): #place the destroyer for computer
        while True:
            print('Computer is placing a/an destroyer')                    
            global cddepth1
            cddepth1=cd_depth # can't do it here without value of cd_depth defined
            global com_des_coor
            com_des_coor = []
            
            orientation2 = random.choice(['v','h'])
            if orientation2 == 'h':
                cs_row, cs_col, cs_depth =random.randint(1,8), random.randint(1,6), 1 #can only place destroyer on the surface
                for x in range(cd_row,cd_row+1):
                    for y in range(cd_col,(cd_col+3)):
                        com_des_coor.append([x,y])    
                        
            if orientation2 == 'v' :
                cs_row, cs_col, cs_depth =random.randint(1,6), random.randint(1,8), 1 #can only place destroyer on the surface
                for x in range(cd_row,cd_row+3):
                    for y in range(cd_col,cd_col+1):
                        com_des_coor.append([x,y])
            print(com_des_coor)
            print(cd_row, cd_col, cd_depth,orientation2)
            
               
            
            if not (any(x in com_des_coor for x in com_sur_sub_coor) == False):
                print("overlapping ship")
                com_des_coor.clear()
               
                continue
            
                                         
            else:  #?????? Use pass?
            #we're happy with the value given.
            #we're ready to exit the loop.
            
                
                break
                
        
        print('Game Start!!!')           
        
        
    
    
    
    # In[ ]:
    
    #hit coordinates
    
    def hit():

        computer_board() # Print User's board
        
        print('Please enter coordinates following this format (row,col,depth). E.g. 3,4,1 (row = 3, col = 4, and depth =1).')
        print('Note: depth = 0 represents the subsea layer, and depth = 1 represents the surface level.')
        hrow, hcol, hdepth = [int(x) for x in input("Enter coordinates: ").split(",")]
        global sur_hit_coor
        global und_hit_coor
        global hdep
        global hrow1
        global hcol1
        global com_sur_board
        global com_und_board
        hrow1=hrow
        hcol1=hcol
        
        hdep = hdepth
        sur_hit_coor = [] #surface ships hith
        und_hit_coor = [] #und ships hit
        if hdepth == 1:
            if hrow ==1:
                if hcol == 1: #corner
                    for x in range(0, 2):
                        for y in range(2,4):
                            com_sur_board[x][y] = ' * |'
                            sur_hit_coor.append([x+1,y-1])
                        
                elif hcol == 8: #corner
                    for x in range(0,2):
                        for y in range(8,10): 
                            com_sur_board[x][y] = ' * |'
                            sur_hit_coor.append([x+1,y-1])
                elif hcol in range(2,8): #on the upper row edges but not corner
                    for x in range(hrow - 1, hrow +1 ):
                        for y in range(hcol, hcol+3):
                            com_sur_board[x][y] = ' * |'
                            sur_hit_coor.append([x+1,y-1])
                
            elif hrow == 8:
                if hcol == 1: #corner
                    for x in range(6,8):
                        for y in range(2,4):
                            com_sur_board[x][y] = ' * |'
                            sur_hit_coor.append([x+1,y-1])    
                elif hcol == 8: #corner
                    for x in range(6,8):
                        for y in range(8,10):
                            com_sur_board[x][y] = ' * |'
                            sur_hit_coor.append([x+1,y-1])
                elif hcol in range(2,8)): #on the lower row edges but not corner
                    for x in range(hrow -2, hrow):
                        for y in range(hcol, hcol+3):
                            com_sur_board[x][y] = ' * |'
                            sur_hit_coor.append([x+1,y-1])
            
            elif (hcol == 1) and (hrow in range(2,8)): #on the left column edges but not corner
                for x in range(hrow-2, hrow+1):
                    for y in range(2,4):
                        com_sur_board[x][y] = ' * |'
                        sur_hit_coor.append([x+1,y-1])
            elif (hcol == 8) and (hrow in range(2,8)): #on the right col edges but not corner
                for x in range(hrow-2, hrow+1):
                    for y in range(8,10):
                        com_sur_board[x][y] = ' * |'
                        sur_hit_coor.append([x+1,y-1])
            else:
                for x in range(hrow -2, hrow+1): #other normal ones
                    for y in range(hcol, hcol+3):
                        com_sur_board[x][y] = ' * |'
                        sur_hit_coor.append([x+1,y-1])
        if hdepth == 0:
            if hrow ==1:
                if hcol == 1: #corner
                    for x in range(0, 2):
                        for y in range(2,4):
                            com_und_board[x][y] = ' * |'
                            und_hit_coor.append([x+1,y-1])
                        
                elif hcol == 8: #corner
                    for x in range(0,2):
                        for y in range(8,10):
                            com_und_board[x][y] = ' * |'
                            und_hit_coor.append([x+1,y-1])
                elif hcol in range(2,8)): # upper edge
                    for x in range(hrow - 1, hrow +1 ):
                        for y in range(hcol, hcol+3):
                            com_sur_board[x][y] = ' * |'
                            sur_hit_coor.append([x+1,y-1])
            elif hrow == 8:
                if hcol == 1: #corner
                    for x in range(6,8):
                        for y in range(2,4):
                            com_und_board[x][y] = ' * |'
                            und_hit_coor.append([x+1,y-1])    
                elif hcol == 8: #corner
                    for x in range(6,8):
                        for y in range(8,10):
                            com_und_board[x][y] = ' * |'
                            und_hit_coor.append([x+1,y-1])           
                elif hcol in range(2,8)): #lower edge
                    for x in range(hrow -2, hrow):
                        for y in range(hcol, hcol+3):
                            com_und_board[x][y] = ' * |'
                            und_hit_coor.append([x+1,y-1])
            elif (hcol == 1) and (hrow in range(1,7)): #left edge
                for x in range(hrow-2, hrow+1):
                    for y in range(2,4):
                        com_und_board[x][y] = ' * |'
                        und_hit_coor.append([x+1,y-1])
            elif (hcol == 8) and (hrow in range(1,7)): #right edge
                for x in range(hrow-2, hrow+1):
                    for y in range(8,10):
                        com_und_board[x][y] = ' * |'
                        und_hit_coor.append([x+1,y-1])
            else:
                for x in range(hrow-2, hrow+1): #normal
                    for y in range(hcol, hcol+3):
                        com_und_board[x][y] = ' * |'
                        und_hit_coor.append([x+1,y-1])
    
    
    
    
    #%%    
    def after_hit():
        if cdep == hdep == 1 :#both submarine and destroyer as well as hit level of the surface
            
            for i in range(len(com_sur_sub_coor)):
                
               if  (com_sur_sub_coor[i][0]>= hrow1-1 and com_sur_sub_coor[i][0]<= hrow1+1) and (  com_sur_sub_coor[i][1]>= hcol1-1 and com_sur_sub_coor[i][1]<= hcol1+1 ):
                       m=com_sur_sub_coor[i][0]-1
                       n=com_sur_sub_coor[i][1]+1
                       com_sur_board[m][n] = ' $ |'
               if  (com_des_coor[i][0]>= hrow1-1 and com_des_coor[i][0]<= hrow1+1) and (  com_des_coor[i][1]>= hcol1-1 and com_des_coor[i][1]<= hcol1+1 ):
                       m=com_des_coor[i][0]-1
                       n=com_des_coor[i][1]+1
                       com_sur_board[m][n] = ' $ |'
        
        elif cdep == hdep == 0 :#submarine underwtaer
        
               for i in range(len(cusub)):
                
                   if(cusub[i][0]>= hrow1-1 and cusub[i][0]<= hrow1+1) and (  cusub[i][1]>= hcol1-1 and cusub[i][1]<= hcol1+1 ):
                       m=cusub[i][0]-1
                       n=cusub[i][1]+1
                       com_und_board[m][n] = ' $ |'
        
        elif cddepth1 == hdep ==1 :#submarine underwater and destroyer at the surface
               for i in range(len(com_des_coor)):
                    if  (com_des_coor[i][0]>= hrow1-1 and com_des_coor[i][0]<= hrow1+1) and (  com_des_coor[i][1]>= hcol1-1 and com_des_coor[i][1]<= hcol1+1 ):
                       m=com_des_coor[i][0]-1
                       n=com_des_coor[i][1]+1
                       com_sur_board[m][n] = ' $ |'
        
        
        
        elif (cdep ==0 and hdep == 1) or (cdep == 1 and hdep == 0 ):
               print(" Sorry! The attack centering area" ,hrow1,hcol1,hdep, "was a total miss" )

        computer_board()
       
    
    #%%
    def com_hit():
       
        c_hrow, c_hcol, c_hdepth = 3,4,1  #?????
        global com_sur_hit_coor
        global com_und_hit_coor
        global chdep #used later
        global chrow1#used later
        global chcol1#used later
        chrow1=c_hrow
        chcol1=c_hcol
        
        chdep = c_hdepth
        com_sur_hit_coor = []
        com_und_hit_coor = []
        if c_hdepth == 1:
            if c_hrow ==1 and c_hcol == 1: #corner
                for x in range(0, 2):
                    for y in range(2,4):
                        user_sur_board[x][y] = ' * |'
                        com_sur_hit_coor.append([x+1,y-1])
                        
            elif c_hrow == 1 and c_hcol == 8: #corner
                for x in range(0,2):
                    for y in range(8,10): 
                        user_sur_board[x][y] = ' * |'
                        com_sur_hit_coor.append([x+1,y-1])
            elif c_hrow == 8 and c_hcol == 1: #corner
                for x in range(6,8):
                    for y in range(2,4):
                        user_sur_board[x][y] = ' * |'
                        com_sur_hit_coor.append([x+1,y-1])    
            elif c_hrow == 8 and c_hcol == 8: #corner
                for x in range(6,8):
                    for y in range(8,10):
                        user_sur_board[x][y] = ' * |'
                        com_sur_hit_coor.append([x+1,y-1])
            elif (c_hrow == 8) and (c_hcol in range(2,7)):
                for x in range(c_hrow -2, c_hrow):
                    for y in range(c_hcol, c_hcol+3):
                        user_sur_board[x][y] = ' * |'
                        com_sur_hit_coor.append([x+1,y-1])
            elif (c_hrow ==1) and (c_hcol in range(2,7)):
                for x in range(c_hrow - 1, c_hrow +1 ):
                    for y in range(c_hcol, c_hcol+3):
                        user_sur_board[x][y] = ' * |'
                        com_sur_hit_coor.append([x+1,y-1])
            elif (c_hcol == 1) and (c_hrow in range(1,7)):
                for x in range(c_hrow-2,c_hrow+1):
                    for y in range(2,4):
                        user_sur_board[x][y] = ' * |'
                        com_sur_hit_coor.append([x+1,y-1])
            elif (c_hcol == 8) and (c_hrow in range(1,7)):
                for x in range(c_hrow-2, c_hrow+1):
                    for y in range(8,10):
                        user_sur_board[x][y] = ' * |'
                        com_sur_hit_coor.append([x+1,y-1])
            else:
                for x in range(c_hrow -2, c_hrow+1):
                    for y in range(c_hcol, c_hcol+3):
                        user_sur_board[x][y] = ' * |'
                        com_sur_hit_coor.append([x+1,y-1])
        if c_hdepth == 0:
            if c_hrow ==1 and c_hcol == 1:
                for x in range(0, 2):
                    for y in range(2,4):
                        user_und_board[x][y] = ' * |'
                        com_und_hit_coor.append([x+1,y-1])
                        
            elif c_hrow == 1 and c_hcol == 8:
                for x in range(0,2):
                    for y in range(8,10):
                        user_und_board[x][y] = ' * |'
                        com_und_hit_coor.append([x+1,y-1])
            elif c_hrow == 8 and c_hcol == 1:
                for x in range(6,8):
                    for y in range(2,4):
                        user_und_board[x][y] = ' * |'
                        com_und_hit_coor.append([x+1,y-1])    
            elif c_hrow == 8 and c_hcol == 8:
                for x in range(6,8):
                    for y in range(8,10):
                        user_und_board[x][y] = ' * |'
                        com_und_hit_coor.append([x+1,y-1])
            elif (c_hrow ==1) and (c_hcol in range(2,7)):
                for x in range(hrow - 1, hrow +1 ):
                    for y in range(hcol, hcol+3):
                        user_sur_board[x][y] = ' * |'
                        com_sur_hit_coor.append([x+1,y-1])
            elif (c_hrow == 8) and (c_hcol in range(2,7)):
                for x in range(c_hrow -2, c_hrow):
                    for y in range(c_hcol, c_hcol+3):
                        user_und_board[x][y] = ' * |'
                        s_und_hit_coor.append([x+1,y-1])
            elif (c_hcol == 1) and (c_hrow in range(1,7)):
                for x in range(c_hrow-2, c_hrow+1):
                    for y in range(2,4):
                        user_und_board[x][y] = ' * |'
                        com_und_hit_coor.append([x+1,y-1])
            elif (c_hcol == 8) and (c_hrow in range(1,7)):
                for x in range(c_hrow-2, c_hrow+1):
                    for y in range(8,10):
                        user_und_board[x][y] = ' * |'
                        com_und_hit_coor.append([x+1,y-1])
            else:
                for x in range(c_hrow-2, c_hrow+1):
                    for y in range(c_hcol, c_hcol+3):
                        user_und_board[x][y] = ' * |'
                        com_und_hit_coor.append([x+1,y-1])
    
    #%%
    def com_after_hit():
        if s_dep == chdep == 1 :#both submarine and destroyer as well as hit level o the surface
        
            
            for i in range(len(sur_sub_coor)):
                
               if  (sur_sub_coor[i][0]>= chrow1-1 and sur_sub_coor[i][0]<= chrow1+1) and (  sur_sub_coor[i][1]>= chcol1-1 and sur_sub_coor[i][1]<= chcol1+1 ):
                       m=sur_sub_coor[i][0]-1
                       n=sur_sub_coor[i][1]+1
                       
                       user_sur_board[m][n] = ' $ |'
               if  (des_coor[i][0]>= chrow1-1 and des_coor[i][0]<= chrow1+1) and (  des_coor[i][1]>= chcol1-1 and des_coor[i][1]<= chcol1+1 ):
                       m=[i][0]-1
                       n=des_coor[i][1]+1
                       
                       user_sur_board[m][n] = ' $ |'
        
        elif s_dep == chdep == 0 :#submarine underwtaer
           
               for i in range(len(und_sub_coor)):
                
                   if(und_sub_coor[i][0]>= chrow1-1 and und_sub_coor[i][0]<= chrow1+1) and (  und_sub_coor[i][1]>= chcol1-1 and und_sub_coor[i][1]<= chcol1+1 ):
                       m=und_sub_coor[i][0]-1
                       n=und_sub_coor[i][1]+1
                       
                       user_und_board[m][n] = ' $ |'
        
        elif   d_depth == chdep ==  1 :#submarine underwater and destroyer at the surface
               for i in range(len(des_coor)):
                    if  (des_coor[i][0]>= chrow1-1 and des_coor[i][0]<= chrow1+1) and (  des_coor[i][1]>= chcol1-1 and des_coor[i][1]<= chcol1+1 ):
                       m=des_coor[i][0]-1
                       n=des_coor[i][1]+1
                    
                       user_sur_board[m][n] = ' $ |'
        
        elif (cdep ==0 and s_dep == 1) or (cdep == 1 and s_dep == 0 ):
               print(" Sorry! The attack centering area" ,hrow1,hcol1,hdep, "was a total miss" )

    

    #%% 
        
    def update_coor(vessel_coor, hit_coor):
        vessel_coor_updated = vessel_coor
        for i in vessel_coor:
            if i in hit_coor:
                vessel_coor_updated.remove(i)
        return vessel_coor_updated

#%%    
    # Run the whole program
    set_board()
    computer_board()
    user_board()
    place_sub()
    place_des()
    com_place_sub()
    com_place_des()
    
    new_sur_sub_coor = sur_sub_coor
    new_und_sub_coor = und_sub_coor
    new_des_coor = des_coor
    new_com_sur_sub_coor = com_sur_sub_coor
    new_com_und_sub_coor = com_und_sub_coor
    new_com_des_coor = com_des_coor
#%%   
    # Attack and summary
    user_sub_sunk = 0
    user_des_sunk = 0
    com_sub_sunk = 0
    com_sub_sunk = 0
    
    
    while True:
        # User attack
        hit()
        after_hit()
        #Update computer vessels' coordinates
        new_com_sur_sub_coor = update_coor(new_com_sur_sub_coor,sur_hit_coor)
        new_com_und_sub_coor = update_coor(new_com_und_sub_coor,und_hit_coor)
        new_com_des_coor = update_coor(new_com_des_coor,sur_hit_coor)
        # Calculate result for computer
        if new_com_sur_sub_coor == [] and new_com_und_sub_coor ==[] and com_sub_sunk == 0:
            print('Computer\'s submarine sunk.')
            user_sub_sunk = 1
        if new_com_des_coor == [] and com_des_sunk == 0:
            print('Computer\'s destroyer sunk.')
            user_des_sunk = 1
        if com_sub_sunk == 1 and com_des_sunk == 1:
            print('User won! :)')
            break
        
        # Computer attack
        com_hit()
        com_after_hit()
        # Update user vessels' coordinates
        new_sur_sub_coor = update_coor(new_sur_sub_coor,com_sur_hit_coor)
        new_und_sub_coor = update_coor(new_und_sub_coor,com_und_hit_coor)
        new_des_coor = update_coor(new_des_coor,com_sur_hit_coor)
        # Calculate result for user
        if new_sur_sub_coor == [] and new_und_sub_coor ==[] and user_sub_sunk == 0:
            print('User\'s submarine sunk.')
            user_sub_sunk = 1
        if new_des_coor == [] and user_des_sunk == 0:
            print('User\'s destroyer sunk.')
            user_des_sunk = 1
        if user_sub_sunk == 1 and user_des_sunk == 1:
            print('Computer won! :)')
            break
        

#%%    
# Choose to rerun the program
    while True:    
        game = input('Do you want to play again? Enter Y for yes or N for no:')
        if game in ('Y','N'):
            break
        else: 
            print('Sorry, I don\'t understand your instructions.\n')
            continue
        
    if game == 'Y':
        continue
    else:
        print('Goodbye!')
        break

            
        
        
     #%%
     #code for check coordinates
    
            ## Don't delete ##
    
    # 1 user vessels
    print('\n','user vessels')
    print('sur_sub_coor: ',sur_sub_coor)
    print('und_sub_coor: ',und_sub_coor)
    print('des_coor: ',des_coor,'\n') 
    
    # 2 
    print('computer vessels')
    print('com_sur_sub_coor: ',com_sur_sub_coor)
    print('com_und_sub_coor: ',com_und_sub_coor)
    print('com_des_coor: ',com_des_coor,'\n') 
    
    # 3
    print('user hit coordinates')
    print('sur_hit_coor: ',sur_hit_coor)
    print('und_hit_coor: ',und_hit_coor,'\n')
    
    # 4
    print('computer hit coordinates')
    print('com_sur_hit_coor: ',com_sur_hit_coor)
    print('com_und_hit_coor: ',com_und_hit_coor,'\n')
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
