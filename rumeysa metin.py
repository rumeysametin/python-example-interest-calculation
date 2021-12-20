print("""
    ......................................................
    .*.*.*.*.*Welcome to the Interest Calculator.*.*.*.*.*
    ......................................................
""")

#kullacıdan isim, faiz oranı, anapara, en fazla yıl ve ayı en sonunda da yineleme ayı değerlerini ister ve alır.
name = input("please enter your name: ")               #kullanıcıdan string değer girmesi istenir.   
rate = float(input("annual interest rate: "))          #kullanıcıdan kesirli sayı girilmesi istenir.
loan_amount = float(input("loan amount: "))            #kullanıcıdan kesirli sayı girilmesi istenir.
max_year = int(input("max year: "))                    #kullanıcıdan tam sayı girilmesi istenir.
max_month = int(input("max month: "))                  #kullanıcıdan tam sayı girilmesi istenir.
iteration = int(input("iteration interval(month): "))  #kullanıcıdan tam sayı girilmesi istenir.

#bu fonksiyon, ay olarak verilen süreyi, yıl ve aya parçalar.
def print_duration(month):
     year = month // 12                         #girilen ayın içindeki tam yılları hesaplar.
     split_month = month - (12 * year)          #girilen aydan tam yılları çıkarır ve kalan ayları hesaplar.
     print("year: {year}, month:{month}".format(year=year,month=split_month)) #parçalanmış tam yılları ve kalan ayları yazdırır. 

#fonksiyon, para miktarı float girildiğinde az önemli olan kısmı kaldırarak tek bir ondalık basamaklı sayı olarak yazdırır.   
def print_money(money):
    print("{money} $".format(money=round(money,1))) #round fonksiyonunu kesirli sayılarda istenen basamakta sayıların girilmesini sağlar. Hesaplanan parayı $ sembolüyle yazdırır.

#fonksiyon, toplam faizi hesaplar. Raporu kim için yazdırdığını, süreyi 1.fonksiyondaki formatta ve son olarak para tutarını 2.fonksiyondaki 
#formatta sırasıyla toplam ve aylık ödeme olarak çağırır.
def print_entry(loan_amount, rate, month):
    total_interest =  (loan_amount/100) * (rate/12) * month  #toplam faiz hesaplanır.
    amount = loan_amount + total_interest                    #anapara ile toplam faiz toplanır, faizli para hesaplanır.
    print("----------------------")                          #yineleme aylarını birbirinden ayırmak, daha iyi bir görüntü almak için ekrana ---------------------- yazar.
    print_duration(month)                                    #1.fonksiyonda süreyi çağırır.
    print("Total Payment:")                                  #ekrana Total Payment: yazar.
    print_money(amount)                                      #2.fonksiyonda, hesaplanan faizli parayı çağırır. 
    print("Monthly Payment:")                                #ekrana Monthly Payment: yazar.
    monthly_payment = amount / month                         #faizli para istenen aya bölünür.
    print_money(monthly_payment)                             #2.fonksiyonda, istenen aya göre aylık ödemeyi çağırır.
    print("----------------------")                          #yineleme aylarını birbirinden ayırmak, daha iyi bir görüntü almak için ekrana ---------------------- yazar.
print ("Report for", name)                                   #rapor sahibinin ismini yazdırır.

#fonksiyon tüm raporu yazdırır. Parametre iteration(ay olarak), iki ardısık girişin süreleri arasındaki farktır. Rapor, maks_yıl ve maks_ay  
#parametreleri tarafından belirtilen süreyi net ay olarak hesaplar hesapladığı sürenin bir fazlasına kadar olan girdileri görüntüler.
def print_full_report(loan_amount, rate, max_year, max_month, iteration):
    duration = (max_year * 12) + max_month                              #aralığı ay cinsinden hesaplamak için girilen en fazla yıl aya dönüştürülür ve en fazla ayla toplanır.
    for month_iteration in range(iteration, duration + 1 , iteration):  #range fonksiyonu başlangıç ve bitiş değerlerinin arasındaki değerleri istenen tekrara göre dizi döner. Bitiş değerinden bir öncesinde durur.
        print_entry(loan_amount, rate, month_iteration)                 #3.fonksiyonda, girilen değerler çağrılır.

print_full_report(loan_amount, rate, max_year, max_month, iteration)    #4.fonksiyonu çağırır.