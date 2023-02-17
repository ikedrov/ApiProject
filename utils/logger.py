import datetime
import os


class Logger:
    file_name = f'logs/log_' + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.log'

    @classmethod
    def write_log_to_file(cls, data: str):

        with open(cls.file_name, 'a+', encoding='utf-8') as file:
            file.write(data)

    @classmethod
    def add_request(cls, url: str, method: str):

        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        add_data = f'\n-----\n'
        add_data += f'Test: {test_name}\n'
        add_data += f'Time: {str(datetime.datetime.now())}\n'
        add_data += f'Request: {method}\n'
        add_data += f'Request URL: {url}\n'
        add_data += '\n'

        cls.write_log_to_file(add_data)

    @classmethod
    def add_response(cls, result):

        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        add_data = f'Response code: {result.status_code}\n'
        add_data += f'Response text: {result.text}\n'
        add_data += f'Response headers: {headers_as_dict}\n'
        add_data += f'Response cookies: {cookies_as_dict}\n'
        add_data += f'\n-----\n'

        cls.write_log_to_file(add_data)

