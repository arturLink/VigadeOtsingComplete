print("ИГРЫ С ЧИСЛАМИ")
while 1:
    try:
        a = abs(int(input("Введите целое число => ")))
        break
    except ValueError:
         print("Это не целое число")
#vodim 4islo eshe proverka
if a==0:#esli 0 to vivod na ekran
    print("Нет смысла ничего делать с нулём")
else:
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    c=b=a#prirovnjat peremen
    paaris=0#s4etchiki
    paaritu=0
    while b > 0:
        if b % 2==0:#proverka 4et li 4islo
            paaris+=1
        else:#v drugih slu4ajah ne 4et tak 4to + v s4etchik
            paaritu+=1
        b = b // 10
    
    print("Чётных цифр:",paaris)
    print("Нечётных цифр:",paaritu)
#skok 4et i ne 4et
    print("Переворачиваем введённое число")
    b=0
    while a > 0:
        number=a % 10
        a=a // 10
        b=b * 10
        b+=number
    print("Перевёрнутое число", b)
#perevorot 4isla
    print("Проверяем гипотезу Сиракуз")
    if c%2==0:#esli 4et to vivod 4isla
        print(c," - чётное число. Делим на 2.")
    else:#v drugih slu4ajah ne 4et 
        print(c," - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c!= 1:#tolko esli c=1 vipolnajatsa vse 4to nishe
        if c%2==0:#4et ili ne 4et
            c=c / 2#delit esli 4et
        else:#esli ne 4et sdelat 4et
            c = (3*c + 1) / 2
    print(c, end=" ")
    print("Гипотеза верна")
#proverjaem gipotezu