"""
Main
Entry point for the program and hadnles the general state and flow.
"""

# Multiproccessing
import multiprocessing as mp

# Hardware Controllers
import CameraController
import MotorController
import DistanceSensorController

# Pins for the stepper motors
YAW_MOTOR_PINS    = (6, 13, 19, 26)
PITCH_MOTOR_PINS  = (7, 1, 0, 5)
FIRING_MOTOR_PINS = (9, 11, 25, 8)
DISTANCE_SENSOR_PINS = (16, 20)
RGB_PINS = (4, 3, 2)

LAUNCHER_PIN = 14




class Manager:

    # Initialize our Manager
    def __init__( self ):
        print("Manager: Initializing.")

        # Multiprocessing Values
        self.phase = mp.Value("i", 0)
        self.desired_yaw_rotation = mp.Value("i", 0)
        self.desired_pitch_rotation = mp.Value("i", 0)
        self.should_fire = mp.Value("i", 0)

        # Make our motors.
        self.yaw_motor = MotorController.MotorController( YAW_MOTOR_PINS, self.desired_yaw_rotation )
        self.pitch_motor = MotorController.MotorController( PITCH_MOTOR_PINS, self.desired_pitch_rotation )
        self.firing_motor = MotorController.MotorController( FIRING_MOTOR_PINS, self.should_fire )

        # Make our camera.
        self.cam_controller = CameraController.CameraController(self.phase, self.desired_yaw_rotation, self.desired_pitch_rotation )

        # Make our distance sensor controller.
        self.dist_controller = DistanceSensorController.DistanceSensorController(self.phase, self.desired_pitch_rotation)

        



    def start(self):        
        # Start Phase 1.
        self.start_phase_one()

    def update( self ):
        pass

    """
    Phase One
        Idle, Awaiting Target
    """
    def start_phase_one( self ):
        print("Manager: Starting Phase One.")
        self.phase = 1

    def evauluate_phase_one( self ):
        pass

    """
    Phase Two
        Target Found, Center in frame
    """
    def start_phase_two( self ):
        print("Manager: Starting Phase Two.")

    def evaluate_phase_two( self ):
        pass

    """
    Phase Three
        Adjust for Speed and Distance
    """

    def start_phase_three( self ):
        print("Manager: Starting Phase Three.")


    def evaluate_phase_three( self ):
        pass

    """
    Phase Four
    Fire 
    """

    def start_phase_four( self ):
        print("Manager: Starting Phase Four.")


    def evaluate_phase_four( self ):
        pass
    



def test():
    yaw = MotorController.MotorController(YAW_MOTOR_PINS)
    while(True):
        yaw.test_rotate()
        
if __name__ == "__main__":
    manager = Manager()
    manager.start()
    test()
    # Loop the program
    while(True):
        manager.update()
