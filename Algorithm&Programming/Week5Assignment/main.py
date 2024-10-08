'''
# @ Author: Lucas Iglesia
# @ Create Time: 2024-10-08 17:48:51
# @ Modified by: Lucas Iglesia
# @ Modified time: 2024-10-08 17:50:38
# @ Description: Week 5 Assignment - Robot Exploring Zones
'''

from zone import zones
from typing import List
from exploringRobot import ExploringRobot, get_available_zones

def main() -> None:
    robot = ExploringRobot()
    robot.run()

if __name__ == "__main__":
    main()