'''
Необходимо написать клиент к API VK , который будет считать распределение возрастов друзей для указанного пользователя.

На вход подается username или user_id пользователя.
На выходе получаем список пар (<возраст>, <количество друзей с таким возрастом>),
отсортированный по убыванию по второму ключу (количество друзей) и по возрастанию по первому ключу (возраст).

Например:
[(26, 8), (21, 6), (22, 6), (40, 2), (19, 1), (20, 1)]

'''

# HTTPS
import requests
from datetime import datetime
from requests.exceptions import HTTPError

# CONSTANTS
MY_ID = 'id312432661'
NAYDIN_ID = 'o.s.naydin'
ACCESS_TOKEN = 'e6c870a0e6c870a0e6c870a0e6e6a15244ee6c8e6c870a0ba496cb35b9f3a17905352b0'
API_VERSION = '5.71'
API_VERSION_F = '5.71'
TIMEOUT = (3, 5)

URL_USERS_GET = 'https://api.vk.com/method/users.get'
URL_FRIENDS_GET = f'https://api.vk.com/method/friends.get'

base_payload = {'v': API_VERSION, 'access_token': ACCESS_TOKEN, 'timeout': TIMEOUT}


def get_id(user_ids):
    ids = []
    try:
        # Using this method we can merge old dictionary and new key/value pair in another dictionary
        r1 = requests.get(URL_USERS_GET,
                          params={**base_payload, **{'user_ids': ','.join(user_ids)}})
        data = r1.json()

        for i in range(len(user_ids)):
            ids.append(data['response'][i]['id'])

        # If the response was successful, no Exception will be raised
        r1.raise_for_status()
        return ids
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6


def get_friends(user_id):
    user_id = get_id({user_id})[0]
    r1 = requests.get(URL_FRIENDS_GET, params={
        **{'v': API_VERSION_F, 'access_token': ACCESS_TOKEN, 'fields': 'bdate', 'timeout': TIMEOUT},
        **{'user_id': user_id}})
    data = r1.json()
    friends_age_dict = {}

    for i in range(data['response']['count']):
        row = data['response']['items'][i]
        if ('bdate' in row) and len(row['bdate'].split('.')) == 3:  # 'bdate' is present and has year
            # bdate = datetime(*map(int, reversed(row['bdate'].split('.'))))
            # age = int((datetime.now() - bdate).days / 365.2425)

            byear = int(row['bdate'].split('.')[2])
            age = datetime.now().year - byear
            friends_age_dict[row['id']] = age

    return friends_age_dict


def calc_age(user_id):
    friends_age_dict = get_friends(user_id)
    age_friendscount_dict = {}
    for k, v in friends_age_dict.items():
        if v in age_friendscount_dict:
            age_friendscount_dict[v] += 1
        else:
            age_friendscount_dict[v] = 1

    # print(friends_age_dict)
    # print(age_friendscount_dict)
    # print(list(age_friendscount_dict.items()))

    age_friendscount_list = list(age_friendscount_dict.items())
    result = sorted(age_friendscount_list, key=lambda x: (-x[1], x[0]))

    return result


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
    '''
    print(calc_age(MY_ID))
    # print(get_id({MY_ID, NAYDIN_ID}))
    # print(get_id({MY_ID})[0])
    # data = get_friends(get_id({MY_ID})[0])

    # print(get_friends(get_id({MY_ID})[0]))
    # print(json.dumps(data, indent=2, sort_keys=False))
    # res = calc_age(USER_ID)
    # print(res)
    '''
