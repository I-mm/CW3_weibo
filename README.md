# Coursework 3: Weibo's data analysis

See this project at [CW3-weibo](https://github.com/I-mm/CW3-weibo). 

There are four csv files, follower_followee,post, user_post,weibo_user.and complete the following task: 

1. Design the database table based on the four files, and transform the data into the database. 
2. Describe the relationship of the tables, and draw the ER map.
3. Complete the following task.  
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

See [excelToDB.py](https://github.com/I-mm/CW2-product_info/blob/master/excelToDB.py). 

- Connect mysql database on remote server:

```python
db = pymysql.connect(host="39.105.165.114", user="root", password="zym2112!", use_unicode=True, charset="utf8")
# Not real password here.
```
- Create table product_info:

```sql
CREATE TABLE product_info (
                 barcode varchar(50) not null,
                 sellType  varchar(10),
                 wholesalePrice float ,
                 productName varchar(50),
                 referencePurchasePrice float,
                 retailPrice float ,
                 unit varchar(20),
                 specification varchar(20),
                 lowestRetailPrice float,
                 productNature varchar(15),
                 warrantyPeriod int,
                 distributionMethod varchar(10),
                 estimatedDaysOfUse int,
                 grossProfitMargin float )CHARSET=utf8 COLLATE=utf8_bin;
```

- Insert statement

```python
    sql = "insert into product_info(barcode, sellType, wholesalePrice, productName, referencePurchasePrice,retailPrice,unit,specification,lowestRetailPrice,productNature,warrantyPeriod,distributionMethod, estimatedDaysOfUse,grossProfitMargin) values ({},{},{},{},{},{},{},{},{},{},{},{},{},{});".format(
        barcode, sellType,
        wholesalePrice, productName,
        referencePurchasePrice,
        retailPrice, unit, specification,
        lowestRetailPrice, productNature,
        warrantyPeriod,
        distributionMethod,
        estimatedDaysOfUse,
        grossProfitMargin)

    try:
        cursor.execute(sql)
    except Exception as e:
        db.rollback()
        print(str(e))
        exit(-1)
    else:
        db.commit()  # Transaction submission
        print('Successful insert row ' + str(i) + '! ')
```

<br>

### Data Analysis
See [data analysis.ipynb](https://github.com/I-mm/CW2-product_info/blob/master/data_analysis.ipynb). 

<br>

### Contributor

[@赵屹铭](https://github.com/I-mm)

