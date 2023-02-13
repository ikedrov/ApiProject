#python3 -m pytest -s -v


from utils.api import GoogleMapsApi


class Test_create_location:

    def test_create_new_location(self):

        print('POST Method')
        post_result = GoogleMapsApi.create_new_location()