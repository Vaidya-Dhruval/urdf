from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_rsp_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("m_5326927_001", package_name="m_5326927_001_moveit_config_pkg").to_moveit_configs()
    return generate_rsp_launch(moveit_config)