import math
alph = 'abcdefghijklmnopqrstuvwxyz'
d = {x:0 for x in alph};
t = int(raw_input())
case = 1

while (t > 0):
    s = raw_input()
    s = s.lower();
    for x in s:
        if x in d: 
            d[x] = d[x] + 1
    w = sorted(d, key = d.get)
    w.reverse()
    sum = 0
    count = 26
    for x in w:
        sum += d[x] * count;
        count -= 1
    print 'Case #' + str(case) + ': ' + str(sum)
    d = {x : 0 for x in alph}
    t -= 1
    case += 1
 
    
