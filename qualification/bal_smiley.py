
t = int(raw_input())

for i in xrange(1,t+1):
    s = raw_input()
    d = {x : {} for x in xrange(0, len(s))}
    li = 'abcdefghijklmnopqrstuvwxyz : ( )'
    check = {x : 1 for x in li}
    flag = 0
    for y in s:
        if y not in check:
            print "Case #" + str(i) + ": NO"
            flag = -1
            break
    if flag == -1:
        continue        
    if s[0] == ')':
        print "Case #" + str(i) + ": NO"
        continue
    elif s[0] == '(':
        d[0] = {1:1}
    else: d[0] = {0:1}
    if s[1] == '(' or s[1] == ')':
        if s[0] == ':':
            d[1][0] = 1
        if s[1] == '(':
            for y in d[0]:
                d[1][y+1] = 1
        if s[1] == ')':
            for y in d[0]:
                if y-1 > 0:
                    d[1][y-1] = 1
    else : d[1] = d[0]
   
    for x in xrange(2,len(s)):
        if s[x] == '(':
            for y in d[x-1]:
                d[x][y+1] = 1
            if s[x-1] == ':':
                d[x].update(d[x-2])
        elif s[x] == ')':
            for y in d[x-1]:
                if y - 1 >= 0:
                    d[x][y-1] = 1
            if s[x-1] == ':':
                d[x].update(d[x-2])
        else:
            d[x] = d[x-1]

    
    for y in d[len(s)-1]:
        if y >= 0:
            flag = 1
            break
    if (flag == 1):
        print "Case #" + str(i) + ": YES"
    else: print "Case #" + str(i) + ": NO"
        
            

            
        
                           
    
    
            
