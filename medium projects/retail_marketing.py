'''
adding products,
calculate price,
generate report,
handle  error cases
'''
# user = input('Enter your name:')
# citem = False
# products_list = {1:'brush',2:'tongue cleaner',3:'paste',4:'soap',5:'shampoo'}
# product_prices = [15,5,10,10,2]

# user_ordered = {}
# ordered_price = []

# def products():
#     print('List of Items are :')
#     for i in products_list:
#         print(i,':',products_list[i])
#     print()
#     if citem != True:
#         stage()

# def stage():
#     steps = {1:'list of items',2:'choose an item',3:'exit from store'}
#     for i in steps:
#         print(i,':',steps[i])
#     root()
    

# def chooseItem():
#    # citem = True
#     #products()
#     item_option = int(input('enter item number what you want or to go to main menu enter any number greater than 5:'))
#     if item_option <=5:
#         quantity(item_option)
#     else:
#         stage()
    
# def quantity(item_number):
#     quant = int(input('Enter quantity:'))
#     item = products_list[item_number]
#     user_ordered[quant]= item
#     chooseItem()

# def exit():
#     print('#'*15)
#     print('Bill')
#     print('Item          Quantity         price')
#     x=0
#     for i in user_ordered:        
#         price = i*product_prices[x]
#         ordered_price[x]=price
#         print('{}          {}          {}'.format(user_ordered[i],i,price))
#         x+=1
#     print('Total price is ',sum(ordered_price))
#     print('Thanks for visiting. hope you visit again')
    
# def root():
#     step_option = int(input('Select above option:'))
#     if step_option == 1:
#         products()
#     elif step_option ==2:
#         chooseItem()
#     elif step_option == 3:
#         exit()
#     else:
#         print('Invalid Option')
# stage()

import math
from datetime import datetime

name= input('enter your name:')

def bill_cal():
    a =True
    total_price =0
    list_item_price =[]
    while a:
        print('''
            1.list of items
            2.choose item
            3.exit
        ''')

    
        choice = int(input('enter your choice:'))
        choices =[1,2,3]
        if choice in choices:
            d = {'dal':23,'oil':35,'mirchi':33}
            if choice == 1: 
                c=1
                for i,j in d.items():
                    print('\t',c,'.',i,'₹',j)
                    c+=1
            if choice == 2:
                q =True
                while q:
                    print("press 'q' to to see main menu.")
                    item = input('enter item:')
                    if item in d.keys():
                        qnt = input('enter Quantity:')
                        if qnt.isdigit():
                            
                            qnt = int(qnt)
                            price = float(d[item]*qnt)
                            list_item_price.append((item,qnt,price))
                            total_price +=price
                        else:
                            print('Invalid Input Quantity..')
                    elif item == 'q':
                        q=False

                    else:
                        print('item not present.')


            if choice == 3:
                a = False
        else:
            print('Invalid Input..Please Enter a valid input.')
    return total_price,'Thank you, Please Visit again.',list_item_price

total,msg,item_price = bill_cal()
if total !=0:
    print('\n')
    print('''
                JP Stores
            BTM,Bangalore,560076
    ''')
    print('Customer Name:',name,'\t','Date:',datetime.now())
    print(20*'==')
    #print('\n')

    for j in item_price:
        print('Item:',j[0],'\tQuntity:',j[1],' Price:',j[2])

    gst = total * 0.1
    gst = math.ceil(gst)
    print(18*'==')
    print('GST: Rs.',float(gst))
    print('Total payble amount: Rs.',float(gst+total))
    print(18*'==')
    print('🙏🙏🙏 ',msg,' 🙏🙏🙏')
else:
    print("Hey, You weren't Brought anything...Please Buy something you want.")
    bill_cal()
#l = [('dal', 3, 69.0), ('dal', 3, 69.0)]




