# Coursework 3: Weibo's data analysis

See this project at [CW3-weibo](https://github.com/I-mm/CW3-weibo). 

**Coursework requirements:** 

There are four csv files, *follower_followee*, *post*, *user_post*, *weibo_user*. And complete the following task: 

1.  Design the database table based on the four files, and transform the data into the database. (See at [csv1ToDB.py](https://github.com/I-mm/CW3_weibo/blob/master/csv1ToDB.py), [csv2ToDB.py](https://github.com/I-mm/CW3_weibo/blob/master/csv2ToDB.py), [csv3ToDB.py](https://github.com/I-mm/CW3_weibo/blob/master/csv3ToDB.py), [csv4ToDB.py](https://github.com/I-mm/CW3_weibo/blob/master/csv4ToDB.py). )
2.  Describe the relationship of the tables, and draw the ER map. (See at [ER map](https://github.com/I-mm/CW3_weibo#er_map))
3.  Complete the following task. (See at [data_analysis.ipynb](https://github.com/I-mm/CW3_weibo/blob/master/data_analysis.ipynb).)
   - Find the content posted by the people who have more than 1000 followers
   - Research the law and features of the content which post_number is more than 5.
   - Please find the spammer and advertiser.
   - Finding zombie fans or followers in the table. 
   - Draw the relationship map of the user.

<br>

### Dependencies 

```
conda env create -f environment.yml
```

<br>

### Data Input (with preliminary screening of data)

See  [csv1ToDB.py](https://github.com/I-mm/CW3_weibo/blob/master/csv1ToDB.py), [csv2ToDB.py](https://github.com/I-mm/CW3_weibo/blob/master/csv2ToDB.py), [csv3ToDB.py](https://github.com/I-mm/CW3_weibo/blob/master/csv3ToDB.py), [csv4ToDB.py](https://github.com/I-mm/CW3_weibo/blob/master/csv4ToDB.py). 

- Connect mysql database on remote server:

```python
db = pymysql.connect(host="39.105.165.114", user="root", password="zym2112!", use_unicode=True, charset="utf8")
# Not real password here.
```
- Create table *follower_followee*:

```python
sql_createTb = "CREATE TABLE follower_followee(t_id varchar(20) primary key," \
                                            "follower varchar(50)," \
                                            "follower_id varchar(40) not null," \
                                            "followee varchar(50)," \
                                            "followee_id varchar(40) not null," \
                                            "guanzhu int," \
                                            "fensi int," \
                                            "post_num int," \
                                            "gender varchar(20)," \
                                            "first_or_last varchar(20))CHARSET=utf8 COLLATE=utf8_bin;"
```

- Create table *post*:

```python
sql_createTb = "CREATE TABLE post(post_id varchar(40)," \
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
```
- Create table *user_post*:

```python
sql_createTb = "CREATE TABLE user_post(post_id varchar(50)," \
                                                "post_time varchar(50)," \
                                                "content varchar(1000)," \
                                                "poster_id varchar(50)," \
                                                "poster_url varchar(200)," \
                                                "repost_num int," \
                                                "comment_num int," \
                                                "repost_post_id varchar(50)," \
                                                "inner_flag varchar(20))CHARSET=utf8 COLLATE=utf8_bin;"
```
- Create table *weibo_user*:

```python
sql_createTb = "CREATE TABLE weibo_user(user_id varchar(40) primary key," \
                                                "user_name varchar(50)," \
                                                "user_image varchar(200)," \
                                                "gender varchar(20)," \
                                                "class int," \
                                                "message varchar(300)," \
                                                "post_num int," \
                                                "follower_num int," \
                                                "followee_num int," \
                                                "is_spammer int)CHARSET=utf8 COLLATE=utf8_bin;"
```
- Insert operation *(Here we take the example of table **follower_followee**)*

```python
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
```

<br>

### ER map

![ER_map.svg](https://github.com/I-mm/CW3_weibo/blob/master/dataAnalysis_output/ER_map.svg)

<br>

### 5 Tasks and Data analysis

See [data_analysis.ipynb](https://github.com/I-mm/CW3_weibo/blob/master/data_analysis.ipynb).

Also, in folder [dataAnalysis_output](https://github.com/I-mm/CW3_weibo/tree/master/dataAnalysis_output), there are complete data obtained from the sql statements in [data_analysis.ipynb](https://github.com/I-mm/CW3_weibo/blob/master/data_analysis.ipynb). 

Collection of sql statements: [cw3_weibo.sql](https://github.com/I-mm/CW3_weibo/blob/master/cw3_weibo.sql). 

<br>

### Contributor

[@赵屹铭](https://github.com/I-mm)

