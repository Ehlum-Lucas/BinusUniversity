'''
# @ Author: Lucas Iglesia
# @ Create Time: 2024-10-08 18:10:34
# @ Modified by: Lucas Iglesia
# @ Modified time: 2024-10-08 18:10:36
# @ Description: Robot Class
'''

from typing import List
from zone import zones
import random

BATTERY_LEVEL = 100
PC_REQUIRED = 4

class ExploringRobot:
    def __init__(self, inventory: List[str] = [], battery_level: int = BATTERY_LEVEL) -> None:
        self.inventory = inventory
        self.battery_level = battery_level

    def move_to_zone(self, zone: str) -> None:
        """Move to a selected zone and encounter a random item."""
        if zone not in get_available_zones():
            print("This zone doesn't exist.")
            return
        print(f"\nExploring {zone}...")
        item = random.choice(zones[zone])
        print(f"You encountered a {item}.")
        self.process_item(item, zone)

    def process_item(self, item : str, zone: str) -> None:
        """Handle items encountered in zones: add to inventory or adjust battery."""
        if item == "power cell":
            self.collect_item(item)
        elif item == "short circuit":
            self.battery_level -= 20
            print("Battery drained by 20%.")
        elif item == "battery pack":
            self.battery_level = min(self.battery_level + 30, 100)
            print("Battery recharged by 30%.")
        zones[zone].remove(item)

    def collect_item(self, item : str) -> None:
        """Add a power cell to the inventory."""
        self.inventory.append(item)
        print("Power cell collected!")

    def display_inventory(self) -> None:
        """Show collected power cells."""
        print("\nInventory:")
        print("Power cells:", self.inventory.count("power cell"))

    def run(self) -> None:
        """Run the robot until the battery runs out or all power cells are collected."""
        while self.battery_level > 0 and self.inventory.count("power cell") < 4:
            print(f"\nBattery Level: {self.battery_level}%")
            self.display_inventory()
            print("Available Zones:", ", ".join(get_available_zones()))
            chosen_zone = input("Choose a zone to explore: ")
            self.move_to_zone(chosen_zone)
            self.battery_level -= 10
        if self.inventory.count("power cell") >= PC_REQUIRED:
            print("\nCongratulations! You collected all power cells and won the game!")
        else:
            print("\nGame Over! You've run out of battery.")

def get_available_zones() -> List[str]:
    """Return a list of available zones."""
    return [zone for zone, items in zones.items() if items]
