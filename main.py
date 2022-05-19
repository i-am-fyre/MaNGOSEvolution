import os
import time
import glob
import fnmatch
import mysql.connector
from mysql.connector import Error

BACKUP_PATH = './backup/'
MIGRATE_DB_PATH = './migrate/'

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
        print("  4. M3 (4.3.4) to M4 (5.4.8)")
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
        elif choice == "4":
            print_banner()
            backup_db(3)
            migrate_db(3)
            break
        elif choice == "q":
            print("Bye!")
            break
        else:
            print("\n")
            print("Invalid choice!")    

def backup_db(version):
    global mysql_user
    global mysql_pass
    global mysql_host
    global mysql_port

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
    migrate_version = version + 1
    print("\n")
    print("Time to migrate the DB!")
    while True:
        choice = input(f"Do you have an existing M{migrate_version} database? [y/n]: ")
        if choice == "y": # This is not complete yet. Working on the 'n' selection first.
            print(f"M{migrate_version} database exists!")
        elif choice == "n":
            print(f"Creating M{migrate_version} database...")
            try:
                os.stat(MIGRATE_DB_PATH)
                print(f"Migration directory ({MIGRATE_DB_PATH}) already exists!")
            except:
                os.mkdir(MIGRATE_DB_PATH)
                print(f"Created migration directory ({MIGRATE_DB_PATH})!")
            
            # Pull database files from github.
            print("\n")
            print("Pulling database files from github...")
            if migrate_version == 1:
                version_text = "one"
            elif migrate_version == 2:
                version_text = "two"
            elif migrate_version == 3:
                version_text = "three"
            elif migrate_version == 4:
                version_text = "four"
            
            os.system(f"git clone https://github.com/mangos{version_text}/database {MIGRATE_DB_PATH}m{migrate_version}db")

            # Create database.
            print("\n")
            print("Creating character database...")
            DATETIME = time.strftime('%Y%m%d%H%M%S') # This is used temporarily during testing.
            new_char_db = f"character{migrate_version}_{DATETIME}" # This is used temporarily during testing.
            # This line should be used once testing is complete:
                # new_char_db = f"character{migrate_version}"

            print(f"Database: {new_char_db}")

            os.system(f"mysql -h{mysql_host} -P {mysql_port} -u {mysql_user} -p{mysql_pass} -e \"Create database {new_char_db}\"")

            # Generate Character Tables.
            for file in os.listdir(f"{MIGRATE_DB_PATH}m{migrate_version}db/Character/Setup"):
                if file.endswith("LoadDB.sql"):
                    file_path = os.path.join(f"{MIGRATE_DB_PATH}m{migrate_version}db/Character/Setup", file)
                    os.system(f"mysql -h{mysql_host} -P {mysql_port} -u {mysql_user} -p{mysql_pass} {new_char_db} < {file_path}")
                    print(f"Character tables imported.\n")


            # Perform Character Updates.
            print("Performing updates for character database...")
            for file in glob.glob(f'{MIGRATE_DB_PATH}m{migrate_version}db/Character/Updates/**/*.sql', recursive=True):
                print(f"Updating {file}...")
                os.system(f"mysql -h{mysql_host} -P {mysql_port} -u {mysql_user} -p{mysql_pass} {new_char_db} < {file}")
                print(f"File {file} imported!\n")
            break
        else:
            print("Invalid choice!")

print_banner()
print_menu()
