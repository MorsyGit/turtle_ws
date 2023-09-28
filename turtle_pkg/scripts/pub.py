#!/usr/bin/python3.8
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('turtle_publisher')

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(1)  # 1 Hz publishing rate

angular_speed = 0.5  # Angular speed in radians per second
radius = 2.0  # Radius of the circular path
linear_speed = angular_speed * radius

while not rospy.is_shutdown():
    vel_msg = Twist()
    vel_msg.linear.x = linear_speed
    vel_msg.angular.z = angular_speed
    pub.publish(vel_msg)
    rospy.loginfo("Moving in a circle")
    rate.sleep()
