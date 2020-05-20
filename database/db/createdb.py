#!/usr/bin/python3
import pymysql

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='root',
                             db='',
                             charset='utf8')

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (FIRST_NAME CHAR(20) NOT NULL,  
                                LAST_NAME CHAR(20), 
                                AGE INT, 
                                SEX CHAR(1), 
                                INCOME FLOAT )""" 

cursor.execute(sql)

connection.close()