import datetime
q=input("enter your name:")
input("for list of items press 1:")
s=''' 
    Rice   Rs 20/kg
    Sugar  Rs 30/kg
    oil    Rs 120/litre
    panner Rs 100/kg
    flour  Rs 20/kg'''
items_list={'rice':20,'sugar':30,'oil':120,'panner':100,'flour':20}
print(s)
items=list()
quantity=list()
total_list=list()
total_sum=0
while(True):
    option=input("if you want to buy press 1 or 2 for exit:")
    if option=='1':
        preference_items=input("enter your items:")
        if preference_items in items_list.keys():
            items.append(preference_items)
            prefered_quantity=input("enter quantity:")
            quantity.append(int(prefered_quantity))
            choice=input("can i bill i items yes or no:")
            if choice=='yes':
                print("==========================kiran supermarket================================")
                print('wanaparthy'.center(60))
                print("Name",q,end=" ")
                now=datetime.datetime.now()
                print("\t\t\t\t\tDate:",now)
                print('---------------------------------------------------------------------------')
                print("sno"+" "+"items"+" "+"quantity"+" "+"price")
                length=len(items)
                for i in range(length):
                    print(i,end="    ")
                    print(items[i],end="   ")
                    print(quantity[i],end="     ")
                    value=items_list.get(items[i])
                    total_quantity=value*quantity[i]
                    total_list.append(int(total_quantity))
                    print(total_quantity)
                print('--------------------------------------------------------------------')
                for j in total_list:
                    total_sum=total_sum+j
                print("\t\t\t\t\t\t\t\tTotal amount:",total_sum)
                print("gst amount",end="")
                gst=total_sum*5/100
                print("\t\t\t\t\t\t\t\tGst:",gst)
                print('---------------------------------------------------------------------')
                print("\t\t\t\t\t\t\t\t\t\tFinal amount:",total_sum+gst)
                print('---------------------------------------------------------------------')
                print("Thank you for visiting")
            elif choice=='no':
                continue
        else:
            print("sorry item not available")
    elif option=='2':
        break
    else:
        print("you have entered wrong number")











