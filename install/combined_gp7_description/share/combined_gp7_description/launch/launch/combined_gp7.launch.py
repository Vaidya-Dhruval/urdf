# launch/combined_robot_launch.py

import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('robot_description', default_value=''),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', LaunchConfiguration('rviz_config')],
            parameters=[{'robot_description': LaunchConfiguration('robot_description')}],
        ),
        LogInfo(
            condition=launch.substitutions.LaunchConfigurationEquals('robot_description', ''),
            msg="Robot description parameter not provided.",
        ),
    ])
