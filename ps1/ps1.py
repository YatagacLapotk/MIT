annual_salary = float(input("Your salary : "))
#kişi yıllık maaşını girdi
total_cost = float(input("Dream house price : "))
#almak istediği evin fiyatını girdi
portion_saved = float(input("Your portion : "))
#ayırmak istediği parayı girdi
semi_annual_rise = float(input("Your annual rise : "))
#yarıyılda bir artaacak maaş miktarı
current_savings = 0
#şu anki ayırdığı para
portion_down_payment = 0.25
#ödemes gereken en az para
r = 0.04
#ayırdığı paranın ona geri dönüşü
#her yılı sırasıyla değerlendirmek için while döngüsü açtım
d = 0
while True :
    #kişinin birikiminin geri dönüşü
    current_savings += (current_savings*r/12)
    #kişinin maaşının aylık değerinin bir kısmını ayıracak 
    monthly_salary = annual_salary/12
    monthly_saving = portion_saved * monthly_salary 
    #bu değeri de şu anki birikimine eklemek lazım 
    current_savings += monthly_saving
    d+=1
    if d %6 == 0:
        annual_salary += annual_salary*semi_annual_rise
    if current_savings >= total_cost*portion_down_payment:
        print(f"Number of months : {d}")
        break 
    