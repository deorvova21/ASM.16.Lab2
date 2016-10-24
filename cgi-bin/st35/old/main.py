from .menu import *

def main():
    my_menu = MENU()
    try:
        while True:



            print(my_menu)
            my_menu(input())
            input()
    except:
        print("close")
    return

if __name__ == '__main__':
    main()




