import pandas as pd
a=pd.read_csv('/home/rahul/Downloads/medical_expenditure.csv')
A1=a[a["Nmale"]<=93]
A2=a[a['AverageDailyExpenditure']<=504]
if len(A2["Nmale"]<=504)*len(a)==len(A1)*len(A2):
    print('Independent')
else:
    print('Dependent')
A1=a[a["Nfemale"]<=131]
A2=a[a['AverageDailyExpenditure']<=504]
if len(A2['Nfemale']<=504)*len(a)==len(A1)*len(A2):
    print('Independent')
else:
    print('Dependent')
A1=a[a["Nage-group2"]<=25]
A2=a[a['AverageDailyExpenditure']>504]
if len(A2['Nage-group2']>504)*len(a)==len(A1)*len(A2):
    print('Independent')
else:
    print('Dependent')
A1=a[a["Nregion5"]<=53]
A2=a[a['AverageDailyExpenditure']>504]
if len(A2['Nage-group2']>504)*1565==len(A1)*len(A2):
    print('Independent')
else:
    print('Dependent')



import pandas as pd
a=pd.read_csv('/home/rahul/Downloads/medical_expenditure.csv')
def covar(x,y):
    l=sum(x)/len(x)
    m=sum(y)/len(y)
    k=0
    for i,j in zip(x,y):
        k+=(i-l)*(j-m)
    return k/(len(y)-1)
print(covar(a['Nmale'].tolist(),a['AverageDailyExpenditure'].tolist()))





import pandas as pd
a=pd.read_csv('/home/rahul/Downloads/medical_expenditure.csv')
def r(x,y):
    l=sum(x)/len(x)
    m=sum(y)/len(y)
    k=0
    n=0
    p=0
    for i,j in zip(x,y):
        k+=(i-l)*(j-m)
        n+=(i-l)**2
        p+=(j-l)**2
    g=k/((n*p)**0.5)
    if g==0:
        print('None')
    elif 0<g<=0.1 or 0<-g<=0.1:
        print('Weak')
    elif 0.1<g<=0.3 or 0.1<-g<=0.3:
        print('Moderate')
    elif 0.3<g<=0.5 or 0.3<-g<=0.5:
        print('Strong')
    elif 0.5<g<=1.0 or 0.5<-g<=1.0:
        print('Very Strong')
    else:
        print('Perfect')
r(a['Nmale'].tolist(),a['AverageDailyExpenditure'].tolist())
r(a['Nfemale'].tolist(),a['AverageDailyExpenditure'].tolist())
r(a['Nhp0'].tolist(),a['AverageDailyExpenditure'].tolist())
r(a['Nhp1'].tolist(),a['AverageDailyExpenditure'].tolist())
r(a['Nicd2'].tolist(),a['AverageDailyExpenditure'].tolist())
