from datetime import date


#first function
def price(size, height, width, num_mow, trim):
    if (size == 1):
        price = 50
    elif (size == 2):
        price = 75
    elif (size == 3):
        price = 100
    else:
        price = size_price(height, width)

    price = price * num_mow
    if (trim == 1):
        price = price + 10
    return(price)

def size_price(height, width):
    price = width * height * (1/25)
    return price

def create_bill():
    h = 0
    w = 0
    print("1 = Small, 2 = Medium, 3 = Large, 0 = custom size \n")
    size = int(input("Type Yard size: \n"))

    if (size == 0):
        h = int(input("Enter yard height: \n"))
        height = h
        w = int(input("Enter yard Width: \n"))
        width = w

    print("How many mows?")
    print("Type 1 for single mow, 2 for double mow, etc...")
    num_mows = int(input("Enter an integer: \n"))

    print("Was there trimming?")
    trim = int(input("Type 1  for yes, 0 for no: \n"))

    return price(size, h, w, num_mows, trim)

def bill_output(price, num_mows, trim):
    curr_date = date.today()
    print("\n\n\n\n\n")
    print("BTDO Mowing\n--------------\nDate:",
           curr_date, "\nTotal: $", price,
           "\nThank you for your business!")
    return()






 





if __name__ == '__main__':
    print("Welcome to Auto Biller")
    cost = create_bill()
    bill_output(cost, 1, 1)
    