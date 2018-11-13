#!/usr/bin/python

import sys
import csv
import urllib2
import urllib

if __name__ == "__main__":

    if len(sys.argv) == 2:
        collection = 'Q21542493'
        csvfile = sys.argv[1]
    elif len(sys.argv) != 2 and len(sys.argv) != 3:
        print ('Usage:\n\taddWikiManifest.py [collection Q id] [csv_out]')
        sys.exit(-1)
    else:    
        collection = sys.argv[1]
        csvfile = sys.argv[2]

    query  = """
                SELECT ?object ?objectLabel ?handle
                WHERE
                {
                  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . } 
                   ?object wdt:P361 wd:%s .
                   ?object wdt:P1184 ?handle
                } 
            """ 
    query = query.strip() % collection        
    url = 'https://query.wikidata.org/sparql?query=%s' % urllib.quote_plus(query)
    req = urllib2.Request(url)
    req.add_header('Accept', 'text/csv')
    response = urllib2.urlopen(req)
    cr = csv.reader(response)
    with open(csvfile, 'wb') as csvfile:
        newfile = csv.writer(csvfile)

        titleRow = True
        for row in cr:
            print row
            if titleRow:
                titleRow = False
                newfile.writerow([row[0],row[1],row[2],"Manifest"])
            else:    
                pid = row[2].split('/')[1]
                manifest = 'https://damsssl.llgc.org.uk/iiif/2.0/%s/manifest.json' % pid
                newfile.writerow([row[0],row[1],row[2],manifest])

