from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  return LaunchDescription(             #기본적인 launch파일의 형식, class 및 다른 것을 사용하지 않고 이 자체로 사용
    Node(
      package='my_package',
      executable='moveturtle',
      name='move_turtle')
  )
