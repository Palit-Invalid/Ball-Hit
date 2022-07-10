import shelve

class PlayerList:
    def __init__(self, filename) -> None:
        self.records = shelve.open(filename)

    def __del__(self):
        self.records.close()

    def update_record(self, playername: str, new_time: float):
        if not playername in self.records:
            print("Not found player ", playername, ". Create record for new user.", sep='')
            self.records[playername] = new_time
        else:
            if self.records[playername] > new_time:
                print("Congratulations! You set a new record!")
                self.records[playername] = new_time

    def print_all(self):
        for rec in self.records:
            print("{0:{width}} {1}".format(rec, self.records[rec], width=10))
