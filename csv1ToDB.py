# -*- coding: utf-8 -*
# 将csv表1：follower_followee导入数据库表

import xlrd
import pymysql
import csv

fileName = "follower_followee"

with open("microblogPCU/" + fileName + ".csv", "r") as csvFile:
    reader = csv.reader(csvFile)

    # 连接数据库 并添加cursor游标
    db = pymysql.connect(host="localhost", user="root", password="zym2112!", use_unicode=True, charset="utf8")
    cursor = db.cursor()

    #  创建数据表的语句
    sql_createTb = "CREATE TABLE " + fileName + "(t_id varchar(20) primary key," \
                                                "follower varchar(50)," \
                                                "follower_id varchar(40) not null," \
                                                "followee varchar(50)," \
                                                "followee_id varchar(40) not null," \
                                                "guanzhu int," \
                                                "fensi int," \
                                                "post_num int," \
                                                "gender varchar(20)," \
                                                "first_or_last varchar(20))CHARSET=utf8 COLLATE=utf8_bin;"

    cursor.execute("USE cw3_weibo;")
    try:
        cursor.execute("DROP TABLE " + fileName + ";")
        cursor.execute(sql_createTb)
    except Exception as e:
        db.rollback()
        print(str(e))
        exit(-1)
    else:
        print("The original table " + fileName + " has been droped! ")
        print("New table " + fileName + " has been created!")

    line_num = 1
    for row in reader:
        if line_num == 1:
            pass
        else:
            if (row[5] == ''):
                row[5] = 0
            if (row[6] == ''):
                row[6] = 0
            if (row[7] == ''):
                row[7] = 0

            sql = "INSERT INTO " + fileName + " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            try:
                cursor.execute(sql, row)
            except Exception as e:
                db.rollback()
                print(str(e))
                exit(-1)
            else:
                db.commit()  # Transaction submission
                print('Successful insert row ' + str(line_num - 1) + '! ')
        line_num += 1

print("============Finished============")
db.close()
cursor.close()
