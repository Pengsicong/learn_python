# 与python交互

* 点击查看[官方文档](http://api.mongodb.org/python/current/tutorial.html)
* 安装python包
    ```
    进入虚拟环境
    sudo pip install pymongo
    或源码安装
    python setup.py
    ```
* 引入包pymongo
    ```
    import pymongo
    ```
* 连接，创建客户端
    ```
    client=pymongo.MongoClient("localhost", 27017)
    ```
* 获得数据库test
    ```
    db=client.test
    ```
* 获得集合stu
    ```
    stu = db.stu
    ```
* 添加文档
    ```
    s1={name:'alex',age:18}
    s1_id = stu.insert_one(s1).inserted_id
    ```
* 查找一个文档
    ```
    s2=stu.find_one()
    ```
* 查找多个文档
    ```
    for cur in stu.find():
        print cur
    ```
 * 获取文档个数
    ```
    print stu.count()
    ```
* 排序
    ```
    单属性: cursor = stu.find().sort('age',1)
    多属性: cursor = stu.find().sort([('age',1), ('name',-1)])
    ```