# Ros-development
For studying
this is first edit3

- - -

## 2023_02_13

- - -

* first
  * turtlebot3
  * Laptop ubuntu 20.04.01 LTS

* second
  * ROS2 DDS explain

* third

```shell
  * ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist '{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 2.0, y: 0.0, z: 1.8}}'
  # I can control turtle1 and turtle2

  * ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.5, y: 9, theta: 1.57, name: 'turtle2'}"
  # I can make service2 to control another turtlebot
```
