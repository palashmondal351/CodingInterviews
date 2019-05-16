# Apple junier python developer
ap,gp=map(float,input().split(';'))
paise={.01:'PENNY', .05:'NICKEL', .10:'DIME', .25:'QUATER', .50:'HALF HOLLAR',
       1:'ONE', 2:'TWO', 5:'FIVE', 10:'TEN', 20:'TWENTY', 50:'FIFTY', 100:'ONE HUNDED'}
value=[100,50,20,10,5,2,1,.50,.25,.10,.05,.01]
def result(ap,gp):
    if(ap>gp):
        print('ERROR')
        return
    elif(ap==gp):
        print('NONE')
        return
    else:
        rval=gp-ap
        l=[]
        for val in value:
            if(rval>=val):
                l.append(val)
                rval-=val
        reamt=sorted([paise[k] for k in l])
        print(','.join(reamt))
        return
result(ap,gp)                
