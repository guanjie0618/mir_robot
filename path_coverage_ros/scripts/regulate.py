#!/usr/bin/env python3

import rospy  
from geometry_msgs.msg import Twist

class Regulate:  

    def __init__(self):  

        rospy.init_node('regulate')
        cmd_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        rate = 50
        looprate = rospy.Rate(rospy.get_param('~hz', rate))

        linear_speed = 0.2
        goal_distance = 0.1
        linear_duration = goal_distance / linear_speed
        cmd = Twist()
        cmd.linear.x = linear_speed

        count = int(linear_duration * rate)
        for i in range(count):
            i += 1
            cmd_pub.publish(cmd)
            looprate.sleep()
            
            


if __name__ == "__main__": Regulate()