import inFlightCore1 as Flight
import time
import Pancake

# Placeholder variables/methods

# A constantly changing function which tells us whether
# it is safe to start a burn
is_safe: bool

# A looping function which takes a boolean value as a parameter
# and returns a boolean value
# Should loop infinitely until it receives what it wants
rocket_acceleration: float

# A float value of the rocket's velocity
rocket_velocity: float

# Start of program
Flight.commissioning()

Flight.on_pad()

Flight.motor_1_burn()

Flight.coast_1()

# Loops 3 times only if conditions are safe and if acceleration isn't detected
counter = 0
while is_safe and counter < 3:
    Flight.motor_2_ignition()
    if rocket_acceleration > 0:
        break
    counter += 1
    time.sleep(0.5)
    # Wait X seconds

# The while loop will be left after 3 failed attempts of the motor_2_ignition
# It will be left if the rocket is unsafe
# It will be left if the rocket successfully ignited

# If it successfully ignited
if is_safe and counter < 3:
    Flight.motor_2_burn()

# If it didn't successfully ignite, it will go straight to coast_2
# When acceleration is < 0, or it isn't safe, or ignition loop failed 3 times
Flight.coast_2()

Flight.drogue_deployment()

Flight.main_deployment()

# gg ez
Flight.landed()
