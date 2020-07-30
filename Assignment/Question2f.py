'''Question 2f CPF Total Contributions'''
import datetime, math

#to open file
def openFile():
    with open('Q2Data.txt') as data:
        content = data.read().splitlines()
    return content


def getGroups(value, groups):
    groupStore = []
    i = 0
    while (i < len(value)):
        if(value[i] <= groups[0]): #35 and below
            groupStore.append(0)
        elif(value[i]>groups[0] and value[i] <= groups[1] ) : #above 35-45
            groupStore.append(1)
        elif(value[i]>groups[1] and value[i] <=groups[2]): #above 45 - 50
            groupStore.append(2)
        elif(value[i]>groups[2] and value[i] <=groups[3]): #above 50 - 55
            groupStore.append(3)
        elif(value[i]>groups[3] and value[i] <=groups[4]): #above 55 - 60 
            groupStore.append(4)
        elif(value[i]>groups[4] and value[i] <=groups[5]): #above 60 - 65
            groupStore.append(5)
        elif(value[i]>groups[5]): #above 65
            groupStore.append(6)
        
        i+=1   
            
    return groupStore

def getDistributions2b(age, totalContribution):
    cpfValue = [    #partially completed for demo
                    #rates group
       (0.6217, 0.1621, 0.2162),  #age<=35
       (0.5677, 0.1891, 0.2432),  #age<35-45
       (0.5136, 0.2162, 0.2702),  #age45-50
       (0.4055, 0.3108, 0.2837),  #age50-55
       (0.4616, 0.1346, 0.4038),  #age55-60
       (0.2122, 0.1515, 0.6363),  #age60-65
       (0.08, 0.08, 0.84)        #age>65
    ]
    groups = (35, 45, 50, 55, 60, 65)
    value = getGroups(age, groups)
    oa = []
    sa = []
    ma = []
    i = 0
    #calcculation for oa, sa, ma
    while (i<len(totalContribution)):
        if(value[i] == 0):
            oa.append(round(totalContribution[i]*cpfValue[0][0],2))
            sa.append(round(totalContribution[i]*cpfValue[0][1],2))
            ma.append(round(totalContribution[i]*cpfValue[0][2],2))
        elif(value[i] == 1):
            oa.append(round(totalContribution[i]*cpfValue[1][0],2))
            sa.append(round(totalContribution[i]*cpfValue[1][1],2))
            ma.append(round(totalContribution[i]*cpfValue[1][2],2)) 
        elif(value[i] == 2 ):
            oa.append(round(totalContribution[i]*cpfValue[2][0],2))
            sa.append(round(totalContribution[i]*cpfValue[2][1],2))
            ma.append(round(totalContribution[i]*cpfValue[2][2],2))
        elif(value[i] == 3):
            oa.append(round(totalContribution[i]*cpfValue[3][0],2))
            sa.append(round(totalContribution[i]*cpfValue[3][1],2))
            ma.append(round(totalContribution[i]*cpfValue[3][2],2))
        elif(value[i] == 4 ):
            oa.append(round(totalContribution[i]*cpfValue[4][0],2))
            sa.append(round(totalContribution[i]*cpfValue[4][1],2))
            ma.append(round(totalContribution[i]*cpfValue[4][2],2))
        elif(value[i] == 5 ):
            oa.append(round(totalContribution[i]*cpfValue[5][0],2))
            sa.append(round(totalContribution[i]*cpfValue[5][1],2))
            ma.append(round(totalContribution[i]*cpfValue[5][2],2))
        elif(value[i] == 6 ):
            oa.append(round(totalContribution[i]*cpfValue[6][0],2))
            sa.append(round(totalContribution[i]*cpfValue[6][1],2))
            ma.append(round(totalContribution[i]*cpfValue[6][2],2))
        
        i+=1
    return oa,sa,ma
    
