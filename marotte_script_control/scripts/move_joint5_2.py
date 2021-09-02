#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float64


def move_joint():
    pub = rospy.Publisher('/marotte/joint5_2_position_controller/command', Float64, queue_size=10)                
    rospy.init_node('move_joint5_2', anonymous=True)                              
    i = 0       
    rate = rospy.Rate(10)     
    while not rospy.is_shutdown():                                         
        position = float(input("Enter the position for the -0.4<joint5_2<0: "))                               
        rospy.loginfo(position)                                            
        pub.publish(position)                                             
        rate.sleep()    
                                                         

if __name__ == '__main__':
    try:
        move_joint()
    except rospy.ROSInterruptException:
        pass


