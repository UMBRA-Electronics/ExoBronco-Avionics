from Pancake import pancake
import time

# Placeholder variables/methods

# This will be an entirely separate class fully designated to writing
# the flight logs. The constructor should check whether there is previous
# flight data and act accordingly, you wouldn't check that here
establish_new_flight_record: None

# A separate method which checks everything it needs to, it should throw
# errors inside that function, so I shouldn't raise any exceptions in this file
# This function should also relay whatever exception was thrown to the groundstation
system_verification_checks: None

# Method which starts all L0 tasks
start_L0_tasks: None

# Transmit data to ground station
transmit_to_groundstation: None

# Writes data to memory
write_to_memory: None

# Transfers memory to SD card
transfer_memory: None

# Starts motor 2 ignition
enable_head_end_ignition: None

# Enables drogue deployment charge
enable_drogue_charge: None

# Enables the main deployment charge
enable_main_charge: None

# Anything that I cant explain
placeholder: None

# Turns off rocket
power_off: None

# This tries to connect to the groundstation, only returns a boolean
establish_groundstation_connection: bool

# This asks for a launch callback from the ground station, returns a boolean when receiving an OK
launch_call_back: bool

# Main charge is broken
main_charge_continuity: bool

# This shows the rocket's acceleration
rocket_acceleration: float

# Estimated rocket acceleration
estimated_acceleration: float

# This shows the rocket's velocity
rocket_velocity: float

# This shows the rocket's altitude
rocket_altitude: float

# The amount of time rocket has been in the air
air_time: float


def commissioning():
    # Starts a new flight record
    establish_new_flight_record
    # A loop trying to connect to the groundstation, breaking out of the
    # loop when it connects
    while True:
        if establish_groundstation_connection:
            break
        time.sleep(0.25)

    # Does all the preliminary testing before being cleared to go
    system_verification_checks

    # If it returns True, break out of the loop
    # Should only return false if it is unsafe to continuously be probing the platform
    while True:
        if launch_call_back:
            break
        time.sleep(0.5)


def on_pad():
    # Updates status variables
    pancake.avionic_state("OnPad")

    # Starts the L0 tasks
    start_L0_tasks

    # Transmits to groundstation and writes to memory if
    # the acceleration > 0. Also goes to the next stage
    # if the acceleration > 0
    while True:
        transmit_to_groundstation
        if rocket_acceleration > 0:
            write_to_memory
            break
        time.sleep(0.25)


def motor_1_burn():
    # Updates status variables
    pancake.avionic_state("Motor1Burn")

    # Constantly writes to memory and groundstation until
    # this phase ends when its acceleration goes below 0
    while True:
        write_to_memory
        transmit_to_groundstation
        if rocket_acceleration < 0:
            break
        time.sleep(0.25)


def coast_1():
    # Updates status variable
    pancake.avionic_state("Coast1")

    # Stores time from RTC?
    air_time

    while True:
        # Loops writing to memory and the ground station
        # Until time is satisfied
        write_to_memory
        transmit_to_groundstation

        # When the compared time is > 15
        if air_time > 15:
            break
        time.sleep(0.25)


def motor_2_ignition():
    # Starts the motor 2 ignition
    enable_head_end_ignition

    # Stores the time
    air_time

    # Writes to memory and groundstation until it has been
    # firing for 2.5 seconds
    while True:
        write_to_memory
        transmit_to_groundstation
        if air_time > 2.5:
            break
        time.sleep(0.25)


def motor_2_burn():
    # updates status variable
    pancake.avionic_state("Motor2Burn")

    # Writes to memory and groundstation until acceleration
    # drops below 0
    while True:
        write_to_memory
        transmit_to_groundstation
        if rocket_acceleration < 0:
            break
        time.sleep(0.25)


def coast_2():
    # Updates status variable
    pancake.avionic_state("Coast2")

    # Writes to memory and groundstation until velocity drops
    # below 0
    while True:
        write_to_memory
        transmit_to_groundstation
        if rocket_velocity < 0:
            break
        time.sleep(0.25)


def drogue_deployment():
    # Writes to memory and groundstation for X seconds, 15 is a
    # placeholder, also enables drogue charge and stores airtime
    counter = 0
    while True and counter < 3:
        # Enables the drogue charge
        enable_drogue_charge

        # Stores time from RTC
        air_time

        # Nested while loop to write to memory and groundstation
        # until air time passes X
        while True:
            write_to_memory
            transmit_to_groundstation
            if air_time > 15:
                break

        if placeholder:
            break

        counter += 1
        time.sleep(0.25)

    if rocket_acceleration == estimated_acceleration and counter < 3:
        # Updates status variable
        pancake.avionic_state("DrogueDeploy")

        # Writes to memory and groundstation until altitude is
        # below 12.5k ft
        while True:
            write_to_memory
            transmit_to_groundstation
            if rocket_altitude < 1250:
                break
            time.sleep(0.25)

    else:
        while True:
            write_to_memory
            transmit_to_groundstation
            if rocket_altitude < 90000:
                break
            time.sleep(0.25)


def main_deployment():
    counter = 0
    while main_charge_continuity and counter < 3:
        # Enables main deployment charge
        enable_main_charge

        # Stores air time from RTC
        air_time

        while True:
            write_to_memory
            transmit_to_groundstation

            if air_time > 2:
                break
            time.sleep(0.25)

    # Updates status variable
    pancake.avionic_state("MainDeploy")

    while True:
        write_to_memory
        transmit_to_groundstation

        if rocket_velocity == 0:
            break
        time.sleep(0.25)


def landed():
    # Updates status variable
    pancake.avionic_state("Landed")

    # Transfers memory to SD Card
    transfer_memory

    # Transmits to groundstation until placeholder
    while True:
        transmit_to_groundstation

        if placeholder:
            break
        time.sleep(0.25)

    # Turns off rocket
    power_off
