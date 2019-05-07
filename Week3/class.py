class washerFactory():
    #Constructor
    def __init__(self, mode, voltage):
        self.mode = mode
        self.voltage = voltage

    #self는 Argument로 치지 않는다.
    def wash(self, time):
        print("{} 세탁기를 돌립니다~".format(self.mode))
        print("{}분 동안 돌립니다~".format(time))
        return

drumwasher = washerFactory("드럼세탁기", 220)
drumwasher.wash(5)