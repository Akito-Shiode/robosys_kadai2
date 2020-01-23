#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def string_check(msg):
    if msg.data == '0' :
        print("\rno pin select")
    elif msg.data == '1' :
        print("\r14 pin select")
    elif msg.data == '2' :
        print("\r17 pin select")
    elif msg.data == '3' :
        print("\r14 & 17 pin select")
    elif msg.data == 'exit' :
        print("\rPublisher is stopped")
    else :
        print("\rPlease choose from one of these.\n 0: no pin\n 1: 14 pin\n 2: 17 pin\n 3: 14 & 17 pin\n exit: exit node")


if __name__ == "__main__":
    print("\rled_flash_sub.py is started")
    rospy.init_node("led_sub")
    sub = rospy.Subscriber('led_flash_str', String, string_check)
    rospy.spin()
