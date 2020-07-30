def getDistributions2a(age, totalContribution):
        if(age<=35):    #calculate oa, sa ma if age is below or equals to 35
            print("Ordinary Account ratio of contribution is:0.6217")
            print("Special Account ratio of contribution is:0.1621")
            print("MediSave Account ratio of contribution is:0.2162")
            oa = round(totalContribution*0.6217,2)
            sa = round(totalContribution*0.1621,2)
            ma = round(totalContribution*0.2162,2)
            print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma))
        elif(age>35 and age<=45):   #calculate oa,sa,ma if age is more than 35 and less than or equals to 45
            print("Ordinary Account ratio of contribution is:0.5677")
            print("Special Account ratio of contribution is:0.1891")
            print("MediSave Account ratio of contribution is:0.2432")
            oa = round(totalContribution*0.5677,2)
            sa = round(totalContribution*0.1891,2)
            ma = round(totalContribution*0.2432,2) 
            print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma ))
        elif(age>45 and age<=50):   #calculate oa,sa,ma if age is more than 45  and less than or equals to 50 
            print("Ordinary Account ratio of contribution is:0.5136")
            print("Special Account ratio of contribution is:0.2162")
            print("MediSave Account ratio of contribution is:0.2702")
            oa = round(totalContribution*0.5136,2)
            sa = round(totalContribution*0.2162,2)
            ma = round(totalContribution*0.2702,2)
            print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma))
        elif(age>50 and age<=55):   #calculate oa,sa,ma if age is more than 50 and less than or equals to 55
            print("Ordinary Account ratio of contribution is:0.4055")
            print("Special Account ratio of contribution is:0.3108")
            print("MediSave Account ratio of contribution is:0.2837")
            oa = round(totalContribution*0.4055,2)
            sa = round(totalContribution*0.3108,2)
            ma = round(totalContribution*0.2837,2)
            print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma ))
        elif(age>55 and age<=60):       #calculate oa,sa,ma if age is more than 55 and less than or equals to 60
            print("Ordinary Account ratio of contribution is:0.4616")
            print("Special Account ratio of contribution is:0.1346")
            print("MediSave Account ratio of contribution is:0.4038")
            oa = round(totalContribution*0.4616,2)
            sa = round(totalContribution*0.1346,2)
            ma = round(totalContribution*0.4038,2)
            print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma ))
        elif(age>60 and age<=65):       #calculate oa,sa,ma if age is more than 60  and less than or equals to 65
            print("Ordinary Account ratio of contribution is:0.2122")
            print("Special Account ratio of contribution is:0.1515")
            print("MediSave Account ratio of contribution is:0.6363")
            oa = round(totalContribution*0.2122,2)
            sa = round(totalContribution*0.1515,2)
            ma = round(totalContribution*0.6363,2)
            print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma ))
        elif(age>65):           #calculate oa,sa,ma if age is more than 65
            print("Ordinary Account ratio of contribution is:0.08")
            print("Special Account ratio of contribution is:0.08")
            print("MediSave Account ratio of contribution is:0.84")
            oa = round(totalContribution*0.08,2)
            sa = round(totalContribution*0.08,2)
            ma = round(totalContribution*0.84,2)
            print("OA contribution is:\t ${}\nSA contribution is:\t ${}\nMA contribution is:\t ${}".format(oa, sa, ma ))
     
        return oa,sa,ma

def main():
    age = int(input("What is employee's age?"))
    totalContribution = float(input("What is your CPF Contributions?"))
    getDistributions2a(age,totalContribution)
    
main()