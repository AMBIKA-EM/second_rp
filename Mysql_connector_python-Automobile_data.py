import pandas as pd
import mysql.connector as msql
from mysql.connector import Error





def add_automobile():
    df = pd.read_csv('Automobile_data.csv',
                     usecols=['company', 'body_style', 'wheel_base', 'length', 'engine_type', 'num_of_cylinders',
                              'horsepower', 'average_mileage', 'price'])
   
    try:
        conn = msql.connect(host="localhost",
                           database='Automobile_data', user='root',
                            password='sdmin')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.execute('DROP TABLE IF EXISTS automobile;')
            print('Creating table....')
            cursor.execute(
                "CREATE TABLE automobile (company CHAR(100),body_style CHAR(100),wheel_base FLOAT(6,2), length FLOAT(6,2),engine_type CHAR(100),num_of_cylinders CHAR(100),horsepower FLOAT(6,2), average_mileage FLOAT(6,2),price FLOAT(8,2))")
            print("automobile table is created....")
            for i, row in df.iterrows():
                sql = "INSERT INTO Automobile_data.automobile VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, tuple(row))
                print("Record inserted")
                conn.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    ### Approach 2 ends ###################


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_automobile()
