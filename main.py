from functions import *

def main():
    while(True):
        menu_page()
        num = input("Select a page: ")
        if(num=="1"):
            a = creat_emp()
            if (a=="no"):
                break
        if(num=="2"):
            a = create_item()   
            if (a=="no"):
                break
        if(num=="3"):
            a = m_p()
            while(a=="employee not found" or a=="item not found" or a=="agian"):
                a = m_p()
        if(num=="4"):
            a = show_all()
            if (a=="no"):
                break
        if(num=="5"):
            break
        

if __name__ == "__main__":
    main()
