

class flightData:
    date = ""
    file_path = ""
    real_transmit: str

    def __init__(self):
        self.file = open(self.file_path + "Flight Data: " + self.date + ".txt", "w")

    def write(self, input_string):
        self.file.write(input_string)

    def transmit(self, input_string):
        self.real_transmit()
