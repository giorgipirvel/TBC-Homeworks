speed=int(input("Enter the speed rate of the car: "))

if speed>=0: #აქ ზედა ზღვარის დაწესებაც შეიძლება
    if speed<30:
        print("SLOW")
    elif speed>120:
        print("VERY FAST")
    elif 60<speed<=120:
        print("FAST")
    elif 30<=speed<=60:
        print("MODERATE")
        
else: #არ შეიძლება სიჩქარე უარყოფითი იყოს
    print("Isn't possible")
    