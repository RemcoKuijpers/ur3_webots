#!/usr/bin/env python

"""ur3_ros_controller controller."""

import rospy
from sensor_msgs.msg import JointState
from controller import Robot, Motor

class RobotController():
    def __init__(self):
        rospy.init_node("ur3_webots_controller")
        self.sub = rospy.Subscriber("/joint_states", JointState, self.callback, queue_size=1)
        self.robot = Robot()
        self.timestep = int(self.robot.getBasicTimeStep())
        self.motors = []
        for m in range(0,12,2):
            self.motors.append(self.robot.getDeviceByIndex(m))
        for t in range(6):
            self.motors[t].setAvailableTorque(10000000)
            self.motors[t].setVelocity(10000000)
        self.positions = [0,0,0,0,0,0]

    def callback(self, data):
        if self.robot.step(self.timestep) != -1:
            for p in range(6):
                self.motors[p].setPosition(data.position[p])

if __name__ == "__main__":
    rc = RobotController()
    rospy.spin()