from csv import reader

'''
Matchlist of one kit.
'''
class Matches:
    type = None                         # Type of mach list
    kit = None                          # Kit id
    date = None                         # Date of match list
    # name = None
    matchlist = []

    def __Matches__(self):
        return

    def setkit(self, kit_p):
        self.kit = kit_p

    def setday(self, day_p: date):
        self.date = day_p

    '''
    Read FTDNA matchlist.
    '''
    @param fname_p File name of match file.
    @return Did the reading succeed?
    def read_ftdna_matchlist(self, fname_p='') -> bool:
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

    '''
    Read MyHeritage matchlist.
    '''
    @param fname_p File name of match file.
    @return Did the reading succeed?
    def read_MyHeritageMatchlist(self, fname_p='') -> bool:
        if fname_p == '':
            return False
        tempkits = []
        try:
            with open(fname_p, 'r') as read_obj:
                csv_reader = reader(read_obj)
                ekarivi = True  # Skip first header row of match list
                for m in csv_reader:
                    if ekarivi == False:
                        tempkits.append(m[1])
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

    '''
    For test purposes. Print kit id and date of file. Extended test print also names of matches.
    '''
    @param fname_p File name of match file.
    @return Did the reading succeed?

    def show(self, mode=1):
        print('Kit', self.kit, self.date)
        if(mode == 2):
            for x in self.matchlist:
                print(x[0])