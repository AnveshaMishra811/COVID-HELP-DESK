from care import state
from care import hospitals
l1=[]
import csv
def Q1():
    ch=0
    sum=0
    a=[8,10,15,6,0]
    print('Are you experiencing any of the following symptoms ?')
    print('1:cough')
    print('2:fever')
    print('3:difficulty in breathing')
    print('4:loss of sense of taste and smell')
    print('5:none of the above')
    ch=input('Response (enter number against the detail): ')
    c=ch.split(',') 
    for i in c:
        if i=='1':
            sum+=(a[0])
        elif i=='2':
            sum+=(a[1])
        elif i=='3':
            sum+=(a[2])
        elif i=='4':
            sum+=(a[3])
        elif i=='5':
            sum+=(a[4])
        else:
            print('wrong response entered')
    l1.append(sum)
    
def Q2():
    ch=0
    sum=0
    d={'diabetes':8,'hypertension':6,'any kind of lung disease':10,'heart disease':9,'kidney disorder':7,'none of the above':0}
    l=list(d.keys())
    a=list(d.values())
    print('Have you/Are you suffering from any of the following disease(s) ?')
    print('1:diabetes')
    print('2:hypertension')
    print('3:any kind of lung disease')
    print('4:heart disease')
    print('5:kidney disorder')
    print('6:none of the above')
    ch=input('Response (enter number against the detail): ')
    c=ch.split(',') 
    for i in c:
        if i=='1':
            sum+=(a[0])
        elif i=='2':
            sum+=(a[1])
        elif i=='3':
            sum+=(a[2])
        elif i=='4':
            sum+=(a[3])
        elif i=='5':
            sum+=(a[4])
        elif i=='6':
            sum+=(a[5])
        else:
            print('wrong response entered')
    l1.append(sum)

def Q3():
    sum=0
    ch=0
    print('Have u travelled anywhere internationally in the last 28-45 days ?')
    print('1:Yes')
    print('2:No')
    ch=input('Response (write yes/no only): ')
    if ch=='Yes' or ch=='yes' or ch=='YES':
        sum+=5
    elif ch=='No' or ch=='no' or ch=='NO':
        sum+=0
    else:
        print()
    l1.append(sum)
    
def Q4():
    sum=0
    ch=0
    print('Which of the following apply to you ?')
    print('1: I have recently interacted or lived with someone who has tested positive for COVID-19')
    print('2: I am a healthcare worker and I examined a COVID-19 confirmed case without protective gear')
    print('3: None of the above')
    ch=int(input('Response (enter number against the detail): '))
    if ch==1:
        sum+=10
    elif ch==2:
        sum+=12
    elif ch==3:
        sum+=0
    else:
        print('wrong number entered')
    l1.append(sum)


    
Q1()
print()
Q2()
print()
Q3()
print()
Q4()
    
s=0
for i in l1:
    s+=i
if s==0 or s<=8:
    print(end='\n')
    print('you are at an EXTREMELY LOW RISK')
    print()
    print('Follow government guidelines to keep yourself safe')  
elif s==9 or s<=12:
    print(end='\n')
    print('You are at LOW RISK of having the infection')
    print()
    print('Take necessary precautions and have a proper diet')
elif s==13 or s<=27:
    print(end='\n')
    print('You are at MODERATE RISK of having the infection')
    print()
    print('Home isolation is recommended,Please stay at home and help us prevent the spreading the virus')
    print('If you prefer to get a test done, then here are some COVID centres listed according to the state in which u reside')
    hospitals()
elif s==28 or s<=36:
    print(end='\n')
    print('You are at HIGH RISK !!!')
    print()
    print('You are recommended to take up a voluntary COVID-19 test')
    print('Here are some COVID centres according to the state in which u reside')
    hospitals()
elif s==37 or s<=45:
    print(end='\n')
    print('You are at an EXTREMELY HIGH RISK!!!')
    print()
    print('Contact to the nearest COVID testing centre and get a test done immediately!')
    print('Here are some COVID centres according to the state in which u reside')
    print('\n')
    hospitals()
else:
    print("ERROR")
    
print()  
print('Thank you for spending your precious time in endeavouring the self assessment test and helping us to reach out to those infected and helping them in thier recovery')

   


    
    
        
    
    
    
    

    
    
    
