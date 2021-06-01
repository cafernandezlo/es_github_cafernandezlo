#!/usr/bin/env python3

from scholarly import scholarly

AUTHOR                  = 'Fernandez-Lozano, Carlos'
SCHOLARLY_FILL_SECTIONS = ['indices']


# https://scholarly.readthedocs.io/en/latest/quickstart.html#fill-the-author-and-publications-container-objects-with-additional-information
search_query = scholarly.search_author(AUTHOR)
author       = next(search_query)
data         = scholarly.fill(author, sections = SCHOLARLY_FILL_SECTIONS)
print(f'''citedby: {data['citedby']}
hindex: {data['hindex']}''')
