import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile


class M_turtle(Node):
    def __init__(self):
        super().__init__('move_turtle')
        self.qos = QoSProfile(depth=10)
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', self.qos)
        self.create_timer(0.1, self.pubmessage)
        self.vel = 0.2
        self.ang_vel = 0.5
        self.move_time = 4.0
        self.is_turning = False
        self.turn_start_time = 0.0

    def pubmessage(self):
        msg = Twist()
        if not self.is_turning:
            msg.linear.x = self.vel
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = self.ang_vel
            if self.get_clock().now().to_sec() - self.turn_start_time >= self.move_time:
                self.is_turning = False
        self.pub.publish(msg)
        self.get_logger().info(f'Sending message: [{msg}]')

        if not self.is_turning and self.get_clock().now().to_sec() >= self.turn_start_time + self.move_time:
            self.is_turning = True
            self.turn_start_time = self.get_clock().now().to_sec()

def main():
    rclpy.init()
    node = M_turtle()
    try:
        rclpy.spin(node)
    except:
        node.destroy_node()


if __name__ == '__main__':
    main()
