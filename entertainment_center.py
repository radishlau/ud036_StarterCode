"""This module creates a movie list object and pass it to fresh_tomatoes to
generate a website"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

# Construct some movies
CASINO_ROYALE = media.Movie("Casino Royale",
                            "Bond got betrayed...",
                            "http://vignette4.wikia.nocookie.net/jamesbond/images/d/df/Casino_Royale_poster.jpeg/revision/latest?cb=20120329172248",  # NOQA
                            "36mnx8dBbGE")

HANA_AND_ALICE = media.Movie("花與愛麗絲",
                             "Alice and Hana are best friends. But they fell "
                             "in love with the same guy...",
                             "http://iv1.lisimg.com/image/3167762/600full-hana-and-alice-poster.jpg",  # NOQA
                             "-t3t47w2z8I")

summer = media.Movie("(500) Days of Summer",
                     "On January 8, Tom Hansen meets Summer Finn, his boss's "
                     "new assistant...",
                     "https://upload.wikimedia.org/wikipedia/en/d/d1/Five_hundred_days_of_summer.jpg",  # NOQA
                     "PsD0NpFSADM")

# A list of moview
MOVIES = [CASINO_ROYALE, HANA_AND_ALICE, summer]

# Generate a website and open it
fresh_tomatoes.open_movies_page(MOVIES)
