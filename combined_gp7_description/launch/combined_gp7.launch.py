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
            default_value='$(find combined_gp7_description)/urdf/combined_gp7.urdf.xacro',
            description='Path to the combined robot URDF Xacro file'),

        # Log the path to the robot description file
        LogInfo(
            msg='Loading robot description from: ' + LaunchConfiguration('robot_description').perform({}),
        ),

        # Node to process Xacro and load the robot description parameter
        Node(
            package='xacro',
            executable='xacro',
            name='xacro_to_urdf',
            output='screen',
            parameters=[{'robot_description': LaunchConfiguration('robot_description')}],
            arguments=[LaunchConfiguration('robot_description')],
        ),

        # Node to publish the robot state
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