def getList(content):
        try:
            #to calculate age of user
            month_list = []
            year_list = []
            ow_list = []
            aw_list = []
            age = []
            totalwages = []
            for i in range(0, len(content),3 ):
                monthAndYear = content[i]
                month, year = monthAndYear.split(' ')
                month_list.append(month)
                year_list.append(year)
                ow_list.append(content[i+1])
                aw_list.append(content[i+2])
            
            #to retrieve current month and year today
            today = str(datetime.date.today())
            curr_year = int(today[:4])
            curr_month = int(today[5:7])

            for x in range (0, len(year_list)):
                curr_age = curr_year - int(year_list[x])
                totalwages.append(float(ow_list[x]) + float(aw_list[x]))
                if(curr_month<int(month_list[x])):
                    age.append(curr_age - 1)
                else:
                    age.append(curr_age)          
        except ValueError:
                print("An error has occurred. Please try again.")

        return totalwages, ow_list, aw_list, age
def calculateCPF(totalWages_list, ow_list, aw_list, age_list):
    print("")   
    employeeCPFContri = [] #20% 
    employerCPFContri = [] #17%
    totalCPFContri    = []
    i=0
    while (i<len(totalWages_list)):
                try:
                    if(age_list[i]<55):  #if age range is less than 55
                        if(totalWages_list[i]<50): 
                            employeeCPFContri.append(0)
                            employerCPFContri.append(0)
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                        elif(totalWages_list[i]>50 and totalWages_list[i]<=500):
                            totalCPFContri.append(round(0.17*totalWages_list[i]),0)
                            employeeCPFContri.append(0)
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                        elif(totalWages_list[i]> 500 and totalWages_list[i]<750):  
                            totalCPFContri.append(round(0.17*float(totalWages_list[i])+0.6*float(totalWages_list[i]-500),0))
                            employeeCPFContri.append(math.floor(0.6*(totalWages_list[i]-500)))
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                        else:   #total wage is more than 750
                            totalvalueContribution = round(0.37*float(ow_list[i])+0.37*float(aw_list[i]),0)
                            valueContributionEmployee = math.floor(0.2*float(ow_list[i]))+0.2*float(aw_list[i])
                            if(totalvalueContribution>=2220):
                                totalCPFContri.append(2220)
                            else:  
                                totalCPFContri.append(totalvalueContribution)
                            if(valueContributionEmployee>1200):
                                employeeCPFContri.append(1200)
                                employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                            else:
                                employeeCPFContri.append(math.floor(valueContributionEmployee))
                                employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                    elif(age_list[i]>=55 and age_list[i]<=60):   #if age range is between 55 to 60
                        if(totalWages_list[i]<50):             
                            totalCPFContri.append(0)        
                            employeeCPFContri.append(0)
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])    
                        elif(totalWages_list[i]>50 and totalWages_list[i]<500):    
                            totalCPFContri.append(round(0.13*float(totalWages_list[i]),0))
                            employeeCPFContri.append(0)
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                        elif(totalWages_list[i]>500 and totalWages_list[i]<750):    
                            totalCPFContri.append(round(0.13*float(totalWages_list[i])+0.39*float((totalWages_list[i]-500))),0)
                            employeeCPFContri.append(math.floor(0.39*(totalWages_list-500)))
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                        else:   #if total wage is more than 750
                            totalvalueContribution = round(0.26*float(ow_list[i])+0.26*float(aw_list[i]),0)
                            valueContributionEmployee = math.floor(0.13*float(ow_list[i])+0.13*float(aw_list[i]))
                            if(totalvalueContribution>=1560):
                                totalCPFContri.append(1560)
                            else:
                                totalCPFContri.append(totalvalueContribution)
                            if(valueContributionEmployee>780):
                                employeeCPFContri.append(780)
                                employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                            else:
                                employeeCPFContri.append(valueContributionEmployee)
                                employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                    elif(age_list[i]>60 and age_list[i]<65):    #if age range is from 60 to 65 
                        if(totalWages_list[i]<50):              
                            totalCPFContri.append(0)
                            employeeCPFContri.append(0)
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                        elif(totalWages_list[i]>50 and totalWages_list[i]<500): 
                            totalCPFContri.append(round(0.09*float(totalWages_list[i])),0)
                            employeeCPFContri.append(0)
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                        elif(totalWages_list[i]>500 and totalWages_list[i]<750):
                            totalCPFContri.append(round(0.09*float(totalWages_list[i])+0.225*float((totalWages_list[i]-500))),0)
                            employeeCPFContri.append(0.225*(totalWages_list-500))
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                        else:
                            totalvalueContribution = round(0.165*float(ow_list[i])+0.165*float(aw_list[i]),0)
                            valueContributionEmployee = math.floor(0.075*float(ow_list[i])+0.075*float(aw_list[i]))
                            if(totalvalueContribution>=990):
                                totalCPFContri.append(990)
                            else:
                                totalCPFContri.append(totalvalueContribution)
                            if(valueContributionEmployee>450):
                                employeeCPFContri.append(450)
                                employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                            else:
                                employeeCPFContri.append(valueContributionEmployee)
                                employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                    else:
                        if(totalWages_list[i]<50):
                            totalCPFContri.append(0)
                            employeeCPFContri.append(0)
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                        elif(totalWages_list[i]>50 and totalWages_list[i]<500):
                            totalCPFContri.append(0.075*float(totalWages_list[i]))
                            employeeCPFContri.append(0)
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                        elif(totalWages_list[i]>500 and totalWages_list[i]<750):
                            totalCPFContri.append(0.075*float(totalWages_list[i])+0.15*float((totalWages_list[i]-500)))
                            employeeCPFContri.append(0.15*(totalWages_list-500))
                            employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                        else:
                            totalvalueContribution = math.ceil(0.125*float(ow_list[i])+0.125*float(aw_list[i]))
                            valueContributionEmployee = math.floor(0.05*float(ow_list[i])+0.05*float(aw_list[i]))
                            if(totalvalueContribution>=750):
                                totalCPFContri.append(750)
                            else:
                                totalCPFContri.append(totalvalueContribution)
                            if(valueContributionEmployee>300):
                                employeeCPFContri.append(300)
                                employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                            else:
                                employeeCPFContri.append(valueContributionEmployee)
                                employerCPFContri.append(totalCPFContri[i]-employeeCPFContri[i])
                    i+=1
                except ValueError:
                    print("Error")
                
    return totalCPFContri, employeeCPFContri, employerCPFContri

