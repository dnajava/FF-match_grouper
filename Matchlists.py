import os
from datetime import date
from Matches import Matches

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
                print('<td>', end=" ")
                print(self.samoja(i, j), end=" ")
                print('</td>', end=" ")
                j += 1
            print('</tr>')
            i += 1
        print('</table></body></html>')

    def mkhtmltable(self, mode=1):
        print('Making html-table...')
        length = len(self.lists)
        f = open("matchtable.html", "w")
        f.write('<html><head>')
        f.write('< link rel = "stylesheet" href = "styles.css">')
        f.write('</head><body><table>')
        f.write('<tr><td colspan = "')
        f.write(str(len(self.lists)))
        f.write('"><h1>Common Matches Table</h1></td></tr>')
        i = 0
        for row in self.lists:
            j = 0
            f.write('<tr>')
            for col in self.lists:
                f.write('<td>')
                if i < j:
                    f.write(str(self.samoja(i,j)))
                    if i == j:
                        f.write(str(len(self.lists[i]).matchlist))
                        print('( x . x )', end=" ")
                    else:
                        f.write('&nbsp;')
                        print('(   .   )', end=" ")
                f.write('</td>')
                j += 1
            f.write('</tr>')
            print()
            i += 1
        f.write('</table></body></html>')
        f.close()
        print()
