# coding=utf-8
# Created by: dong4j.
# Date: 2016-12-10.
# Time: 14:54.
# Description: 

import MySQLdb


def connect_mysql():
    db = MySQLdb.connect("localhost", "root", "bVWrFXDqfhKV*xRMzsag8BGb", "spider")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取一条数据库。
    data = cursor.fetchone()
    print "Database version : %s " % data
    # 关闭数据库连接
    db.close()

def create_table():
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "bVWrFXDqfhKV*xRMzsag8BGb", "spider")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 如果数据表已经存在使用 execute() 方法删除表。
    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # 创建数据表SQL语句
    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,
             SEX CHAR(1),
             INCOME FLOAT )"""
    cursor.execute(sql)

def insert_db():
    db = MySQLdb.connect("localhost", "root", "bVWrFXDqfhKV*xRMzsag8BGb", "spider")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
    #          LAST_NAME, AGE, SEX, INCOME)
    #          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
           LAST_NAME, AGE, SEX, INCOME) \
           VALUES ('%s', '%s', '%d', '%c', '%d' )" % ('Mac', 'dong4j', 20, 'M', 2000)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    # 关闭数据库连接
    db.close()

if __name__ == '__main__':
    connect_mysql()
    # create_table()
    insert_db()