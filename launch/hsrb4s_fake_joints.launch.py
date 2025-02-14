import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    # Path to the generated URDF file
    robot_description_file = '/tmp/hsrb4s_with_fake_joints.urdf'

    # Read the URDF file content
    with open(robot_description_file, 'r') as urdf_file:
        robot_description = urdf_file.read()

    # Path to RViz configuration
    rviz_file = os.path.join(get_package_share_directory('hsr_description'), 'rviz2', 'display.rviz')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}],
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['--display-config', rviz_file],
        ),
    ])
