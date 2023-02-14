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

    @staticmethod
    def get_new_location(place_id):

        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        get_result = HttpMethods.get(get_url)
        print(get_result.text)
        return get_result

    @staticmethod
    def put_new_location(place_id):
        put_resource = '/maps/api/place/update/json'
        put_url = base_url + put_resource + key
        print(put_url)
        json_to_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        put_result = HttpMethods.put(put_url, json_to_update_new_location)
        print(put_result.text)
        return put_result

    @staticmethod
    def delete_new_location(place_id):
        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_to_delete_new_location = {
            "place_id": place_id
        }
        delete_result = HttpMethods.delete(delete_url, json_to_delete_new_location)
        print(delete_result.text)
        return delete_result
