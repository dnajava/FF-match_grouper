'''
Names of tested persons of kits. Load them from a csv file.
'''
class KitNames:
    def __KitNames(self):
        list = []

    def read_namelist(self, fname_p='') -> bool:
        '''
        Read names of tested persons from file
        :param str fname_p File name of names of kits file. If not set, use kitsnames.csv
        :return bool Did the reading success?
        '''

        if fname_p == '':
            fname_p = 'kitsnames.csv'

        tempkits = []
        try:
            with open(fname_p, 'r') as read_obj:
                csv_reader = reader(read_obj)
                for m in csv_reader:
                    m2 = m.split()
                    kit = m[0]
                    name = m[1]
                    name += m[2]
                    m3 = (kit,name)
                    self.list.append(m3)
        except (IOError, OSError) as err:
            print(err)
            return False
        finally:
            if read_obj is not None:
                read_obj.close()
        return True


    def getname(self, kit_p: str) -> str:
        '''
        Find full name of tested person of a kit
        :param str kit_p Kit id
        :return str Full name of tested person of a kit
        '''

        for x in self.list:
            if kit_p == self.list[kit_p][2]:
                return self.list[kit_p][2]


    def show(self, mode_p=0):
        '''
        For test purposes. Show
        :param int mode_p Print whole list item, only kit id or kit id and full name
        '''

        match mode_p:
            case 0:
                for a in self.list:
                    print(a[0], end=" ")
            case 1:
                for a in self.list:
                    print(a[0], end=" ")
            case 2:
                for a in self.list:
                    print(a[0], a[1], end=" ")
            case _:
                print('Unknown')