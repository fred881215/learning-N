#!/usr/bin/python3
import pymysql
import mysql.connector

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='000000')

cursor = connection.cursor()

# Create db
cursor.execute("CREATE DATABASE ardudb")

# Create table
cursor.execute("CREATE TABLE users (name VARCHAR(255), age INTEGER(99), user_id INTEGER AUTO_INCREMENT PRIMARY Key)")

connection.close()

