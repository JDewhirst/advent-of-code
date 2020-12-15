
if __name__=="__main__":
    # input data
    t = [19,20,14,0,9,1]
    
    # Dictionary {num:turn} where turn is the last turn that num was said
    nt = dict([(y,x+1) for (x,y) in enumerate(t[:len(t)-1])])
    
    # the last thing said, not yet in dict
    last = t[-1]
    
    for turn in range(len(t),30000000):
        if last in nt:
            # last was previously said at turn nt[last]
            nxt = turn - nt[last]
            nt[last] = turn
            last = nxt
        else:
            nt[last] = turn
            last = 0
        # Reassure the human that I am doing something (or comment out if not needed)
        if turn % 1000000 == 0:
            print('.',end='',flush=True)
            
    print(last)