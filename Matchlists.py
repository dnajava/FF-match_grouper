import os
from datetime import date
from Matches import Matches
from KitNames import KitNames

names = [
    'Pekka Hietala',
    'Jorma Hietala',
    'Mauri Peltola',
    'Johannes Sankari',
    'Marja Kantonen',
    'Outi Nieminen',
    'Paavo Vuorialho',
    'Matti Matikainen',
    'Taru Kantonen',
    'Ritva Kantonen',
    'Nisa Khan',
    'Terttu Hietala',
    'Ilpo Kantonen',
    'Timo Rehtonen']

class Matchlists:
    lists = []

    def __Matchlists(self):
        lists = []

    def __getitem__(self):
        return self.lists

    def get_matchlists(self, dlpath=''):
        if dlpath == '':
            self.lists = None
            return False

        with os.scandir(dlpath) as entries:
            for entry in entries:
                if (entry.name).endswith('.csv'):
                    if ('Family' in entry.name and 'Finder' in entry.name and 'Matches' in entry.name):
                        s2 = (entry.name).split('_')
                        dday = date(int(s2[4][0:4]), int(s2[4][5:7]), int(s2[4][8:10]))
                        newkit = Matches()
                        newkit.setkit(s2[0])
                        newkit.setday(dday)
                        newkit.read_matchlist((dlpath + entry.name))
                        (self.lists).append(newkit)
        return True

    def show(self, mode=1):
        for x in self.lists:
            x.show(mode)

    def sama_nimi(self, eka, toka) -> bool:
        if len(eka) != len(toka):
            return False
        for i in range(len(eka)):
            if eka[i] != toka[i]:
                return False
        return True

    def samoja(self, i_p : int, j_p : int):
        samoja = 0
        for a in self.lists[i_p].matchlist:
            for b in self.lists[j_p].matchlist:
                if self.sama_nimi(a[0], b[0]):
                    samoja += 1
                # table.add(xamoja)
        return samoja

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

    def mkhtmltable(self, mode_p=0):
        print('Making html-table...')
        mllength = len(self.lists)
        f = open("matchtable.html", "w")
        f.write('<html>\n<head>\n')
        f.write('<link rel="stylesheet" href="styles.css">\n')
        f.write('</head>\n')

        # Body. First table header to html file
        f.write('<body>\n<table>\n')
        s = '<tr><td colspan = "' + str(mllength+1) + '"class="TableHeader"><h1>Common Matches Table</h1></td></tr>\n'
        f.write(s)
        f.write('<tr><th id="Base">&nbsp;</th>')
        for ih in range(0, mllength):                           # Header row; kits numbers or identification
            f.write('<th>')
            f.write(str(ih+1))
            f.write('</th>')
        f.write('</tr>\n')

        i = 0                                                   # i is list index number and rows after headers start 0
        for row in self.lists:                                  # row index line
            f.write('<tr><th>')
            match mode_p:
                case 0:
                    f.write(str(i + 1))
                case 1:
                    s = list[i].kit + str(i+1)
                    f.write(s)
                case 2:
                    s = self.lists[i].kit + ' ' + str(i + 1)
                    f.write(s)
                case 3:
                    s = names[i] + ' ' + self.lists[i].kit + ' ' + str(i+1)
                    f.write(s)
                case _:
                    f.write('&nbsp')
            f.write('</th>')
            j = 0
            for i2 in range(0, i):                              # print common matches to diagonal - 1
                j += 1
                s = '<td class="Before">' + str(self.samoja(i,j)) + '</td>'
                f.write(s)
            len3 = len(self.lists[i].matchlist)                 # Diagonal is match list lenght (all are matches)
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