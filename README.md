# Considering Usability in an Automatic Signal Measuring System
## Installation
You need to use Ubuntu 20.04 ROS(noetic).

### Source install
```bash
# create a catkin workspace
mkdir -p ~/{catkin_ws}/src
cd ~/{catkin_ws}/src/

# clone into the catkin workspace
git clone https://github.com/AILab121/OOSE.git

# use rosdep to install all dependencies (including ROS itself)
sudo apt-get update -qq
sudo apt-get install -qq -y python-rosdep
sudo rosdep init
rosdep update
rosdep install --from-paths ./ -i -y --rosdistro noetic

# build all packages in the catkin workspace
source /opt/ros/noetic/setup.bash
catkin_init_workspace
cd ~/catkin_ws
catkin_make -DCMAKE_BUILD_TYPE=RelWithDebugInfo

source ~/catkin_ws/devel/setup.bash
```

## Gazebo demo(existing map)
```bash
# gazebo:
roslaunch mir_gazebo mir_maze_world.launch
```
- click the "start" button in the Gazebo GUI
```bash
# localization:
roslaunch mir_navigation amcl.launch

# navigation:
roslaunch mir_navigation start_planner.launch \
    map_file:=$(rospack find mir_gazebo)/maps/map.yaml
rviz -d $(rospack find mir_navigation)/rviz/navigation.rviz
```

## Gazebo demo(mapping)
```bash
# gazebo:
roslaunch mir_gazebo mir_maze_world.launch
```
- click the "start" button in the Gazebo GUI
```bash
# mapping:
roslaunch mir_navigation hector_mapping.launch

# navigation:
roslaunch mir_navigation move_base.xml with_virtual_walls:=false
rviz -d $(rospack find mir_navigation)/rviz/navigation.rviz

# save map:
rosrun map_server map_saver -f /home/ailab/new_robot_ws/src/mir_robot/mir_gazebo/maps/test
```

## Adjustment parameters
- /move_base_node/DWBLocalPlanner
- **max_speed_xy** can control speed
```bash
rosrun rqt_reconfigure rqt_reconfigure
```

## Connect the joystick
```bash
roslaunch robot5g teleop_joy.launch
```

## Complete Coverage Path Planning
- You need to create the map first

```bash
roslaunch path_coverage path_coverage.launch
```
- Click Publish Point at the top of RViz
- Click a single corner of n corners of the region
- Repeat for n times. After that you'll see a polygon with n corners
- The position of the final point should be close to the first
- When the closing point is detected the robot starts to cover the area

## Signal heat map
- You need to pay attention to the robot_width in path_coverage.launch and the size of map2darray in heatmap.py
- Need to change the speed to 0.2
```bash
rosrun signal heatmap.py 
```

## Running the driver on the real robot
### start up the robot
- switch on Mir
- connect to its wifi
- open mir.com

### Start the ROS driver
```bash
roslaunch mir_driver mir.launch
roslaunch mir_navigation costmap.xml
rviz -d $(rospack find mir_navigation)/rviz/navigation.rviz
```
