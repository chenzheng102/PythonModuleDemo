#-*- coding:utf-8 -*-

def filed(data):
    #name type AUTO_INCREMENT UNSIGNED PRIMARY_key UNIQUE COMMENT
    filed_body = ""
    filed_body+=data["filed_name"]+" "
    filed_body+=data["filed_type"]

    if "size" in data:
        if data["size"] != 0:
            filed_body += "({}) ".format(data["size"])
    filed_body+=" "
    if "AUTO_INCREMENT" in data:
        if data["AUTO_INCREMENT"] == True:
            filed_body+="AUTO_INCREMENT  "
    if "primary_key" in data:
        if data["primary_key"] == True:
            filed_body += "PRIMARY KEY "
    if data["primary_key"] == True:
        filed_body += "PRIMARY KEY "
    if data["null"] == True:
        filed_body += "not null "
    if data["union"] == True:
        filed_body += "union "

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

    #仅考虑正常字段，未考虑唯一索引
    arr = []
    #字段构造数据
    data = {"filed_name":"name","filed_type":"varchar","size":300,"AUTO_INCREMENT":False,
            "primary_key":False,"null":"null","COMMENT":"姓名","union":False}
    filed_sql = filed(data)
    print(filed_sql)
    arr.append(data)
    print(filed_sql)
    data = {"filed_name":"age","filed_type":"int","size":20,"AUTO_INCREMENT":False,
            "primary_key":False,"null":"null","COMMENT":"姓名","union":False}

    filed_sql = filed(data)
    arr.append(data)
    #
    print(filed_sql)
    # #完整sql创建表方法
    product_sql("person",arr)
    #
    # #多表
    db_dabase = {
        "person":[
            {"filed_name": "name", "filed_type": "varchar", "size": 100, "AUTO_INCREMENT": False,
             "primary_key": False, "null": "null", "COMMENT": "姓名", "union": False},
            {"filed_name": "age", "filed_type": "int", "size": 20, "AUTO_INCREMENT": False,
             "primary_key": False, "null": "null", "COMMENT": "姓名", "union": False},
            {"filed_name": "email", "filed_type": "varchar", "size": 100, "AUTO_INCREMENT": False,
             "primary_key": False, "null": "null", "COMMENT": "姓名", "union": False},
            {"filed_name": "addr", "filed_type": "varchar", "size": 100, "AUTO_INCREMENT": False,
             "primary_key": False, "null": "null", "COMMENT": "姓名", "union": False}
        ]
    }
    product_sqls(db_dabase)