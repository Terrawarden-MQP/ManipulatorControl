# ManipulatorControl

### Dependencies

- numpy (v1.26)
- dynamixel_sdk
- ROS2 (rclpy)

Internal Dependencies:
- Terrawarden-MQP/CustomMessages

## Node Info

Manipulator Control is a lightweight node for controlling a 3DOF arm using Dynamixel actuators with Quintic Trajectories. 
It also contains a setpoint queue for processing multi-step commands, such as pre-written stow + unstow procedures.

### Trajectory Modes
- TrajectoryModes.JOINT_SPACE - Joint space quintic trajectory
- TrajectoryModes.TASK_SPACE - Task space quintic trajectory
- TrajectoryModes.LIVE_TRACK - Skips quintic trajectory, queues arm motion instantly for live tracking incoming positions

## ROS Info

### Publishers
| Topic | Type | Description |
|-------|------|-------------|
| `/arm_status` | ArmStatus (see CustomMessages) | A recurring message (100Hz) with information about the Arm's position, velocity, and current motion plans |
| `/ee_pos` | geometry_msgs/PointStamped | A recurring message (100 Hz) with the 3D Position of the End Effector |

### Subscribers
| Topic | Type | Description |
|-------|------|-------------|
| `/move_arm_command` | ArmCommand (see CustomMessages) | An incomming arm motion command. Interrupts any previous motion plans |
| `/force_grasp` | std_msgs/Bool | A command to open/close the gripper directly |

### Services
| Topic | Parameters | Description |
|-------|------|-------------|
| `/stow_arm` | None | Queues the stow routine |
| `/unstow_arm` | None | Queues the unstow routine |

### ros2 launch args
| Argument | Type | Description |
|-------|------|-------------|
| None |  | |