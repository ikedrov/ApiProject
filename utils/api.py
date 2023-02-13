from utils.http_methods import HttpMethods

base_url = 'https://rahulshettyacademy.com'
key = '?key=qaclick123'


class GoogleMapsApi:

    @staticmethod
    def create_new_location():

        json_to_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = '/maps/api/place/add/json'
        post_url = base_url + post_resource + key
        print(post_url)
        post_result = HttpMethods.post(post_url, json_to_create_new_location)
        print(post_result.text)
        return post_result
    
