# FF match grouper
# Ilpo Kantonen 27 August 2023

from Matchlists import Matchlists

if __name__ == '__main__':
    ml = Matchlists()
    ml.get_matchlists('/path/to/downloads/')

    ml.mkhtmltable()
