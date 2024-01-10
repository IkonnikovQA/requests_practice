import requests
import json

def get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    for x in response:
        print(x)
        # print(x['title'])

get_all_posts()

def get_one_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/42').json()
    print(response)

get_one_post()

def post_new_post():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = json.dumps({
        "title": "foo",
        "body": "bar",
        "userId": 1
    })
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data = body, headers = headers)
    print(response.json())

post_new_post()

def update_post():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = json.dumps({
        "title": "foo1",
        "body": "bar2",
        "userId": 1
    })
    response = requests.put('https://jsonplaceholder.typicode.com/posts/42', data = body, headers = headers)
    print(response.json())

update_post()

def patch_post():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = json.dumps({
        "title": "foo1",
        "userId": 1
    })
    response = requests.patch('https://jsonplaceholder.typicode.com/posts/42', data=body, headers=headers)
    print(response.json())


patch_post()

def delete_post():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/42')
    print(response.text)
    print(response.status_code)

delete_post()