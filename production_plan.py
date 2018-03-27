# make a production list
product_list = []

# print out instructions on how to use the app
print("Enter products that you are running today: ")
print("Enter 'Enter' to stop adding products.")

while True:
    # ask for new products
    new_product = input("> ")
    new_product = new_product.lower()
    # App should stop listing when all products are added by using "DONE"
    if new_product == "enter":
        break
    # add new items to our list
    product_list.append(new_product)
# enter product quantity or required production quantity
try:
    product_quantity = int(input("Enter order quantity > "))
    # when user eneters a word (str) instead of a number (int), remind the user to enter a number
except ValueError:
    print("ERROR! "
          "Please eneter a number!")

def material_plan():

# select work station with options; extrusion / printing / slitting
        work_station = input("Whats your work station> ")
        if work_station == "extrusion":
        # print the product name and production quantity factoring in 4% production waste
            print("You are extruding {}{} kg.".format(product_list,product_quantity * 1.04))
            # print required materials for the ordered quantity that is:
            #  4 cores / 1000kg
            #  Plastic LDPE required
            print("You require {} cores, {} kgs LDPE raw material".format(product_quantity/250,product_quantity*1.1))
            # production capacity of 400kg / hour
            print("You will complete in {} hours!".format(product_quantity/400))

        elif work_station == "printing":
            # print the product name and production quantity factoring in 2.5% start up waste
            print("You are printing {}{}.".format(product_list,product_quantity * 1.025))
            # raw material required printing inks, paper cores (4 /1000kg)
            print("You require {} cores, {} kgs ink ".format(product_quantity / 250, product_quantity * 0.01))
            # production capacity of 1000kg / hour
            print("You will complete in {} hours!".format(product_quantity / 1000))

        elif work_station == "slitting":
            # print the product name and production quantity factoring in 5% trim waste
            print("You are slitting {}{}.".format(product_list,product_quantity * 1.05))
            # raw material required paper cores (40 /1000kg)
            print("You require {} cores. ".format(product_quantity / 25))
            # production capacity of 1000kg / hour
            print("You will complete in {} hours!".format(product_quantity / 350))

    # Remind the user to enter a valid work station that is known by the app.
        else:
            print("Please enter a work station among: extrusion/ printing/ slitting!")


# print out the plan
print("Your production plan consists of the following products:")
for product in product_list:
    print(product)
print(material_plan())



