# FF match grouper
# Ilpo Kantonen 27 August 2023

from Matchlists import Matchlists

if __name__ == '__main__':
    ml = Matchlists()
    ml.get_matchlists('/path/to/data/')

    # Parameter:
    # 0, only row number to left column number
    # 1, kit id and number of row to left
    # 2, name of tested person, kit id and row number to left
    ml.mkhtmltable(2)

    # ml.mllengths()
