#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float64


def move_joint():
    pub = rospy.Publisher('/marotte/joint4_position_controller/command', Float64, queue_size=10)                
    rospy.init_node('move_joint4', anonymous=True)                              
    i = 0       
    rate = rospy.Rate(10)     
    while not rospy.is_shutdown():                                         
        position = float(input("Enter the position for the -1.7<joint4<1.7: "))                               
        rospy.loginfo(position)                                            
        pub.publish(position)                                             
        rate.sleep()  
                                                         

if __name__ == '__main__':
    try:
        move_joint()
    except rospy.ROSInterruptException:
        pass


