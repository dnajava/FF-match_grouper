import os
from csv import reader
from datetime import date
from Matches import Matches

mltypes = ['Unkwnown', 'FTDNA', 'MyHeritage']

class Matchlists:
    lists = []
    kitsnames = []

    def __Matchlists__(self):
        self.lists = []
        self.kitnames = []

    def readkitsnames(self):
        try:
            with open('kitsnames.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                for m in csv_reader:
                    s = m[0].split(' ')
                    x = (s[0], s[1] + ' ' + s[2])
                    self.kitsnames.append(x)
        except (IOError, OSError) as err:
            print(err)
            return False
        finally:
            if read_obj is not None:
                read_obj.close()

    def __getitem__(self):
        return self.lists

    def showkitsnames(self):
        for k in self.kitsnames:
            print(k)

    def get_FTDNA_matchlists(self, dlpath: str = ''):
        if dlpath == '':
            self.lists = None
            return False

        with os.scandir(dlpath) as entries:
            for entry in entries:
                if (entry.name).endswith('.csv'):
                    if ('Family' in entry.name and 'Finder' in entry.name and 'Matches' in entry.name):
                        s2 = (entry.name).split('_')
                        newkit = Matches()
                        newkit.type = 'FTDNA'
                        newkit.kit = s2[0]
                        newkit.name = ''
                        newkit.date = date(int(s2[4][0:4]), int(s2[4][5:7]), int(s2[4][8:10]))
                        newkit.read_ftdna_matchlist((dlpath + entry.name))
                        (self.lists).append(newkit)
        return True

    def month(s: str) -> int:
        match s[0]:
            case 'k':
                kk = 6
            case 'e':
                kk = 8
            case 's':
                kk = 9
            case 'l':
                kk = 10
            case 'j':
                kk = 12
            case 't':
                match s[1]:
                    case 'a':
                        return 1
                    case 'o':
                        return 5
                    case _:
                        return 0
            case 'h':
                match s[2]:
                    case 'u':
                        return 4
                    case 'e':
                        return 7
                    case _:
                        return 0
            case 'm':
                if s[2] != 'a':
                    return 0
                if s[3] == r:
                    return 11
                else:
                    if s[3] == 'a':
                        return 3
                    else:
                        return 0
            case _:
                return 0

    def get_MyHeritage_matchlists(self, dlpath : str = ''):
        if dlpath == '':
            self.lists = None
            return False

        with (os.scandir(dlpath) as entries):
            ind = 0
            for entry in entries:
                if ((entry.name).endswith('.csv')) and ('DNA-osumalista' in entry.name):
                    self.type = 'MyHeritage'
                    newkit = Matches()
                    newkit.type = 'MyHeritage'
                    newkit.kit = None
                    s = entry.name.split(' ')
                    newkit.name = s[0] + ' ' + s[1]
                    newkit.date = date(2023,8, 28)
                    newkit.read_MyHeritageMatchlist((dlpath + entry.name))
                    (self.lists).append(newkit)
        return False

    def show(self, mode : int = 1):
        for x in self.lists:
            x.show(mode)

    def sama_nimi(self, eka: str, toka: str) -> bool:
        if len(eka) != len(toka):
            return False
        for i in range(len(eka)):
            if eka[i] != toka[i]:
                return False
        return True

    def samoja(self, i_p: int, j_p: int) -> int:
        if self.lists[i_p].matchlist == None or self.lists[i_p].matchlist == None:
            return 0
        samoja = 0
        if self.lists[i_p].matchlist != None:
            for a in self.lists[i_p].matchlist:
                if self.lists[j_p].matchlist != None:
                    for b in self.lists[j_p].matchlist:
                        if self.sama_nimi(a[0], b[0]):
                            samoja += 1
        return samoja

    def findname(self, kit_p: str) -> str:
        for a in self.kitsnames:
            if a[0] == kit_p:
                return a[1]
        return 'Unknown'

    def mktable(self, mode=1):
        print('<html><head></head><body><table>')
        i = 0
        for row in self.lists:
            j = 0
            print('<tr>', end=" ")
            for col in self.lists:
                print('<th>', end=" ")
                print(self.samoja(i, j), end=" ")
                print('</th>', end=" ")
                j += 1
            print('</tr>')
            i += 1
        print('</table></body></html>')

    # Parameter mode_p
    # 0, only row number to left column number
    # 1, kit id and number of row to left
    # 2, name of tested person, kit id and row number to left
    def mkhtmltable(self, mode_p: int = 0):
        print('Making html-table...')
        mllength = len(self.lists)
        f = open("matchtable.html", "w")
        f.write('<html>\n<head>\n')
        f.write('<link rel="stylesheet" href="styles.css">\n')
        f.write('</head>\n')

        # Body. First table header to html file
        f.write('<body>\n<table>\n')
        s = '<tr><td colspan = "' + str(mllength+2) + '"class="TableHeader"><h1>Common Matches Table</h1></td></tr>\n'
        f.write(s)
        f.write('<tr><th colspan=2 id="Base">&nbsp;</th>')
        for ih in range(0, mllength):                           # Header row; kits numbers or identification
            f.write('<th>')
            f.write(str(ih+1))
            f.write('</th>')
        f.write('</tr>\n')

        i = 0                                                   # i is list index number and rows after headers start 0
        for row in self.lists:                                  # row index line
            f.write('<tr><th>')
            match self.lists[i].type[0]:
                case 'F':
                    f.write('FTDNA')
                case 'M':
                    f.write('MyHer')
                case _:
                    f.write('Unkn ')
            f.write('</th><th>')
            match mode_p:
                case 0:
                    f.write(str(i + 1))
                case 1:
                    if self.lists[i].kit != None:
                        s = self.lists[i].kit + ' ' + str(i+1)
                    else:
                        s = 'No id' + ' ' + str(i + 1)
                    f.write(s)
                case 2:
                    s = self.findname(self.lists[i].kit) + ' ' + str(i+1)
                    f.write(s)
                case _:
                    f.write('&nbsp')
            f.write('</th>')
            j = 0
            for i2 in range(0, i):                              # print common matches to diagonal - 1
                j += 1
                s = '<td class="Before">' + str(self.samoja(i, j)) + '</td>'
                f.write(s)
            if (self.lists[i]).matchlist != None:
                len3 = len( (self.lists[i]).matchlist)         # Diagonal is match list lenght (all are matches)
            else:
                len3 = 0
            s = '<td class="Diagonal">' + str(len3) + '</td>'
            f.write(s)
            for i3 in range(i+1, mllength):
                f.write('<td class="Rest">&nbsp;</td>')
            f.write('</tr>')
            i += 1
            if i % 5 == 0:
                print(i, end=" ")
            else:
                print('.', end=" ")

        f.write('\n</table>\n</body>\n</html>')
        f.close()

    def mllengths(self):
        i = 0
        for x in self.lists:
            print('i=', i, len(x.matchlist) )
            i += 1