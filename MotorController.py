"""
    Handles a single stepper motor on the pins passed to it
"""
import multiprocessing as mp    
import StepperMotor

class MotorController:
    def __init__(self, pins, desired_rotation) -> None:
        assert len(pins) == 4, "MotorController: Incorrect number of pins"
        self.motor = StepperMotor.StepperMotor(pins[0], pins[1], pins[2], pins[3])

        self.desired_rotation = desired_rotation
        print(f"Motor Controller: Initializing on pins: {pins}")

        
    def start():
        pass
    
    def update(self):
        pass

    def test_rotate(self, value):
        self.motor.rotate(value)