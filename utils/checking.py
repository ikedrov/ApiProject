import json


class Check:

    @staticmethod
    def check_status_code(result, status_code):

        assert status_code == result.status_code
        print(f'Success. Status code: {str(result.status_code)}')

    @staticmethod
    def check_json_token(result, expected_value):

        token = json.loads(result.text)
        assert list(token) == expected_value
        print('All fields are present.')
