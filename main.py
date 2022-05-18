import os
import time
import mysql.connector
from mysql.connector import Error

BACKUP_PATH = './backup/'


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
        print("  2. M1 (2.4.3) to M2 (3.3.5a)")
        print("  3. M2 (3.3.5a) to M3 (4.3.4)")
        print("  q. Quit")
        print("\n")
        choice = input("Enter choice: ")
        if choice == "1":
            print_banner()
            backup_db(0)
            migrate_db(0)
            break
        elif choice == "2":
            print_banner()
            backup_db(1)
            migrate_db(1)
            break
        elif choice == "3":
            print_banner()
            backup_db(2)
            migrate_db(2)
            break
        elif choice == "q":
            print("Bye!")
            break
        else:
            print("\n")
            print("Invalid choice!")    

def backup_db(version):
    mysql_user = input("Enter MySQL username [default: mangos]: ") or "mangos"
    mysql_pass = input("Enter MySQL password [default: mangos]: ") or "mangos"
    mysql_host = input("Enter MySQL host [default: 127.0.0.1]: ") or "127.0.0.1"
    mysql_port = int(input("Enter MySQL port [default: 3306]: ") or "3306")
    db_mangosd_name = input(f"Enter mangosd/world database name [default: mangos{version}]: ") or f"mangos{version}"
    db_characters_name = input(f"Enter characters database name [default: character{version}]: ") or f"character{version}"

    # Test database connections before backing up.
    success = 0
    for db_x in [db_mangosd_name, db_characters_name]:
        conn = None
        try:
            conn = mysql.connector.connect(host=mysql_host, port=mysql_port, user=mysql_user, passwd=mysql_pass, db=db_x)
            
            if conn.is_connected():
                print(f"Connected to database ({db_x})!")
                success+=1
        except:
            print(f"Error connecting to database ({db_x})!")
        finally:
            if conn is not None and conn.is_connected():
                conn.close()

    # only proceed below if both databases connected above.
    if success == 2:
        try:
            os.stat(BACKUP_PATH)
            print(f"Backup folder ({BACKUP_PATH}) exists!")
        except:
            os.mkdir(BACKUP_PATH)
            print(f"Created backup directory ({BACKUP_PATH})!")

        print("\n")
        print(f"Backing up M{version} databases into {BACKUP_PATH}")
        print("\n")
        DATETIME = time.strftime('%Y%m%d-%H%M%S')
        for db_x in [db_mangosd_name, db_characters_name]:
            BACKUP_FILE = f"{BACKUP_PATH}{db_x}-{DATETIME}.sql"
            print(f"Backing up {db_x}...")
            os.system(f"mysqldump -h {mysql_host} -P {mysql_port} -u {mysql_user} -p{mysql_pass} {db_x} > {BACKUP_FILE}")
            try: 
                os.stat(f"{BACKUP_FILE}")
                if (os.path.getsize(f"{BACKUP_FILE}") > 0):
                    print(f"Backup of {db_x} successful!")
                else:
                    print(f"Backup of {db_x} failed!")
                    os.remove(f"{BACKUP_FILE}")
            except:
                print(f"Error backing up {db_x}!")
    else:
        print("\n")
        print("Unable to connect to one or more databases! Please confirm your credentials and ensure that the user is authorized to access the databases.")

def migrate_db(version):
    print("Time to migrate the DB!")

print_banner()
print_menu()
