from setuptools import find_packages, setup

package_name = 'arm_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Terrawarden Drone Cleanup MQP',
    maintainer_email='gr-dronecleanup@wpi.edu',
    description='ROS2 Node for Controlling a 3DOF arm with Dynamixels',
    license='GPLv3',
    entry_points={
        'console_scripts': [
        	'arm_node = arm_control.RosArm:main',
        ],
    },
)