def cel_to_fahren(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahren_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main(): #examples
    cel_temperatures = [20, 37, 67]
    for celsius in cel_temperatures:
        fahrenheit = cel_to_fahren(celsius)
        print(f"{celsius} C = {fahrenheit} F")
    
    print()

    fahren_temperatures = [30, 65, 89]
    for fahrenheit in fahren_temperatures:
        celsius = fahren_to_cel(fahrenheit)
        print(f"{fahrenheit} F = {celsius} C")

if __name__ == "__main__":
    main()
