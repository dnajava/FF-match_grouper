from csv import reader

class Matches:
    '''
    Matchlist of one kit.
    '''

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


    def read_ftdna_matchlist(self, fname_p='') -> bool:
        '''
        Read FTDNA matchlist.
        :param str fname_p File name of match file.
        : return bool Did the reading succeed?
        '''

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


    def read_MyHeritageMatchlist(self, fname_p='') -> bool:
        '''
        Read MyHeritage matchlist.
        :param str fname_p File name of match file
        :return bool Did the reading success?
        '''

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


    def show(self, mode=1):
        '''
        For test purposes. Print kit id and date of file. Extended test print also names of matches.
        :param int mode Printing mode kit id or full name of tested person
        :return bool Did the reading succeed?
        '''
        print('Kit', self.kit, self.date)
        if(mode == 2):
            for x in self.matchlist:
                print(x[0])