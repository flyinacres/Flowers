__author__ = 'rfischer'

N, K = raw_input().split()
c =  raw_input().split()
ci = sorted([int(numeric_string) for numeric_string in c], reverse=True)

total = 0
m = 1
friend = 1
for f in ci:
    total += m * f
    #print friend, m, f, total
    friend += 1
    if friend > int(K):
        friend = 1
        m += 1


#print N, K
#print ci
print total