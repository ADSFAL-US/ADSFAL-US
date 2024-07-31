


artc = input("стоимость протоартефактов: ")
dustc = input("стоимость аномальной пыли: ")
ar = 0

basear = ""
osear = ""
nobasear = ""
rarear = ""
legar = ""

for i in artc:

    if i == "/":
        ar += 1

    else:
        if ar == 0:
            basear += str(i)

        if ar == 1:
            nobasear += str(i)

        if ar == 2:
            osear += str(i)

        if ar == 3:
            rarear += str(i)

        if ar == 4:
            legar += str(i)




if rarear == "":
    rarear = "2500"

if legar == "":
    legar = "5000"

while True:
    
    
    count0 = input("белый: ")
    count1 = input("зеленый: ")
    count2 = input("синий: ")
    count3 = input("розовый: ")
    count4 = input("легендарный: ")
    count5 = input("пыль: ")


    endCoast = (int(count0)*int(basear))+(int(count1)*int(nobasear))+(int(count2)*int(osear))+(int(count3)*int(rarear))+(int(count4)*int(legar))
    endCoast += int(count5)*int(dustc)
    print(endCoast)