'''Question 2e CPF Total Contributions'''
import datetime, math
#to get group which people belongs to depending on their age
def getGroups(value, groups):
#     print(groups[0])
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
    oa = 0
    sa = 0
    ma = 0
#calculate oa, sa, ma
    if(value == 0):
        oa = round(totalContribution*cpfValue[0][0],2)
        sa = round(totalContribution*cpfValue[0][1],2)
        ma = round(totalContribution*cpfValue[0][2],2)
    elif(value == 1):
        oa = round(totalContribution*cpfValue[1][0],2)
        sa = round(totalContribution*cpfValue[1][1],2)
        ma = round(totalContribution*cpfValue[1][2],2) 
    elif(value == 2 ):
        oa = round(totalContribution*cpfValue[2][0],2)
        sa = round(totalContribution*cpfValue[2][1],2)
        ma = round(totalContribution*cpfValue[2][2],2)
    elif(value == 3):
        oa = round(totalContribution*cpfValue[3][0],2)
        sa = round(totalContribution*cpfValue[3][1],2)
        ma = round(totalContribution*cpfValue[3][2],2)
    elif(value == 4 ):
        oa = round(totalContribution*cpfValue[4][0],2)
        sa = round(totalContribution*cpfValue[4][1],2)
        ma = round(totalContribution*cpfValue[4][2],2)
    elif(value == 5 ):
        oa = round(totalContribution*cpfValue[5][0],2)
        sa = round(totalContribution*cpfValue[5][1],2)
        ma = round(totalContribution*cpfValue[5][2],2)
    elif(value == 6 ):
        oa = round(totalContribution*cpfValue[6][0],2)
        sa = round(totalContribution*cpfValue[6][1],2)
        ma = round(totalContribution*cpfValue[6][2],2)

    
    return oa,sa,ma
    
#Function to get month, year, ow, aw
def getDOB_totalwage():
    while True:
        try:
            month, year = input("Enter month and year, separated by space:").split()
            ow = float(input("Enter amount for monthly ordinary wages:"))
            aw = float(input("Enter amount for monthly additional wages:"))
            today = str(datetime.date.today())
            curr_year = int(today[:4])
            curr_month = int(today[5:7])
            age = curr_year - int(year)
            totalwages = ow + aw
            if(curr_month<int(month)):
                age = age - 1
            return totalwages, ow, aw, age 
        except ValueError:
            print("An error has occurred. Please try again.")
         
