#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float64


def move_joint1(position):
    pub = rospy.Publisher('/marotte/joint1_position_controller/command', Float64, queue_size=10)                                                                  
    pub.publish(position)      
def move_joint2(position):
    pub = rospy.Publisher('/marotte/joint2_position_controller/command', Float64, queue_size=10)                                                                  
    pub.publish(position)  
def move_joint3(position):
    pub = rospy.Publisher('/marotte/joint3_position_controller/command', Float64, queue_size=10)                                                                  
    pub.publish(position)      
def move_joint4(position):
    pub = rospy.Publisher('/marotte/joint4_position_controller/command', Float64, queue_size=10)                                                                  
    pub.publish(position)  
def move_joint_5_gripper(position):
    pub = rospy.Publisher('/marotte/joint5_1_position_controller/command', Float64, queue_size=10)                                                                  
    pub.publish(position)      
    pub = rospy.Publisher('/marotte/joint5_2_position_controller/command', Float64, queue_size=10)                                                                  
    pub.publish(-position)    


      
                                                         


