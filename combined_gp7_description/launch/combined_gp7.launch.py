#!/usr/bin/env python

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Declare the launch arguments
    return LaunchDescription([
        DeclareLaunchArgument(
            'robot_description',
            default_value='$(find combined_gp7_description)/urdf/combined_robot.xacro',
            description='Path to the combined robot URDF file'),

        # Log the path to the robot description file
        LogInfo(
            condition=LaunchConfiguration('robot_description'),
            msg='Loading robot description from: ' + LaunchConfiguration('robot_description')
        ),

        # Node to load the robot description parameter
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': LaunchConfiguration('robot_description')}],
        ),

        # Node to launch RViz for visualization
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            # Provide path to an RViz configuration file or remove arguments if not needed
            # arguments=['-d', LaunchConfiguration('rviz_config')],
        ),
    ])