def writeFile(age_list,ow_list, aw_list, totalwages_list, employeeCPFContri, employerCPFContri, oa_list, sa_list, ma_list):

        with open("output.txt","w") as file:
            for i in range(len(totalwages_list)):
                '''Print out output to text file'''
                file.write("Age:{0} OW: ${1} AW: ${2}\n".format(age_list[i],ow_list[i],aw_list[i] ))
                file.write("Total CPF contribution:\t\t${:.0f}\n".format(totalwages_list[i]))
                file.write("Employee CPF contribution:\t${:.0f}\n".format(employeeCPFContri[i]))
                file.write("Employer CPF contribution:\t${:.0f}\n".format(employerCPFContri[i]))
                file.write("Contribution to Ordinary Account: ${:.2f}\n".format(oa_list[i]))
                file.write("Contribution to Special Account: ${:.2f}\n".format(sa_list[i]))
                file.write("Contribution to Medisave Account: ${:.2f}\n".format(ma_list[i]))
                '''Print out output on cconsole''' 
                print("Age:{0} OW: ${1} AW: ${2}".format(age_list[i],ow_list[i],aw_list[i] ))
                print("Total CPF contribution:\t\t${:.0f}".format(totalwages_list[i]))
                print("Employee CPF contribution:\t${:.0f}".format(employeeCPFContri[i]))
                print("Employer CPF contribution:\t${:.0f}".format(employerCPFContri[i]))
                print("Contribution to Ordinary Account: ${:.2f}".format(oa_list[i]))
                print("Contribution to Special Account: ${:.2f}".format(sa_list[i]))
                print("Contribution to Medisave Account: ${:.2f}".format(ma_list[i]))
def main():
    content = openFile()
    totalwages_list, ow_list, aw_list, age_list  = getList(content)
    totalContribution, employeeCPFContri, employerCPFContri  = calculateCPF(totalwages_list, ow_list, aw_list, age_list)
    oa_list, sa_list, ma_list = getDistributions2b(age_list,totalContribution)    
    writeFile(age_list,ow_list, aw_list, totalContribution, employeeCPFContri, employerCPFContri, oa_list, sa_list, ma_list)
    
main()