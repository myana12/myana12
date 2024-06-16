import datetime
class market:
    items=list()
    quantity=list()
    total_list=list()
    total_sum=0
    def __init__(self,q,items):
        self.name =q
        self.items1=items
    def purchasing(self):
        while(True):
            option=input("if you want to buy press 1 or 2 for exit:")
            if option=='1':
                preference_items=input("enter your items:")
                if preference_items in self.items1.keys():
                    self.items.append(preference_items)
                    prefered_quantity=input("enter quantity:")
                    self.quantity.append(int(prefered_quantity))
                    choice=input("can i bill i items yes or no:")
                    if choice=='yes':
                        print("===================kiran supermarket====================")
                        print('wanaparthy'.center(60))
                        print("Name",self.name,end=" ")
                        now=datetime.datetime.now()
                        print("\t\t\t\t\tDate:",now)
                        print('---------------------------------------------')
                        print("sno"+" "+"items"+" "+"quantity"+" "+"price")
                        length=len(self.items)
                        for i in range(length):
                            print(i,end="    ")
                            print(self.items[i],end="   ")
                            print(self.quantity[i],end="     ")
                            value=items_list.get(self.items[i])
                            total_quantity=value*self.quantity[i]
                            self.total_list.append(int(total_quantity))
                            print(total_quantity)
                        print('-------------------------------------------------')
                        for j in self.total_list:
                            self.total_sum=self.total_sum+j
                        print("\t\t\t\t\t\t\t\tTotal amount:",self.total_sum)
                        print("gst amount",end="")
                        gst=self.total_sum*5/100
                        print("\t\t\t\t\t\t\t\tGst:",gst)
                        print('------------------------------------------------')
                        print("\t\t\t\t\t\t\t\t\t\tFinal amount:",self.total_sum+gst)
                        print('-------------------------------------------------')
                        print("Thank you for visiting")
                    elif choice=='no':
                        continue
                else:
                    print("sorry item not available")
            elif option=='2':
                break
            else:
                print("you have entered wrong number")
q=input("enter name")
t=input("for list of items press 1:")
items_list={'rice':20,'sugar':30,'oil':120,'panner':100,'flour':20}
s=''' 
    Rice   Rs 20/kg
    Sugar  Rs 30/kg
    oil    Rs 120/litre
    panner Rs 100/kg
    flour  Rs 20/kg'''
print(s)
r1=market(q,items_list)
r1.purchasing()
