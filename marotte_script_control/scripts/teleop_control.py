#! /usr/bin/env python3
import rospy
import tty
import sys
import termios
from std_msgs.msg import Float64
import all_joints
import time


def move_joint():              
    rospy.init_node('telop_control', anonymous=True)       
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)                       
    rate = rospy.Rate(10)     
    input = 0
    angle_j1=0
    angle_j2=0
    angle_j3=0
    angle_j4=0
    angle_j5=0
    pos_change=0.01
    
    while not rospy.is_shutdown():    
        rospy.loginfo("Press the joint number to operate: ")
        print("Joint1:" + str(angle_j1))
        print("Joint2:" + str(angle_j2))
        print("Joint3:" + str(angle_j3))
        print("Joint4:" + str(angle_j4))
        print("Joint5_gripper:" + str(angle_j5))
        print("pos_change:" + str(pos_change))
        input = sys.stdin.read(1)
        while(input=="1" or input=="+" or input=="-" or input=="i" or input=="d"):
            print("Operating on Joint1")
            print("Joint1:" + str(angle_j1))
            print("Joint2:" + str(angle_j2))
            print("Joint3:" + str(angle_j3))
            print("Joint4:" + str(angle_j4))
            print("Joint5_gripper:" + str(angle_j5))
            print("pos_change:" + str(pos_change))
            input = sys.stdin.read(1)
            if input =="+":
                if angle_j1<1.70:
                    angle_j1 = angle_j1+ pos_change
                else:
                    angle_j1=1.7
                all_joints.move_joint1(angle_j1)               
            elif input == "-":
                if angle_j1 >-1.70:
                    angle_j1 = angle_j1-pos_change
                else:
                    angle_j1=-1.7
                all_joints.move_joint1(angle_j1)       
            elif input=="i":
                pos_change=pos_change+0.001
            elif input=="d":
                pos_change=pos_change-0.001            
            else:
                rospy.loginfo("De-selecting Joint 1")

            


        while(input=="2" or input=="+" or input=="-" or input=="i" or input=="d"):
            print("Operating on Joint2")
            print("Joint1:" + str(angle_j1))
            print("Joint2:" + str(angle_j2))
            print("Joint3:" + str(angle_j3))
            print("Joint4:" + str(angle_j4))
            print("Joint5_gripper:" + str(angle_j5))     
            print("pos_change:" + str(pos_change))     
            input = sys.stdin.read(1)
            if input =="+":
                if angle_j2<1.70:
                    angle_j2 = angle_j2+ pos_change
                else:
                    angle_j2=1.7
                all_joints.move_joint2(angle_j2)               
            elif input == "-":
                if angle_j2 >-1.70:
                    angle_j2 = angle_j2-pos_change
                else:
                    angle_j2=-1.7

                all_joints.move_joint2(angle_j2)         
            elif input=="i":
                pos_change=pos_change+0.001
            elif input=="d":
                pos_change=pos_change-0.001        
            else:
                rospy.loginfo("De-selecting Joint 2")



        while(input=="3" or input=="+" or input=="-" or input=="i" or input=="d"):
            print("Operating on Joint3")
            print("Joint1:" + str(angle_j1))
            print("Joint2:" + str(angle_j2))
            print("Joint3:" + str(angle_j3))
            print("Joint4:" + str(angle_j4))
            print("Joint5_gripper:" + str(angle_j5))
            print("pos_change:" + str(pos_change))
            
            input = sys.stdin.read(1)
            if input =="+":
                if angle_j3<1.70:
                    angle_j3 = angle_j3+ pos_change
                else:
                    angle_j3=1.7
                all_joints.move_joint3(angle_j3)               
            elif input == "-":
                if angle_j3 >-1.70:
                    angle_j3 = angle_j3-pos_change
                else:
                    angle_j3=-1.7
                all_joints.move_joint3(angle_j3)               
            elif input=="i":
                pos_change=pos_change+0.001
            elif input=="d":
                pos_change=pos_change-0.001  
            else:
                rospy.loginfo("De-selecting Joint 3")
        while(input=="4" or input=="+" or input=="-" or input=="i" or input=="d"):
            print("Operating on Joint4")
            print("Joint1:" + str(angle_j1))
            print("Joint2:" + str(angle_j2))
            print("Joint3:" + str(angle_j3))
            print("Joint4:" + str(angle_j4))
            print("Joint5_gripper:" + str(angle_j5))
            print("pos_change:" + str(pos_change))
            
            input = sys.stdin.read(1)
            if input =="+":
                if angle_j4<1.70:
                    angle_j4 = angle_j4+ pos_change
                else:
                    angle_j4=1.7
                all_joints.move_joint4(angle_j4)               
            elif input == "-":
                if angle_j4 >-1.70:
                    angle_j4 = angle_j4-pos_change
                else:
                    angle_j4=-1.7
                all_joints.move_joint4(angle_j4)               
            elif input=="i":
                pos_change=pos_change+0.001
            elif input=="d":
                pos_change=pos_change-0.001  
            else:
                rospy.loginfo("De-selecting Joint 4")

        while(input=="5" or input=="+" or input=="-" or input=="i" or input=="d"):
            print("Operating on Joint5_gripper")
            print("Joint1:" + str(angle_j1))
            print("Joint2:" + str(angle_j2))
            print("Joint3:" + str(angle_j3))
            print("Joint4:" + str(angle_j4))
            print("Joint5_gripper:" + str(angle_j5))
            print("pos_change:" + str(pos_change))
            
            input = sys.stdin.read(1)
            if input =="+":
                if angle_j5<0.4:
                    angle_j5 = angle_j5+ pos_change
                else:
                    angle_j5=0.4
                all_joints.move_joint_5_gripper(angle_j5)               
            elif input == "-":
                if angle_j5 >-0.4:
                    angle_j5 = angle_j5-pos_change
                else:
                    angle_j5=-0.4
                all_joints.move_joint_5_gripper(angle_j5)               
            elif input=="i":
                pos_change=pos_change+0.001
            elif input=="d":
                pos_change=pos_change-0.001  
            else:
                rospy.loginfo("De-selecting Joint 5_ gripper")             

             
      

    #termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)    

                                                         

if __name__ == '__main__':
    try:
        move_joint()
    except rospy.ROSInterruptException:
        pass









