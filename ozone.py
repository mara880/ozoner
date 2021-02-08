Molecule_mass = 1.964 # masa czasteczki w gramach na metr szescienny
Half_time = 2 # okres polrozpadu wzgledem godziny, dla bezpieczenstwa przyjeto 30 minut co jest rowne 2 stad T=2

# 1 gram/m3 ozonu to 509ppm
# 1 ppm to 1.964 mg/m3
# wzor: 24.45 * concentration[mg/m3] / molecular_weight[g/mol]
# M = 48 g/mol
# http://www.absoluteozone.com/ozone-conversions-and-equations.html
# https://trioxygen.com.pl/uploads/filemanager/materialy/artykul.pdf
# https://www.teesing.com/en/page/library/tools/ppm-mg3-converter

# kubatura pomieszczenia

def room_volume(length, width, height):
    volume = length*width*height
    return volume

# zdolności produkcyjne urządzenia w gramach na godzine oraz w ppm na minute

def production(power):
    # zdolność produkcji ozonu na podstawie mocy urządzenia
    # z kazdych 20W można wyprodukować 1 gram ozonu
    ozon = power / 20
    print("Zdolnosc wytwarzania ozonu na godzine: {0} g/m3".format(ozon))
    return ozon

def concentration(volume,ozon):
    concentration = (ozon*1000)/volume
    ppm = ((24.45 * concentration) / 48) / 60
    return ppm

# wymagany czas do ozonowania

def desinfection_time(ppm, mode_work, volume):
    print("Stezenie osiagniete po godzinie nie uwzgledniajace rozpadu: {0} ppm".format(round(((ppm*60)/volume), 2)))
    if mode_work == 1:
        conc = 0
        temp = ppm
        time = 0
        while conc <= 56:
            conc = conc + ppm
            time = time + 1
        print("Uruchom urządzenie na: ",time," minut")
    elif mode_work == 2:
        conc = 0
        temp = ppm
        time = 0
        while conc <= 12:
            conc = conc + ppm
            time = time + 1
        print("Uruchom urządzenie na: ", time, " minut")
    elif mode_work == 3:
        conc = 0
        time = 0
        while conc <= 4:
            conc = conc + ppm
            time = time + 1
        print("Uruchom urządzenie na: ",time, " minut")
    return time

# bezpieczny czas do wejscia do pomieszczenia

def safe_time(time,ppm):
    safe_time = (ppm*60) / time
    count = 0
    while safe_time > 0.1:
        safe_time = safe_time / Half_time
        count = count + 1
    print("Do pomieszczenia wejdz bezpiecznie po uplywie: {0} minut".format(count * 30))

# main

def main():
    print('''                **************************************************
        ***     Witaj w programie wspomagającym prace z ozonatorem     ***
                **************************************************''')
    print("Podaj wymagane dane.")
    length = int(input("Dlugosc pomieszczenia: "))
    width = int(input("Szerokosc pomieszczenia: "))
    height = int(input("Wysokosc pomieszczenia: "))
    power = int(input("Podaj moc ozonatora w Watach: "))
    mode_work = int(input('''Podaj tryb pracy:
         1. Ozonowanie popożarowe (42 ppm przez 45 minut)
         2. Ozonowanie ( 6ppm przez 30 minut)
         3. Ozonowanie ( 2ppm przez 30 minut)
        :--->>> '''))
    volume = room_volume(length,width,height)
    ozon = production(power)
    ppm = concentration(volume,ozon)
    time = desinfection_time(ppm,mode_work,volume)
    safe_time(time,ppm)
    #room_volume potrzebuje l w h i zwraca volume
    #production potrzebuje power i zwraca ozon
    #concentration potrzebuje volume i ozon i zwraca ppm
    #desinfection_tiem potrzebuje ozon, mode_work, volume i zwraca time
    #safe_time potrzebuje time i ppm

if __name__ == "__main__":
    main()