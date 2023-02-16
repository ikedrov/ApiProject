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

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'{field_name} is right.')
