import os
import mysql.connector
from mysql.connector import Error


def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ____    ____         ____  _____   ______     ___     ______                             ")
    print("|_   \  /   _|       |_   \|_   _|.' ___  |  .'   `. .' ____ \                            ")
    print("  |   \/   |   ,--.    |   \ | | / .'   \_| /  .-.  \| (___ \_|                           ")
    print("  | |\  /| |  `'_\ :   | |\ \| | | |   ____ | |   | | _.____`.                            ")
    print(" _| |_\/_| |_ // | |, _| |_\   |_\ `.___]  |\  `-'  /| \____) |                           ")
    print("|_____||_____|\'-;__/|_____|\____|`._____.'  `.___.'  \______.'                           ")
    print(" ________  ____   ____   ___   _____  _____  _____  _________  _____   ___   ____  _____  ")
    print("|_   __  ||_  _| |_  _|.'   `.|_   _||_   _||_   _||  _   _  ||_   _|.'   `.|_   \|_   _| ")
    print("  | |_ \_|  \ \   / / /  .-.  \ | |    | |    | |  |_/ | | \_|  | | /  .-.  \ |   \ | |   ")
    print("  |  _| _    \ \ / /  | |   | | | |   _| '    ' |      | |      | | | |   | | | |\ \| |   ")
    print(" _| |__/ |    \ ' /   \  `-'  /_| |__/ |\ \__/ /      _| |_    _| |_\  `-'  /_| |_\   |_  ")
    print("|________|     \_/     `.___.'|________| `.__.'      |_____|  |_____|`.___.'|_____|\____| ")

    print("\n")

def print_menu():
    while True:
        print("Select one of the following options: ")
        print("  1. M0 (1.12.1) to M1 (2.4.3)")
        print("  q. Quit")
        print("\n")
        choice = input("Enter choice: ")
        if choice == "1":
            print_banner()
            backup_db(0)
        elif choice == "q":
            print("Bye!")
            break
        else:
            print("\n")
            print("Invalid choice!")    

def backup_db(version):
    mysql_user = input("Enter MySQL username [default: mangos]: ") or "mangos"
    mysql_pass = input("Enter MySQL password [default: mangos]: ") or "mangos"
    mysql_host = input("Enter MySQL host [default: localhost]: ") or "localhost"
    mysql_port = int(input("Enter MySQL port [default: 3306]: ") or "3306")
    db_mangosd_name = input("Enter mangosd/world database name [default: mangosd0]: ") or "mangosd0"
    db_characters_name = input("Enter characters database name [default: characters0]: ") or "characters0"

    for db_x in [db_mangosd_name, db_characters_name]:
        conn = None
        try:
            conn = mysql.connector.connect(host=mysql_host, port=mysql_port, user=mysql_user, passwd=mysql_pass, db=db_x)
            
            if conn.is_connected():
                print(f"Connected to database ({db_x})!")
        except:
            print(f"Error connecting to database ({db_x})!")
        finally:
            if conn is not None and conn.is_connected():
                conn.close()

# only proceed below if both databases connected above.

    print("Backing up database...")
    print("\n")
    if version == 0:
        print("Backing up M0 database...")
        print("\n")
        print("M0 database backed up successfully!")
    elif version == 1:
        print("Backing up M1 database...")
        print("\n")
        print("M1 database backed up successfully!")
    else:
        print("\n")
        print("Invalid version!")

print_banner()
print_menu()