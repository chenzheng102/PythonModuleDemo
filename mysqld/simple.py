#-*- coding:utf-8 -*-

def filed(data):
    #name type AUTO_INCREMENT UNSIGNED PRIMARY_key UNIQUE COMMENT
    filed_body = ""
    filed_body+=data["filed_name"]+" "
    filed_body+=data["type"]+" "
    if "AUTO_INCREMENT" in data:
        if data["AUTO_INCREMENT"] == True:
            filed_body+="AUTO_INCREMENT  "
    if "primary_key" in data:
        if data["primary_key"] == True:
            filed_body += "PRIMARY KEY "

    if "COMMENT" in data:
        if data["COMMENT"] != "":
            filed_body += "COMMENT '"+data["COMMENT"]+"'"

    filed_body += ","
    return filed_body


def product_sql(table_name,arr):
    sql = ""
    sql+="create table "+table_name
    fileds_data = ""
    for data in arr:
        fileds_data+=filed(data)
    sql+="({});".format(fileds_data[:-1])
    print(sql)
    return sql

def product_sqls(data):
    listd = []
    for k,v in data.items():
        sql = product_sql(k,v)
        listd.append(sql)
    print(listd)
    return listd



if __name__ == '__main__':


    arr = []
    #字段构造数据
    data = {"filed_name":"name","type":"varchar(50)","AUTO_INCREMENT":False,
            "primary_key":False,"COMMENT":"姓名"}
    filed_sql = filed(data)
    arr.append(data)
    print(filed_sql)
    data = {"filed_name":"age","type":"int","AUTO_INCREMENT":False,
            "primary_key":False,"COMMENT":"年龄"}

    filed_sql = filed(data)
    arr.append(data)

    print(filed_sql)
    #完整sql创建表方法
    product_sql("person",arr)

    #多表
    db_dabase = {
        "person":[
            {"filed_name": "name", "type": "varchar(50)", "AUTO_INCREMENT": False,
             "primary_key": False, "COMMENT": ""},
            {"filed_name": "age", "type": "int", "AUTO_INCREMENT": False,
             "primary_key": False, "COMMENT": ""},
            {"filed_name": "e_mail", "type": "varchar(50)", "AUTO_INCREMENT": False,
             "primary_key": True, "COMMENT": ""},
            {"filed_name": "addr", "type": "varchar(50)", "AUTO_INCREMENT": False,
             "primary_key": False, "COMMENT": ""}
        ],"person1":[
            {"filed_name": "name", "type": "varchar(50)", "AUTO_INCREMENT": False,
             "primary_key": False, "COMMENT": ""},
            {"filed_name": "age", "type": "int", "AUTO_INCREMENT": False,
             "primary_key": False, "COMMENT": ""},
            {"filed_name": "e_mail", "type": "varchar(50)", "AUTO_INCREMENT": False,
             "primary_key": True, "COMMENT": ""},
            {"filed_name": "addr", "type": "varchar(50)", "AUTO_INCREMENT": False,
             "primary_key": False, "COMMENT": ""}
        ],"person2":[
            {"filed_name": "name", "type": "varchar(50)", "AUTO_INCREMENT": False,
             "primary_key": False, "COMMENT": ""},
            {"filed_name": "age", "type": "int", "AUTO_INCREMENT": False,
             "primary_key": False, "COMMENT": ""},
            {"filed_name": "e_mail", "type": "varchar(50)", "AUTO_INCREMENT": False,
             "primary_key": True, "COMMENT": ""},
            {"filed_name": "addr", "type": "varchar(50)", "AUTO_INCREMENT": False,
             "primary_key": False, "COMMENT": ""}
        ]
    }
    product_sqls(db_dabase)