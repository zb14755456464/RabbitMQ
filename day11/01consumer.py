zhangbiao = "在黑暗中的每一次跳跃都是成长"

import pika,time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello',durable=True) # 消息持久话，durable = true 关机没事


def callback(ch, method, properties, body):
   #ch 管道的名字
    print(ch,method,properties)
    #time.sleep(30)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag) # 客户端要手动的向服务器确认处理完了

channel.basic_qos(prefetch_count=1)#消息公平分发，如果当前的客户端还有消息，没处理完，就不会发给他，发给空闲的
channel.basic_consume(#消费信息
                    callback,#如果收到消息，就调用这个函数来处理消息
                      queue='hello',
                     # no_ack=True 客户端没处理完，会传给下一个客户端，默认会断掉

                       )

print(' [*] Waiting for messages. To exit press ')
channel.start_consuming()
