import time
import board
import simpleio

# define the frequency of each note in Hz
NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392
NOTE_A4 = 440
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_E3 = 165
NOTE_G3 = 196
NOTE_A3 = 220
NOTE_B3 = 247

# define the duration of each note in seconds
QUARTER_NOTE = 0.25
HALF_NOTE = 0.5
WHOLE_NOTE = 1

# create a simpleio output for the buzzer
buzzer = simpleio.tone(board.IO16, 440)

# define the notes and timing for the Mario theme song
mario_song = [
    (NOTE_E4, QUARTER_NOTE),
    (NOTE_E4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_E4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_C4, QUARTER_NOTE),
    (NOTE_E4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_G4, HALF_NOTE),
    (0, HALF_NOTE),
    (NOTE_G3, HALF_NOTE),
    (0, HALF_NOTE),
    (NOTE_C4, HALF_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_G3, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_E3, QUARTER_NOTE),
    (0, HALF_NOTE),
    (NOTE_A3, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_B3, QUARTER_NOTE),
    (0, HALF_NOTE),
    (NOTE_A3, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_G3, QUARTER_NOTE),
    (NOTE_E4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_G4, HALF_NOTE),
    (0, HALF_NOTE),
    (NOTE_A4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_F4, QUARTER_NOTE),
    (NOTE_G4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_E4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_C4, QUARTER_NOTE),
    (NOTE_D4, QUARTER_NOTE),
    (0, HALF_NOTE),
    (NOTE_B3, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_C4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_G3, QUARTER_NOTE),
    (NOTE_E4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_G4, HALF_NOTE),
    (0, HALF_NOTE),
    (NOTE_A4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_F4, QUARTER_NOTE),
    (NOTE_G4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_E4, QUARTER_NOTE),
    (0, QUARTER_NOTE),
    (NOTE_C4, QUARTER_NOTE),
    (NOTE_D4, QUARTER_NOTE),
    (0, HALF_NOTE),
    (0, WHOLE_NOTE)
]