from dis import disco


def check_digit(msg):
    while True:
            v = input(msg)
            if v.isdigit():
                return v




def menu_page():
    print("---------------------------")
    print("| 1- Create Employee      |")
    print("| 2- Create Item          |")
    print("| 3- Make Purchase        |")
    print("| 4- All Employee Summary |")
    print("| 5- Exit                 |")
    print("---------------------------")


    

allitems = []
def create_item():
    while(True):
        item = []

        #check if item number is not empty and is digit
        it_id = check_digit("Item Number : ")
        if(allitems):
            #check if item with this id exist or not
            while(any(c == int(it_id) for r in allitems for c in r)):
                it_id = check_digit("Item Number: ")
            item.insert(0, int(it_id))
        else:
            item.insert(0, int(it_id))

        it_name = input("Item Name: ")
        while(it_name == ""):
            it_name = input("Item Name: ")
        item.insert(1, it_name)

        #check if item cost is not empty and is digit
        it_co = check_digit("Item Cost: ")
        item.insert(2, int(it_co))
        
        allitems.append(item)
        print("Item ID, Item Name, Item Cost")
        for oneItem in allitems:
            for j in oneItem:
                print(j , end=",   ")
            print()
        check = input("Another Item: ")
        if(check.lower() == "no"):
            print("Go to Menu? ")
            check = input("enter yes or no: ")
            if(check == "yes"):
                return "yes"
            elif(check == "no"):
                return "no"






allEmployees = []
def creat_emp():
    while(True):
        employee = []

        #check if employee id is not empty and is digit
        emp_id = check_digit("Employee ID: ")
        if(allEmployees):
            #check if employee with this id exist or not
            while(any(c == int(emp_id) for r in allEmployees for c in r)):
                emp_id = check_digit("Employee ID: ")
            employee.insert(0, int(emp_id))
        else:
            employee.insert(0, int(emp_id))


        emp_name = input("Employee Name: ")
        while(emp_name == ""):
            emp_name = input("Employee Name: ")
        employee.insert(1, emp_name)


        emp_type = input("Employee Type: ")
        #check if employee is hourly or manager
        while(emp_type != "hourly" and emp_type != "manager"):
            print("enter 'hourly' or 'manager'")
            emp_type = input("Employee Type: ")
        employee.insert(2, emp_type)


        #check if year of work is not empty and is digit
        emp_yw = check_digit("Years Worked: ")
        employee.insert(3, int(emp_yw))

        emp_tp = 0
        employee.insert(4, emp_tp)

        emp_td = 0
        employee.insert(5, emp_td)

        #check if discount number is not empty and is digit
        emp_dn = check_digit("Discount Number: ")
        #check if employee with this discount id exist or not
        while(any(c == int(emp_dn) for r in allEmployees for c in r)):
            emp_dn = check_digit("Discount Number: ")
        employee.insert(6, int(emp_dn))

        allEmployees.append(employee)
        # print(allEmployees)
        print("Employee ID, Employee Name, Employee Type, Years Worked, Total Purchased, Total Discounts, Employee Discount Number")
        for oneEmployee in allEmployees:
            for j in oneEmployee:
                print(j , end=",  ")
            print()
        check = input("Another Employee: ")
        if(check.lower() == "no"):
            print("Go to Menu? ")
            check = input("enter yes or no: ")
            if(check == "yes"):
                return "yes"
            elif(check == "no"):
                return "no"






def m_p():
    while(True):
        # item_found = False

        if(allEmployees):
            if(allitems):
                print("Item Number, Item Name, Item Cost")
                for item in allitems:
                    print(item[0],",", item[1],",", item[2])
                item_number = input("Input item number: ")
                for j in  allitems:
                    if str(j[0]) == item_number:
                        print("Employee ID, Employee Name, Employee Type, Years Worked, Total Purchased, Total Discounts, Employee Discount Number")
                        for oneEmployee in allEmployees:
                            for e in oneEmployee:
                                print(e , end=",  ")
                            print()
                        if(allEmployees):
                            employee_number = input("Input employee number: ")
                            for i in  allEmployees:
                                if str(i[0]) == employee_number:
                                    cost = j[2]
                                    if(i[3] >= 10):
                                        discount = 1/10 * cost
                                    else:
                                        discount = i[3]/100 * cost
                                    if(i[2] == "manager"):
                                        discount += 1/10 * cost
                                    elif(i[2] == "hourly"):
                                        discount += 1/50 * cost
                                    if(discount > 200):
                                        discount = 200
                                    i[4] += cost
                                    i[5] += discount
                                    print(i)
                                    check = input("Another Purchase: ")
                                    if(check.lower() == "no"):
                                        return "finish"
                                    else:
                                        return "agian"
                                
                            print("employee not found!")
                            return "employee not found"
                        else:
                            print("employee not found!")
                            return "employee not found"
                    
                print("item not found!")
                return "item not found"
            else:
                print("No items founds!")
                return "no items"
        else:
            print("No Employees founds!")
            return "no employees"
    
def show_all():
    if(allEmployees):
        print("Employee ID, Employee Name, Employee Type, Years Worked, Total Purchased, Total Discounts, Employee Discount Number")
        for a in allEmployees:
            print(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
        print("Go to Menu? ")
        check = input("enter yes or no: ")
        if(check == "yes"):
            return "yes"
        else:
            return "no"
    else:
        print("no summary")
        return "yes"