#python3 -m pytest -s -v
import json

from utils.checking import Check
from utils.api import GoogleMapsApi


class Test_create_location:

    def test_create_new_location(self):

        print('POST Method')
        post_result = GoogleMapsApi.create_new_location()
        check_post = post_result.json()
        place_id = check_post.get('place_id')
        Check.check_status_code(post_result, 200)
        Check.check_json_token(post_result, ['status', 'place_id', 'scope', 'reference', 'id'])
#        token = json.loads(post_result.text)
#        print(list(token))

        print('GET POST Method')
        get_result = GoogleMapsApi.get_new_location(place_id)
        Check.check_status_code(get_result, 200)
        Check.check_json_token(get_result, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print('PUT Method')
        put_result = GoogleMapsApi.put_new_location(place_id)
        Check.check_status_code(put_result, 200)
        Check.check_json_token(put_result, ['msg'])

        print('GET PUT Method')
        get_result = GoogleMapsApi.get_new_location(place_id)
        Check.check_status_code(get_result, 200)
        Check.check_json_token(get_result, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print('DELETE Method')
        delete_result = GoogleMapsApi.delete_new_location(place_id)
        Check.check_status_code(delete_result, 200)
        Check.check_json_token(delete_result, ['status'])

        print('GET DELETE Method')
        get_result = GoogleMapsApi.get_new_location(place_id)
        Check.check_status_code(get_result, 404)
        Check.check_json_token(get_result, ['msg'])

        print('Test OK')
