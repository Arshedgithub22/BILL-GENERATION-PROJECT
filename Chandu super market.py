from datetime import datetime
name=input("Enter your name:")
list='''
rice     rs 50/kg
sugar    rs 20/kg
Maggi    rs 50/kg
boost    rs 30/each
closeup  rs 2/each
flour    rs 5/kg
chilli   rs 2/pac
ghee     rs 3/kg
'''
print(list)
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

items={'rice':70,'sugar':30,'Maggi':5,'boost': 10,'closeup':10,'flour':40,'chilli':50,'ghee':100}
option=int(input("Enter option:"))
if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("if you want buy press 1 or 2 for exit:")) 
    if inp1==2:
        break  
    if inp1==1:
        item=input("Enter your item:")
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=totalprice*5/100
            finalamount=gst+totalprice
        else:
            print("your item is not placed in above list")
    else:
        print("you entered false number")
    bill=input("if bill is needed press yes or no:")
    if bill == 'yes':
        pass
        if finalamount!=0:
            print(25*"=","CHANDU SUPER MARKET",25*"=")
            print(28*" ","RAYAPUDI")  
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-") 
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*' ',plist[i])
                print(75*"-")
                print(50*" ",'TotalAmount:','Rs',totalprice)
                print("gst amount",50*" ",'Rs',gst)
                print(75*"-")
                print(50*" ",'finalamount:','Rs',finalamount) 
                print(75*"-")
                print(50*" ",'Thanks for visiting')
                print(75*"-")  
                 
                 
        