#Function to calculate CPF         
def calculateCPF(totalWages, ow, aw, age):
    employeeCPFContri = 0 #20% 
    employerCPFContri = 0 #17%
    totalCPFContri = 0
    if(age<55): #if age is less than 55
        if(totalWages<50):
            employeeCPFContri = 0
            employerCPFContri = totalCPFContri-employeeCPFContri
        elif(totalWages>50 and totalWages<=500):
            totalCPFContri = round(0.17*totalWages, 0)
            employeeCPFContri = 0
            employerCPFContri = totalCPFContri-employeeCPFContri
        elif(totalWages> 500 and totalWages<750):
            totalCPFContri = round(0.17*float(totalWages)+0.6*float(totalWages-500),0)
            employeeCPFContri = math.floor(0.6*(totalWages-500))
            employerCPFContri = totalCPFContri-employeeCPFContri
        else:#more than 750
            totalvalueContribution = round(0.37*float(ow)+0.37*float(aw),0)
            valueContributionEmployee = math.floor(0.2*float(ow))+0.2*float(aw)
            if(totalvalueContribution>=2220):
                totalCPFContri = 2220
            else:
                totalCPFContri = totalvalueContribution
            if(valueContributionEmployee>1200):
                employeeCPFContri = 1200
                employerCPFContri = totalCPFContri-employeeCPFContri
            else:
                employeeCPFContri =math.floor(valueContributionEmployee)
                employerCPFContri = totalCPFContri-employeeCPFContri
    elif(age>=55 and age<=60):  # if age is in the range of 55 and 60
        if(totalWages<50):
            totalCPFContri = 0
            employeeCPFContri = 0
            employerCPFContri = totalCPFContri-employeeCPFContri
        elif(totalWages>50 and totalWages<500): 
            totalCPFContri = round(0.13*float(totalWages),0)
            employeeCPFContri = 0
            employerCPFContri = totalCPFContri-employeeCPFContri
        elif(totalWages>500 and totalWages<750):
            totalCPFContri = 0.13*float(totalWages)+0.39*float((totalWages-500))
            employeeCPFContri = math.floor(0.39*(totalWages-500))
            employerCPFContri = totalCPFContri-employeeCPFContri
        else:
            totalvalueContribution = round(0.26*float(ow)+0.26*float(aw),0)
            valueContributionEmployee = math.floor(0.13*float(ow)+0.13*float(aw))
            if(totalvalueContribution>=1560):
                totalCPFContri = 1560
            else:
                totalCPFContri = totalvalueContribution
            if(valueContributionEmployee>780):
                employeeCPFContri = 780
                employerCPFContri = totalCPFContri-employeeCPFContri
            else:
                employeeCPFContri = valueContributionEmployee
                employerCPFContri = totalCPFContri-employeeCPFContri
    elif(age>60 and age<65):    #if age is in the range of 60 to 65
        if(totalWages<50):
            totalCPFContri = 0
            employeeCPFContri = 0
            employerCPFContri = totalCPFContri-employeeCPFContri
        elif(totalWages>50 and totalWages<500):
            totalCPFContri = round(0.09*float(totalWages),0)
            employeeCPFContri = 0
            employerCPFContri = totalCPFContri-employeeCPFContri
        elif(totalWages >500 and totalWages <750):
            totalCPFContri = round(0.09*float(totalWages)+0.225*float((totalWages-500)),0)
            employeeCPFContri = 0.225*(totalWages-500)
            employerCPFContri = totalCPFContri-employeeCPFContri
        else:
            totalvalueContribution = round(0.165*float(ow)+0.165*float(aw),0)
            valueContributionEmployee = math.floor(0.075*float(ow)+0.075*float(aw))
            if(totalvalueContribution>=990):
                totalCPFContri = 990
            else:
                totalCPFContri = totalvalueContribution
            if(valueContributionEmployee>450):
                employeeCPFContri = 450
                employerCPFContri = totalCPFContri-employeeCPFContri
            else:
                employeeCPFContri = valueContributionEmployee
                employerCPFContri = totalCPFContri-employeeCPFContri
    else:       #if age is above 65
        if(totalWages<50):
            totalCPFContri = 0
            employeeCPFContri = 0
            employerCPFContri = totalCPFContri-employeeCPFContri
        elif(totalWages>50 and totalWages<500):
            totalCPFContri = 0.075*float(totalWages)
            employeeCPFContri = 0
            employerCPFContri = totalCPFContri-employeeCPFContri
        elif(totalWages>500 and totalWages<750):
            totalCPFContri.append(0.075*float(totalWages)+0.15*float((totalWages-500)))
            employeeCPFContri = 0.15*(totalWages-500)
            employerCPFContri = totalCPFContri-employeeCPFContri
        else:
            totalvalueContribution = math.ceil(0.125*float(ow)+0.125*float(aw))
            valueContributionEmployee = math.floor(0.05*float(ow)+0.05*float(aw))
            if(totalvalueContribution>=750):
                totalCPFContri = 750
            else:
                totalCPFContri = totalvalueContribution
            if(valueContributionEmployee>300):
                employeeCPFContri = 300 
                employerCPFContri = totalCPFContri-employeeCPFContri
            else:
                employeeCPFContri = valueContributionEmployee
                employerCPFContri = totalCPFContri-employeeCPFContri


                
    return totalCPFContri, employeeCPFContri, employerCPFContri

#function to print the output of calculated oa, sa, ma
def writeFile(age, ow, aw, totalwages, employeeCPFContri, employerCPFContri, oa, sa, ma):
    print("Total CPF contribution:\t\t${:.0f}".format(totalwages))
    print("Employee CPF contribution:\t${:.0f}".format(employeeCPFContri))
    print("Employer CPF contribution:\t${:.0f}".format(employerCPFContri))
    print("Contribution to Ordinary Account: ${:.2f}".format(oa))
    print("Contribution to Special Account: ${:.2f}".format(sa))
    print("Contribution to Medisave Account: ${:.2f}".format(ma))
#                         
      
  
def main():
    totalwages, ow, aw, age  = getDOB_totalwage()
    totalContribution, employeeCPFContri, employerCPFContri  = calculateCPF(totalwages, ow, aw, age)
    oa, sa, ma = getDistributions2b(age,totalContribution)    
    writeFile(age, ow, aw, totalContribution, employeeCPFContri, employerCPFContri, oa, sa, ma)
    
main()