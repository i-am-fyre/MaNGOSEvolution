# Here is the plan:
# 1. Get list of all tables in db1
# 2. Begin copying data from db1 to db2
# 3. Start with the easy ones, exact same tables/columns.




def migrate(conn, db1, db2):
    # Table: ahbot_category
    cursor = conn.cursor()

    # Get list of all tables in db1
    cursor.execute('show tables')
    tables = [row[0] for row in cursor.fetchall()]

    # Get list of all columns in db1
    for i in tables:
        print("Table: " + i)
        cursor.execute('show columns from ' + i)
        for j in cursor:
            print("> " + j[0])

def 