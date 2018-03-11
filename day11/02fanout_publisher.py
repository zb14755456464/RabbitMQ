zhangbiao = "在黑暗中的每一次跳跃都是成长"
import pika


# 类似于一个广播，关了就收不到了，开了才会收到
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()
# 发布方没声明queue，只要exchange

channel.exchange_declare(exchange='logs',  # 绑定这个的都会受到
                         type='fanout')

message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
