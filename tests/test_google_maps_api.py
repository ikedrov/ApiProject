#python3 -m pytest -s -v


from utils.api import GoogleMapsApi


class Test_create_location:

    def test_create_new_location(self):

        print('POST Method')
        post_result = GoogleMapsApi.create_new_location()
        check_post = post_result.json()
        place_id = check_post.get('place_id')

        print('GET POST Method')
        get_result = GoogleMapsApi.get_new_location(place_id)

        print('PUT Method')
        put_result = GoogleMapsApi.put_new_location(place_id)

        print('GET PUT Method')
        get_result = GoogleMapsApi.get_new_location(place_id)

        print('DELETE Method')
        put_result = GoogleMapsApi.delete_new_location(place_id)

        print('GET DELETE Method')
        get_result = GoogleMapsApi.get_new_location(place_id)