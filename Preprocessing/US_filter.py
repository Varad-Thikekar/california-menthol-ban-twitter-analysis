import ujson
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import csv
import re
from pandas import DataFrame


class US_filter:
    keywords1 = ['United States','Alabama', 'Nebraska', 'Nevada', 'New Hampshire', 'New Mexico',
                  'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Pennsylvania',
                  'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Vermont', 'Virginia',
                  'West Virginia', 'Wisconsin', 'Wyoming', 'Arizona', 'Arkansas', 'California',
                  'Colorado', 'Delaware', 'Florida', 'Georgia', 'Indiana', 'Iowa', 'Kansas',
                  'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Minnesota', 'New Hampshire', 'New Mexico',
                  'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego',
                  'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus',
                  'Charlotte', 'Indianapolis', 'Denver', 'El Paso', 'Nashville',
                  'Memphis', 'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore', 'Milwaukee',
                  'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Atlanta', 'Kansas City',
                  'Colorado Springs', 'Miami', 'Raleigh', 'Omaha', 'Long Beach', 'Virginia Beach', 'Oakland',
                  'Minneapolis', 'Tulsa', 'Arlington', 'Tampa', 'New Orleans', 'Bakersfield', 'Cleveland',
                  'Aurora', 'Anaheim', 'Santa Ana', 'Riverside', 'Corpus Christi', 'Lexington', 'Henderson',
                  'Stockton', 'Saint Paul', 'Cincinnati', 'St. Louis', 'Pittsburgh', 'Greensboro', 'Lincoln',
                  'Anchorage', 'Plano', 'Orlando', 'Irvine', 'Durham', 'Chula Vista', 'Toledo', 'Fort Wayne',
                  'St. Petersburg', 'Laredo', 'Chandler', 'Madison', 'Lubbock', 'Scottsdale', 'Reno',
                  'Gilbert', 'Glendale', 'North Las Vegas', 'Winston–Salem', 'Chesapeake', 'Norfolk', 'Fremont',
                  'Garland', 'Irving', 'Hialeah', 'Richmond', 'Baton Rouge']
    keywords1 = [x.lower() for x in keywords1]
    keywords2 = ['USA', 'US'," AL", " AK", " AZ", " AR", " CA", " CT", " DC",
                      " DE", " FL", " GA", " HI", " ID", " IL", " IN", " IA", " KS", " KY",
                      " LA", " ME", " MD", " MN", " MS",
                      " MT", " NE", " NV", " NH", " NM", " NC", " ND",
                      " OH", " OK", " PA", " SC", " SD", " TN",
                      " TX", " VT", " VA", " WV", " WI", " WY"]
    keywords2 = [x.lower() for x in keywords2]

    keywords = set(keywords1 + keywords2)
    # keywords = keywords1 + keywords2



    def main(self):
        self.filter()

    def contains(self, line):  # detect whether the username contains promotion keywords
        location = ""
        if "user" in line:
            if "location" in line["user"]:
                location = line["user"]["location"]

        if not location: return False
        location = location.lower()

        for s in self.keywords:
            if (s in location):
                return True
        return False


    def filter(self):
        with open("temp2.json", 'w') as output:  # output file
            with open("product_juul_filtered.json", 'rb') as src:  # input file
                for line in src:
                    parsedJsonRecord = ujson.decode(line)
                    if self.contains(parsedJsonRecord):
                        output.write(ujson.dumps(parsedJsonRecord) + '\n')
        output.close()
        src.close()


if __name__ == '__main__':
    US_filter().main()