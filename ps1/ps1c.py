annual_salary = float(input("Your salary : "))
#kişi yıllık maaşını girdi
a = annual_salary
total_cost = 1000000
#almak istediği evin fiyatı
portion_saved = 5000
#ayrılan para 
biggest = 10000
#en büyük değeri yazdım
smallest = 0
#en küçük değer
semi_annual_rise = 0.07
#yarıyılda bir artaacak maaş miktarı
portion_down_payment = 0.25
#ödemes gereken en az para
r = 0.04
#ayırdığı paranın ona geri dönüşü
#her denemeyi bulmak için while döngüsü açtım
d = 0
while True :
    annual_salary = a
    current_savings = 0
    for i in range(36):
        #kişinin birikiminin geri dönüşü
        current_savings += (current_savings*r/12)
        #kişinin maaşının aylık değerinin bir kısmını ayıracak 
        monthly_salary = annual_salary/12
        monthly_saving = (portion_saved/10000) * monthly_salary 
        #bu değeri de şu anki birikimine eklemek lazım 
        current_savings += monthly_saving
        print(current_savings)
        if (i+1) %6 == 0:
            annual_salary += annual_salary*semi_annual_rise
    d+=1
    if d >= 60:
        print("There is nothing we can do")
        break
    if current_savings > int(total_cost*portion_down_payment):
        biggest = portion_saved
        portion_saved = (biggest+smallest)/2
    elif current_savings < int(total_cost*portion_down_payment):
        smallest = portion_saved
        portion_saved = (biggest+smallest)/2
    elif current_savings == int(total_cost*portion_down_payment):
        print(f"best saving rate : {portion_saved/10000}")
        print(f"steps in bisection search : {d}")
        break