#!/usr/bin/env python3

import os
import rospy
from duckietown.dtros import DTROS, NodeType, TopicType
from duckietown_msgs.msg import WheelsCmdStamped, LanePose, Twist2DStamped,SegmentList,AntiInstagramThresholds
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage, Image

class MySubscriberNode(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MySubscriberNode, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        # construct publisher
        self.sub = rospy.Subscriber('marschla/anti_instagram_node/corrected_image/compressed', CompressedImage, self.callback)

    def callback(self, msg):
        delay = rospy.Time.now() - msg.header.stamp
        delay_float = delay.secs + float(delay.nsecs)/1e9    
        rospy.loginfo('delay test2 [s] =  %s' % delay_float) 
        

if __name__ == '__main__':
    # create the node
    node = MySubscriberNode(node_name='my_subscriber_node')
    # keep spinning
    rospy.spin()
