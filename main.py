# FF match grouper
# Ilpo Kantonen 27 August 2023

from Matchlists import Matchlists

if __name__ == '__main__':
    DL = '/path/to/matchlists/directpry/'
    debug = 0

    ml = Matchlists()
    ml.get_FTDNA_matchlists(DL, debug)
    ml.get_MyHeritage_matchlists(DL, debug)
    ml.readkitsnames()


    '''
    # Parameter:
    0, only row number to left column number
    1, kit id and number of row to left
    2, name of tested person, kit id and row number to left
    '''
    ml.mkhtmltable(2)
