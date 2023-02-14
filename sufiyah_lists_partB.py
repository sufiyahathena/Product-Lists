#Sufiyah Sajan
#Lists

#Part B

product_names = ["hamburger", "cheeseburger", "small fries", "greek salad", "watermelon salad"]
product_costs = [0.99, 1.29, 1.49, 3.99, 5.99]
inventory = [10, 5, 20, 15, 8]

resume = 'yes'
cont = input("(s)earch for product, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
while resume == 'yes':
    if cont == 'q' or cont == 's' or cont == 'l' or cont == 'a' or cont == 'r' or cont == 'u' or cont == 'e':
        
        if cont == 'q':
            print("See you soon!")
            resume = 'no'
            break
        
        if cont == 's':
            name = str(input("Enter a product name: "))
            if name in product_names:
                print("We sell ", name, " at ", product_costs[product_names.index(name)], " per unit")
                print("We currently have ", inventory[product_names.index(name)], " in stock")
                print()
                cont = input("(s)earch for product, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")

            else:
                print("Sorry, we dont sell ", name)
                print()
                cont = input("(s)earch for product, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
                
        if cont == 'l':
            print()
            print("{0:<20s}{1:<15s}{2:>10s}".format("Product", "Price", "Quantity"))
            for i in range(len(product_names)):
                print("{0:<20s}{1:<10.2f}{2:10d}".format(product_names[i], product_costs[i], inventory[i]))
            print()
            cont = input("(s)earch for product, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
            
        if cont == 'a':
            print()
            newname = str(input("Enter a new product name: "))
            if newname in product_names:
                print("Sorry, we already sell that product. Try again.")
                print()
                newname = str(input("Enter a new product name: "))
            product_names.append(newname)
            
            newcost = float(input("Enter a product cost: "))
            if float(newcost) <= 0.0:
                print("Invalid cost. Try again.")
                print()
                newcost = str(input("Enter a product cost: "))
            product_costs.append(newcost)
                                
            newinventory = int(input("How many of these products do we have? "))
            if int(newinventory) <= 0:
                print("Invalid quantity. Try again.")
                print()
                newinventory = str(input("How many of these products do we have? "))
            inventory.append(newinventory)
                                
            print("Product added!")
            print()
            cont = input("(s)earch for product, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
            
        if cont == 'r':
            remove = input("Enter a product name: ")
            if remove in product_names:
                del product_costs[product_names.index(remove)]
                del inventory[product_names.index(remove)]
                product_names.remove(remove)
                print("Product removed!")
            else:
                print("Product doesn't exist. Can't remove.")
            print()
            cont = input("(s)earch for product, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")

        if cont == 'u':
            updatename = input("Enter a product name: ")
            if updatename in product_names:
                updating = input("What would you like to update? (n)ame, (c)ost or (q)uantity: ")
                if updating == 'n' or updating == 'c' or updating == 'q':
                
                    if updating == 'n':
                        updatingname = str(input("Enter a new name: "))
                        if updatingname in product_names:
                            print("Duplicate name!")
                            updatingname = str(input("Enter a new name: "))
                        product_names[product_names.index(updatename)] = updatingname
                        print("Product name has been updated")
                    
                    elif updating == 'c':
                        updatingcost = float(input("Enter a new cost: "))
                        if updatingcost <= 0.0:
                            print("Invalid cost!")
                            updatingcost = float(input("Enter a new cost: "))
                        product_costs[product_names.index(updatename)] = updatingcost
                        print("Product cost has been updated")

                    elif updating == 'q':
                        updatingquantity = int(input("Enter a new quantity: "))
                        if updatingquantity <= 0:
                            print("Invalid quantity!")
                            updatingquantity = int(input("Enter a new quantity: "))
                        inventory[product_names.index(updatename)] = updatingquantity
                        print("Product quantity has been updated")
                else:
                    print("Invalid option")

            else:
                print("Product doesn't exist. Can't update.")
            print()
            cont = input("(s)earch for product, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
            
        if cont == 'e':
            print()
            most = max(product_costs)
            print("Most expensive product: ", most, " (", product_names[product_costs.index(most)], ")")
            least = min(product_costs)
            print("Least expensive product: ", least, " (", product_names[product_costs.index(least)], ")")
            total = 0
            for items in product_costs:
                totalvalue = items * inventory[product_costs.index(items)]
                total += totalvalue
            print("Total value of all products: ", format(total, '.2f'))
            print()
            cont = input("(s)earch for product, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")

            
    else:
        print("Invalid option, try again")
        print()
        cont = input("(s)earch for product, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
