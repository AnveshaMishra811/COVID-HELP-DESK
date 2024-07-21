#all over india
import matplotlib.pyplot as plt
import numpy as np
def india():
    plt.plot(['march','april','may','june','july','Aug ',' sept ',' october'],[26,1118,3967,11502,29429,65002,83809,67708])
    plt.title('MONTHLY AVERAGE OF CASES IN INDIA')
    plt.xlabel('MONTHS')
    plt.ylabel('AVERAGE COVID CASES IN INDIA')
    plt.show()
    
#recovered cases
def recovered():
    plt.plot(['march','april','may','june','july','Aug ',' sept ',' october'],[25.6,2691,28555,210010,668135,1861458,3861858,6520011])
    plt.title('RECOVERED CASES')
    plt.xlabel('Months')
    plt.ylabel('Average recovered cases(per month)')
    plt.show()
#recovered()
#india()
#fatality cases
def fatality():
    plt.plot(['march','april','may','june','july','Aug ',' sept ',' october'],[0,39,100,325,582,996,1054,680])
    plt.title('FATALITY CASES')
    plt.xlabel('Months')
    plt.ylabel('Average fatality cases(per month)')
    plt.title('MONTHLY AVERAGE CASES OF FATALITY IN INDIA')
    plt.show()
#unt wise cases
def un():
    l3=['Andaman&NicobarIslands','Chandigarh','Dadra & Nagar Haveli','Government of Delhi','Jammu&Kashmir','Ladhakh','Lakshadweep','Puducherry']
    l4=[4184,13848,3213,344318,90166,5812,0,33832]
    y_pos=np.arange(len(l3))
    plt.barh(y_pos,l4,align='center',color='y')
    plt.yticks(y_pos,l3)
    plt.xlabel('cases')
    plt.title('MONTHLY AVERAGE CASES IN UNION TERRITORIES ')
    for index,value in enumerate(l4):
        plt.text(value,index,str(value))
    plt.show()


#state wise
def state():
    l1=['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chattisgarh','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','kerela','Madhya Pradesh','Maharashtra','Manipur']
    l2=['Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','Uttar Pradesh','West bengal']
    l=l1+l2
    l5=[796919,14077,203282,209447,170130,601150,41586,163959,154495,19844,98610,788551,369323,164341,1625197,16621,8720,2359,8296,276094,129693,180755,3727,700193,229001,30070,59508,463858,337283]
    y_pos=np.arange(len(l))
    plt.barh(y_pos,l5,align='center',color='green')
    plt.yticks(y_pos,l)
    plt.xlabel('cases')
    plt.title('MONTHY AVERAGE CASES IN STATES')
    for index,value in enumerate(l5):
        plt.text(value,index,str(value))
    plt.show()

ch=0
print('1:Graph representing monthly average cases all over India')
print('2:Graph representing monthly average recovered cases all over India')
print('3:Graph representing monthly average fatality cases all over India')
print('4:Graph representing average cases in states of India')
print('5:Graph representing average cases in union territories of India')
print()
ch=input('enter number written against the type of graph you want to view')
c=ch.split(',')
for i in c:
    if i=='1':
        india()
    elif i=='2':
        recovered()
    elif i=='3':
        fatality()
    elif i=='4':
        state()
    elif i=='5':
        un()
    else:
        print('invalid choice entered')
        break
print()

    
    

