# ur3_webots

UR3 webots package to work with the manipation packages of the robot Suii.

## Getting started

### Requirements
For this package to work you'll need the following components:
* ROS Melodic
* Webots
* URSim version 3.6.1
* Suii packages
It's assumed ROS Melodic and Webots are already installed.

#### URSim installation
URSim version 3.6.1 can be downloaded from the following [website](https://www.universal-robots.com/download/?option=42164#section16632). Follow the instructions on that website for installation and startup.
**Be aware that the installation of URSim removes some ROS packages, you'll need to reinstall them after the URSim installation.**

#### Suii packages installation
The Suii packages that are needed can be found in the following Github repositories [suii_manipulation](https://github.com/RoboHubEindhoven/suii_manipulation), [suii](https://github.com/RoboHubEindhoven/suii). Clone those Github repositories to your catkin workspace. **Make sure to follow the extra installation steps for suii_manipulation. These can be found in the README of that repository.**

### Installing
To install this package, clone this repository to your catkin workspace.

## Running
1. Open webots and load the ur3.wbt file included worlds folder in this repository.
2. Launch Suii robot model with the following command: ``roslaunch suii_description display.launch``
3. Launch ``roslaunch suii_manipulation ur3_suii.launch robot_ip:=localhost``
4. Open up rviz and add Robotmodel to check if the robot model is loaded correctly: ``rosrun rviz rviz``
5. Run manipulation node: ``rosrun suii_manipulation Manipulation.py``. The robot should make a move when this node is started.
6. To move the robot to different positions ``rosservice call /move_camera "target: 0"``. Where 0 can be a integer from 0 to 16.
