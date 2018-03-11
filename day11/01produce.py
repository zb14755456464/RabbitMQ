zhangbiao = "在黑暗中的每一次跳跃都是成长"

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))#建立基本的socket
channel = connection.channel()#开通一个管道

# 声明queue，queue的名字叫做hello
channel.queue_declare(queue='hello',durable=True)


channel.basic_publish(exchange='',
                      routing_key='hello',#queue的名字
                      body='Hello World!123',
                      #消息持久化
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent 'Hello World!'")
connection.close()