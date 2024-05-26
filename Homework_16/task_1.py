def average_temperature(temperature):
    total = sum(temperature)
    number_of_temp = len(temperature)
    average = total / number_of_temp
    return average

def main():
    temperature = [22,25,19,23,25,26,23]
    average_temp = average_temperature(temperature)
    print("Average temperature:",average_temp)

if __name__ == "__main__":
    main()
