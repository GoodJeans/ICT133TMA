def getGroups(value, groups):
    if(value <= groups[0]):
        return 0
    elif(value>groups[0] and value <= groups[1]):
        return 1
    elif(value>groups[1] and value <=groups[2]): 
        return 2
    elif(value>groups[2] and value <=groups[3]): 
        return 3
    elif(value>groups[3] and value <=groups[4]): 
        return 4
    elif(value>groups[4] and value <= groups[5]): 
        return 5
    else:
        return 6

def getDistributions2b(age, totalContribution):
    cpfValue = [    #partially completed for demo
                    #rates group
       (0.6217, 0.1621, 0.2162),  #age<=35
       (0.5677, 0.1891, 0.2432),  #age<=45
       (0.5136, 0.2162, 0.2702),  #age<=50
       (0.4055, 0.3108, 0.2837),  #age<=55
       (0.4616, 0.1346, 0.4038),  #age<=60
       (0.2122, 0.1515, 0.6363),  #age<=65
       (0.08, 0.08, 0.84)        #age>65
    ]
    groups = (35, 45, 50, 55, 60, 65)
    value = getGroups(age, groups)
    if(value == 0):   #calculate oa,sa,ma if age is less than or equals 35
        print("Ordinary Account ratio of contribution is:0.6217")
        print("Special Account ratio of contribution is:0.1621")
        print("MediSave Account ratio of contribution is:0.2162")
        oa = round(totalContribution*cpfValue[0][0],2)
        sa = round(totalContribution*cpfValue[0][1],2)
        ma = round(totalContribution*cpfValue[0][2],2)
        print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma))
    elif(value == 1):   #calculate oa,sa,ma if age is between 35 and 45
        print("Ordinary Account ratio of contribution is:0.5677")
        print("Special Account ratio of contribution is:0.1891")
        print("MediSave Account ratio of contribution is:0.2432")
        oa = round(totalContribution*cpfValue[1][0],2)
        sa = round(totalContribution*cpfValue[1][1],2)
        ma = round(totalContribution*cpfValue[1][2],2) 
        print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma ))
    elif(value == 2 ):  #calculate oa,sa,ma if age is between 45 and 50
        print("Ordinary Account ratio of contribution is:0.5136")
        print("Special Account ratio of contribution is:0.2162")
        print("MediSave Account ratio of contribution is:0.2702")
        oa = round(totalContribution*cpfValue[2][0],2)
        sa = round(totalContribution*cpfValue[2][1],2)
        ma = round(totalContribution*cpfValue[2][2],2)
        print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma))
    elif(value == 3):   #calculate oa,sa,ma if age is between 50 and 55
        print("Ordinary Account ratio of contribution is:0.4055")
        print("Special Account ratio of contribution is:0.3108")
        print("MediSave Account ratio of contribution is:0.2837")
        oa = round(totalContribution*cpfValue[3][0],2)
        sa = round(totalContribution*cpfValue[3][1],2)
        ma = round(totalContribution*cpfValue[3][2],2)
        print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma ))
    elif(value == 4):       #calculate oa,sa,ma if age is between 55 and 60
        print("Ordinary Account ratio of contribution is:0.4616")
        print("Special Account ratio of contribution is:0.1346")
        print("MediSave Account ratio of contribution is:0.4038")
        oa = round(totalContribution*cpfValue[4][0],2)
        sa = round(totalContribution*cpfValue[4][1],2)
        ma = round(totalContribution*cpfValue[4][2],2)
        print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma ))
    elif(value ==5 ):   #calculate oa,sa,ma if age is between 60 and 65
        print("Ordinary Account ratio of contribution is:0.2122")
        print("Special Account ratio of contribution is:0.1515")
        print("MediSave Account ratio of contribution is:0.6363")
        oa = round(totalContribution*cpfValue[5][0],2)
        sa = round(totalContribution*cpfValue[5][1],2)
        ma = round(totalContribution*cpfValue[5][2],2)
        print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma ))
    elif(value == 6 ):  #calculate oa,sa,ma if age is above 65
        print("Ordinary Account ratio of contribution is:0.08")
        print("Special Account ratio of contribution is:0.08")
        print("MediSave Account ratio of contribution is:0.84")
        oa = round(totalContribution*cpfValue[6][0],2)
        sa = round(totalContribution*cpfValue[6][1],2)
        ma = round(totalContribution*cpfValue[6][2],2)
        print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma ))

        return oa,sa,ma

        
def main():
    age = int(input("What is employee's age?"))
    totalContribution = float(input("What is your CPF Contributions?"))
    getDistributions2b(age,totalContribution)

    
main()