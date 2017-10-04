from random import randint, shuffle
def nar():
    rn = randint(0,1) # major or Minor
    ar = [0,3+rn,7,12,15+rn,19,24,27+rn]
    return(ar)
def step():
    step = randint(0,3)
    return(step)
def step2():
    step = randint(-7,7)
    return(step)
def step3():
    step = randint(1,3)
    return(step)

dim = [-3,0,3,6,9,12,15,18,21,24]
aug = [0,4,8,12,16,20,24]

nums = [0,2,3,5,7,8,10,12,14,15,17]

arp=[]
for i in range(0,5,1):
    st = step() #start note on the arpeggio
    st2 = step2() #start frequency
    st3 = step3() #length of arpeggio
    ar = nar()
    x = [x+st2 for x in ar[st:-st3]]+(list(reversed([x+st2 for x in ar[st:-st3-1]])))+[x+st2 for x in nums[st:-st3]]+(list(reversed([x+st2 for x in nums[st:-st3-1]])))
    shuffle(x)
    arp.extend(x)
    if(randint(0,1)==0):
        arp.extend([x+st2 for x in ar[st:-st3]]+(list(reversed([x+st2 for x in ar[st:-st3-1]]))))
        x= [x+st2 for x in nums[st:-st3]]+(list(reversed([x+st2 for x in nums[st:-st3-1]])))
        if(randint(0,1)==0):
            shuffle(x)
        arp.extend(x)
    st = step()
    st3 = step3()
    if(randint(0,1)==0):
        arp.extend([x+st2 for x in ar[st:-st3]]+(list(reversed([x+st2 for x in ar[st:-st3-1]]))))
    x = ([x+st2 for x in nums[st:-st3]]+[x+st2 for x in nums[st:-st3]])
    shuffle(x)
    if(randint(0,1)==0):
        arp.extend(x)
    if(randint(0,1)==0):
        arp.extend([x+st2 for x in dim[st:-st3]]+(list(reversed([x+st2 for x in dim[st:-st3-1]]))))
        if(randint(0,1)==0):
            st = step()
            st3 = step3()
            arp.extend([x+st2 for x in dim[st:-st3]]+(list(reversed([x+st2 for x in dim[st:-st3-1]]))))
    if(randint(0,1)==0):
        arp.extend([x+st2 for x in aug[st:-st3]]+(list(reversed([x+st2 for x in aug[st:-st3-1]]))))
    arp.extend([x+st2 for x in ar[st:-st3]]+(list(reversed([x+st2 for x in ar[st:-st3-1]]))))
    x = [x+st2 for x in ar[st:-st3]]+(list(reversed([x+st2 for x in ar[st:-st3-1]])))
    if(randint(0,1)==0):
        shuffle(x)    
    arp.extend(x)





#    arp.extend([x+5 for x in ar[step():]])
#    arp.extend([x+6 for x in ar[step():]])
#    arp.extend([x+3 for x in ar[step():]])
#    arp.extend([x-7 for x in ar[step():]])
#shuffle(arp)

# Length
lengl=[]
for i in range(0,len(arp)-2,1):
    ti= 1
  # ti= 0.7 + np.abs(step2())/7
    tii=0
    if(step2()==0):
        ti = 2
        if(step()==0):
            ti =2
    if(i > len(arp)-10):
        tii += .2
    if(i==len(arp)-1-2):
        tii = .6
    lengl.extend([.13*ti+tii])
