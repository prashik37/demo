#groserry billing application :
groserry ={'1':{'name':'maggie','stock':200,'price':20},
           '2':{'name':'pencil','stock':200,'price':10},
           '3':{'name':'perfume','stock':100,'price':200},
           '4':{'name':'tpaste','stock':150,'price':75},
           '5':{'name':'soap','stock':120,'price':30},
           '6':{'name':'oilpkg','stock':130,'price':120}}
final_amount=0
amount1=0
amount2=0
qtn =input("u want menu?")
ans ='yes'
print("prod_id\tname\t\tstock\t\tprice")
print("-----------------------------------------------------------------")
if qtn== ans:
    for key,val in groserry.items():

        name = val['name']
        stock = val['stock']
        price = val['price']
        print(f"{key}\t\t{name}\t\t{stock}\t\t\t{price}")
        print("-----------------------------------------------------------------")


msg = input("which product u want to buy ")
for key,val in groserry.items():
    for k,v in val.items():
        if v==msg:
           print({key:val})
           msg1=int(input("how many u want"))
           amount1 = val['price'] * msg1
           print("amount1 = ", amount1)
           val['stock']=val['stock']-msg1

msg2 = input("u want to buy other things ")
ans2 = 'yes'
qtn = input("u want menu?")
ans = 'yes'
print("prod_id\tname\t\tstock\t\tprice")
print("-----------------------------------------------------------------")
if qtn == ans:
    for key, val in groserry.items():
            name = val['name']
            stock = val['stock']
            price = val['price']
            print(f"{key}\t\t{name}\t\t{stock}\t\t\t{price}")
            print("-----------------------------------------------------------------")
if msg2 == ans2:
    msg = input("which product u want to buy ")
    for key, val in groserry.items():
        for k, v in val.items():
             if v == msg:
              print({key: val})
              msg1 = int(input("how many u want"))
              amount2 = val['price'] * msg1
              print(" amount2 = ", amount2)
              val['stock'] = val['stock'] - msg1
msg = input("you want bill ")
ans = 'yes'
if ans==msg:
    final_amount = amount1+amount2
    print("final_amount=",final_amount)
    if final_amount>1000:
       fair_amount= final_amount-(final_amount/10)
       print("fair amount= ",fair_amount)

