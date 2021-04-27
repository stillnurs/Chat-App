from client import Client
import time
from threading import Thread

c1 = Client('Steve')
c2 = Client('Joe')


def update_messages():
    """
    updates the local list of messages
    :return: None
    """
    msgs = []
    run = True
    while run:
        time.sleep(0.1)  # update ever 1/10 of a second
        new_messages = c1.get_messages()  # get any messages from client
        msgs.extend(c1.get_messages())  # add to local list of messages

        for msg in new_messages:  # display new messages
            print(msg)
            if msg == '{quit}':
                run = False
                break


Thread(target=update_messages).start()

c1.send_message('hello')
time.sleep(2)
c2.send_message('whats up')
time.sleep(2)
c1.send_message('Nothing much')
time.sleep(2)
c2.send_message('cool!')
time.sleep(5)

c1.disconnect()
time.sleep(2)
c2.disconnect()
