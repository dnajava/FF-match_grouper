from csv import reader

class Matches:
    kit = None
    date = None
    matchlist = []

    def __Matches__(self, kit_p: str, day_p: date):
        self.kit = kit_p
        self.date = day_p
        return

    def setkit(self, kit_p):
        self.kit = kit_p

    def setday(self, day_p: date):
        self.date = day_p

    def read_matchlist(self, fname_p='') -> bool:
        if fname_p == '':
            return False
        tempkits = []
        try:
            with open(fname_p, 'r') as read_obj:
                csv_reader = reader(read_obj)
                ekarivi = True  # Skip first header row of match list
                for m in csv_reader:
                    if ekarivi == False:
                        tempkits.append(m)
                    else:
                        ekarivi = False
        except (IOError, OSError) as err:
            print(err)
            return False
        finally:
            if read_obj is not None:
                read_obj.close()
        self.matchlist = tempkits
        return True

    def show(self, mode=1):
        print('Kit', self.kit, self.date)
        if(mode == 2):
            for x in self.matchlist:
                print(x[0])