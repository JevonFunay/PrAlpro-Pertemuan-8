handle1 = open("satu.txt", 'r')
handle2 = open("dua.txt", 'r')
loro = handle2.readlines()
siji = handle1.readlines()

for i in range(0,len(siji)):
    for j in range(0,len(loro)):
        if i==j:
            if siji[i]==loro[j]:
                continue
            else:
                print(siji[i])
                print(loro[j])