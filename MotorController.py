"""
    Handles a single stepper motor on the pins passed to it
"""
import multiprocessing as mp    

class MotorController:
    def __init__(self, pins, desired_rotation) -> None:
        assert len(pins) == 4, "MotorController: Incorrect number of pins"

        self.desired_rotation = desired_rotation
        print(f"Motor Controller: Initializing on pins: {pins}")

        
    def start():
        pass
    
    def update(self):
        pass