# -*- coding: utf-8 -*
# 将csv表2：post导入数据库表

import xlrd
import pymysql
import csv

fileName = "post"

with open("microblogPCU/" + fileName + ".csv", "r") as csvFile:
    reader = csv.reader(csvFile)

    # 连接数据库 并添加cursor游标
    db = pymysql.connect(host="localhost", user="root", password="zym2112!", use_unicode=True, charset="utf8")
    cursor = db.cursor()

    #  创建数据表的语句
    sql_createTb = "CREATE TABLE " + fileName + "(post_id varchar(40)," \
                                                "scratch_time varchar(50)," \
                                                "post_time varchar(50)," \
                                                "content varchar(1000)," \
                                                "iamge varchar(200)," \
                                                "poster varchar(50)," \
                                                "poster_id varchar(40)," \
                                                "poster_url varchar(200)," \
                                                "repost_num int," \
                                                "comment_num int," \
                                                "repost_post_id varchar(40))CHARSET=utf8 COLLATE=utf8_bin;"

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
            sql = "INSERT INTO " + fileName + " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

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
