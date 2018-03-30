import threading

class IoT4_0(threading.Thread):
         def run(self):
                  for _ in range(10):
                           print(threading.currentThread().getName())

send = IoT4_0(name='Sending out messages')
receive = IoT4_0(name='Receiving messages')       

send.start()
receive.start()
