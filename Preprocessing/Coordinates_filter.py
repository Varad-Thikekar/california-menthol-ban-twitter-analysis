import ujson
from shapely.geometry import Point, shape
import fiona
from geopy.geocoders import Nominatim
import ssl
import certifi
class LocationFilter:

    missed = 0
    def main(self):
        # self.context = ssl.create_default_context(cafile=certifi.where())
        # self.geolocator = Nominatim(user_agent="Varads_project", ssl_context=self.context)

        # Load the California shapefile
        with fiona.open("ca_state_boundaries.shp") as shp:
            self.california_boundary = shape(shp[0]['geometry'])

        self.remove()

    def contains(self,line,counter):
        try: # it throws error after a few requests
            self.context = ssl.create_default_context(cafile=certifi.where())
            name = 'varad'+str(counter)
            self.geolocator = Nominatim(user_agent=name, ssl_context=self.context)
            location = line['user']['location']
            if location:
                location_info = self.geolocator.geocode(location)
                if location_info:
                    raw_data = location_info.raw
                    lat = raw_data['lat']
                    long = raw_data['lon']  

                    point_to_check = Point(long, lat)  # Longitude, Latitude

                    # Check if the point is within California
                    if self.california_boundary.contains(point_to_check):
                        return True
                    else:
                        return False
        except:
            print(counter)
            self.missed += 1
            return False


    def remove(self):
        with open("alternative_final_tweets.json", 'w') as output:  # Output filename changed to .txt
            with open("new_filtered_promo_tweets.json", 'r') as src:
                counter=0
                for line in src:
                    parsedJsonRecord = ujson.decode(line)
                    counter+=1
                    if self.contains(parsedJsonRecord,counter):
                        output.write(ujson.dumps(parsedJsonRecord) + '\n')


        output.close()
        src.close()
        print(self.missed)


if __name__ == '__main__':
    LocationFilter().main()