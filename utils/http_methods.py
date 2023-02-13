import requests


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookies = ''

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result

    @staticmethod
    def put(url):
        result = requests.put(url, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result

    @staticmethod
    def delete(url):
        result = requests.delete(url, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result

