#python3 -m pytest -s -v
#python3 -m pytest --alluredir=test_results/ tests/test_google_maps_api.py
#allure serve test_results/

import json
import allure
from utils.checking import Check
from utils.api import GoogleMapsApi


@allure.epic('Test create location')
class TestCreateLocation:

    @allure.description('Test creates, updates and deletes location')
    def test_create_new_location(self):

        print('POST Method')
        post_result = GoogleMapsApi.create_new_location()
        check_post = post_result.json()
        place_id = check_post.get('place_id')
        Check.check_status_code(post_result, 200)
        Check.check_json_token(post_result, ['status', 'place_id', 'scope', 'reference', 'id'])
#        token = json.loads(post_result.text)
#        print(list(token))
        Check.check_json_value(post_result, 'status', 'OK')

        print('GET POST Method')
        get_result = GoogleMapsApi.get_new_location(place_id)
        Check.check_status_code(get_result, 200)
        Check.check_json_token(get_result, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Check.check_json_value(get_result, 'address', '29, side layout, cohen 09')

        print('PUT Method')
        put_result = GoogleMapsApi.put_new_location(place_id)
        Check.check_status_code(put_result, 200)
        Check.check_json_token(put_result, ['msg'])
        Check.check_json_value(put_result, 'msg', 'Address successfully updated')

        print('GET PUT Method')
        get_result = GoogleMapsApi.get_new_location(place_id)
        Check.check_status_code(get_result, 200)
        Check.check_json_token(get_result, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Check.check_json_value(get_result, 'address', '100 Lenina street, RU')

        print('DELETE Method')
        delete_result = GoogleMapsApi.delete_new_location(place_id)
        Check.check_status_code(delete_result, 200)
        Check.check_json_token(delete_result, ['status'])
        Check.check_json_value(delete_result, 'status', 'OK')

        print('GET DELETE Method')
        get_result = GoogleMapsApi.get_new_location(place_id)
        Check.check_status_code(get_result, 404)
        Check.check_json_token(get_result, ['msg'])
        Check.check_json_value(get_result, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print('Test OK')
