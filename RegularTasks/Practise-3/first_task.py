import pymysql


def main():
    db = pymysql.connect("localhost", "root", "password", "python_task")
    cursor = db.cursor()
    cursor.execute("SELECT item FROM python_task.customer_item_registration")
    data = cursor.fetchall()
    for row in data:
        kek=row[0]
        print(kek)
    # print(data)
    db.close()


# disconnect from server

if __name__ == '__main__':
    main()
