#-*-coidng:utf-8 -*-
#导入SQLite驱动：
import sqlite3
#连接到SQlite数据库
def insertSqlites(sql):
    #数据库文件是test.db，不存在，则自动创建
    conn = sqlite3.connect('test.db')
    #创建一个cursor：
    cursor = conn.cursor()
    #执行一条SQL语句：创建user表
    cursor.execute(sql)
    #插入一条记录：
    #通过rowcount获得插入的行数：
    print(cursor.rowcount) #reusult 1
    #关闭Cursor:
    cursor.close()
    #提交事务：
    conn.commit()
    #关闭connection：
    conn.close()

def selectsqliteTable():
    sql = "tables"
    # 数据库文件是test.db，不存在，则自动创建
    conn = sqlite3.connect('test.db')
    # 创建一个cursor：
    cursor = conn.cursor()
    # 执行一条SQL语句：创建user表
    cursor.execute(sql)
    print(cursor.fetchall())
    # 插入一条记录：
    # 通过rowcount获得插入的行数：
    print(cursor.rowcount)  # reusult 1
    # 关闭Cursor:
    cursor.close()
    # 提交事务：
    conn.commit()
    # 关闭connection：
    conn.close()

if __name__ == '__main__':
    selectsqliteTable()
    # sql = "create table person(name varchar(50), age int )"
    # insertSqlites(sql)
    # sql_list = ['create table person5(name varchar(50) ,age int ,e_mail varchar(50) PRIMARY KEY ,addr varchar(50) );', 'create table person1(name varchar(50) ,age int ,e_mail varchar(50) PRIMARY KEY ,addr varchar(50) );', 'create table person2(name varchar(50) ,age int ,e_mail varchar(50) PRIMARY KEY ,addr varchar(50) );']
    #
    # for sql in sql_list:
    #     print(sql)
    #     insertSqlites(sql)

