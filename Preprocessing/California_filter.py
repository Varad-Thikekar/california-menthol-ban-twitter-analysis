import requests
import ujson

class CityFilter:

    keywords = set()
    def main(self):
        self.california_cities = self.get_california_cities()
        self.califirnia_counties = self.get_california_counties()
        for city_name in self.california_cities:
            city_name = city_name[:-17]
            if ' ' in city_name:
                self.keywords.add(city_name.lower())
                self.keywords.add((''.join(city_name.split())).lower())

            else:
                self.keywords.add(city_name.lower())

        for county_name in self.califirnia_counties:
            county_name = county_name[:-19]
            if ' ' in county_name:
                self.keywords.add(county_name.lower())
                self.keywords.add((''.join(county_name.split())).lower())

            else:
                self.keywords.add(county_name.lower())

        print(self.keywords)
        self.remove()

    def get_california_cities(self):
        base_url = "https://api.census.gov/data/2019/pep/population"
        state = "06"  # California's state code
        level = "place"  # Indicates places (cities and towns)

        # API request to fetch cities and towns in California
        response = requests.get(
            f"{base_url}?get=NAME&for={level}:*&in=state:{state}"
        )

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            cities = [place[0] for place in data[1:]]  # Extract city names from response
            return cities
        else:
            print("Error fetching data:", response.status_code)
            return None

    def get_california_counties(self):

        base_url = "https://api.census.gov/data/2019/pep/population"
        state = "06"  # California's state code
        level = "county"  # Indicates counties

        # API request to fetch counties in California
        response = requests.get(
            f"{base_url}?get=NAME&for={level}:*&in=state:{state}"
        )

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            counties = [place[0] for place in data[1:]]  # Extract county names from response
            return counties
        else:
            print("Error fetching data:", response.status_code)

    def contains(self, line):  # detect whether the twitter content contains location keywords

        if line['user']['location']:
            location = line['user']['location']
        else: return False

        location = location.lower()

        for s in self.keywords:
            if (s in location):
                return True
        return False


    def remove(self):
        with open("tempcal2.json", 'w') as output:  # Output filename changed to .txt
            with open("product_juul_filtered.json", 'r') as src:
                temp=0
                for line in src:
                    parsedJsonRecord = ujson.decode(line)
                    if self.contains(parsedJsonRecord):

                        output.write(ujson.dumps(parsedJsonRecord) + '\n')


        output.close()
        src.close()




if __name__ == '__main__':
    CityFilter().main()

