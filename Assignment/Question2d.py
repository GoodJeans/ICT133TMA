import datetime, math
'''Function to get contributions'''
def getContributions(month, year, ow, aw):
    age = getAge(month, year)
    totalWages = ow + aw
    ageRange = (55, 60, 65)
    wageRange = (50, 500, 750)
    totalCPFContributions = 0
    
    if(age <= ageRange[0]): #if age is less than or equals to 55

        if (totalWages <= wageRange[0] ):
            totalCPFContributions = 0
            employeeShareContributions = 0
        
        elif (totalWages > wageRange[0] and totalWages< wageRange[1]):
            totalCPFContributions = 0.17* totalWages
            employeeShareContributions = 0
        
        elif (totalWages > wageRange[1] and totalWages< wageRange[2]):
            totalCPFContributions = 0.17* totalWages + 0.6 * (totalWages - 500)
            employeeShareContributions = 0.6 * (totalWages - 500 )
        
        else:
            totalCPFContributions = 0.37 * ow + 0.37 * aw 
            employeeShareContributions = 0.2 * ow + 0.2 * aw 
            if(totalCPFContributions > 2220):
                totalCPFContributions = 2200
            if(employeeShareContributions > 1200):
                employeeShareContributions = 1200
                
    elif (age > ageRange[0] and age < ageRange[1]): #if age range is 55 to 60
        
        if (totalWages < wageRange[0] ):
            totalCPFContributions = 0
            employeeShareContributions = 0
        
        elif( totalWages < wageRange[1] ):
            totalCPFContributions = 0.13 * totalWages
            employeeShareContributions = 0
        
        elif (totalWages >= wageRange[1]):
            totalCPFContributions = 0.13 * totalWages + 0.39 * (totalWages - 500)
            employeeShareContributions = 0.39 * (totalWages - 500)
            
        else:
            totalCPFContributions = (0.26 * ow) + (0.26 * aw)
            employeeShareContributions = (0.13 * ow) + (0.13 * aw)

            if(totalCPFContributions >= 1560):
                totalCPFContributions = 1560 
            
            if(employeeShareContributions > 780):
                employeeShareContributions = 780
    
    elif (age > ageRange[1] and age < ageRange[2] ):   #if age range is 60 to 65
        
        if (totalWages <wageRange[0]):
            totalCPFContributions = 0
            employeeShareContributions = 0
        
        elif (totalWages < wageRange[1]):
            totalCPFContributions = 0.09 * totalWages
            employeeShareContributions = 0
        
        elif (totalWages > wageRange[1] and totalWages < wageRange[2]):
            totalCPFContributions = 0.09 * totalWages + 0.225 * (totalWages - 500)
            employeeShareContributions = 0.225 * (totalWages - 500)
        
        else:
            totalCPFContributions = (0.165 * ow) + (0.165 * aw)
            employeeShareContributions = (0.075 * ow) + (0.075 * aw)
            if(totalCPFContributions > 990):
                totalCPFContributions = 990
            if (employeeShareContributions >450 ):
                employeeShareContributions = 450
    
    else:           # if age range is above 65
        if (totalWages < wageRange[0]):
            totalCPFContributions = 0
            employeeShareContributions = 0
            
        elif (totalWages > wageRange[0] and totalWages < wageRange[1] ):
            totalCPFContributions = 0.075 * totalWages
            employeeShareContributions = 0
        
        elif (totalWages > wageRange[1] and totalWages < wageRange[2] ):
            totalCPFContributions = 0.075 * totalWages + 0.15 * (totalWages - 500 )
            employeeShareContributions = 0.15 * (totalWages - 500 )
        
        else:
            totalCPFContributions = (0.125 * ow) + (0.125 * aw) 
            employeeShareContributions = 0.05 * ow + 0.05 * aw
            
            if (totalCPFContributions > 750 ):
                totalCPFContributions = 750 
            if (employeeShareContributions > 300):
                employeeShareContributions = 300
        
    print("Total CPF Contributions is ${:.2f}" .format(round(totalCPFContributions,0)))
    print("Total employee contributions is ${:.2f}" .format(math.floor(employeeShareContributions)))

'''Function to get age'''
def getAge(month, year):
    today = str(datetime.date.today())
    curr_year = int(today[:4])
    curr_month = int(today[5:7])
    age = curr_year - int(year)
    if(curr_month<int(month)):
        age = age - 1
        
    return age
        
def main():
    month, year = input("Enter month and year, separated by space:").split()
    ow = float(input("Enter amount for monthly ordinary wages:"))
    aw = float(input("Enter amount for monthly additional wages:"))
    getContributions(month, year, ow, aw)
    
main()