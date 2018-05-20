# 交互代码

* 引入模块
    ```
    import redis
    ```
* 连接
    ```
    try:
        r=redis.StrictRedis(host='localhost',port=6379)
    except Exception,e:
        print e.message
    ```
* 方式一：根据数据类型的不同，调用相应的方法，完成读写
    ```
    r.set('name','hello')
    r.get('name')
    ```
* 方式二：pipline 缓冲多条命令，然后一次性执行，减少服务器-客户端之间TCP数据库包，从而提高效率
    ```
    pipe = r.pipeline()
    pipe.set('name', 'world')
    pipe.get('name')
    pipe.execute()
    ```
* 封装
    ```
    import redis
    class RedisHelper():
        def __init__(self,host='localhost',port=6379):
            self.__redis = redis.StrictRedis(host, port)
        def get(self,key):
            if self.__redis.exists(key):
                return self.__redis.get(key)
            else:
                return ""
        def set(self,key,value):
            self.__redis.set(key,value)
        ```