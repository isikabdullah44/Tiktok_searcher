import datetime
import requests
import json

cookies = {
    'ttwid': '1%7CACMC-ule9G29bPvl7M-R0dUZRbXsrD2oomOrQeNF9zE%7C1659634704%7C31bb04347e14e389fa3f07d5af6f3b375f4e8745f72b55b31f978cfd1cc7f603'
}

ms_token = '045Qq_hhx-TyJVSVWnOMiwACTTDu9ve_UsnPRg_1W2m__MNNn9JPrvb9-UFX8eDJD84oup8s60JY6JRExJ5p28KlPqdaGHSUpCVArff2z7eTC2SC3tzWmzdWIkziFYAxe9ALGpQf'


def make_tiktok_search(keyword):
    tiktok_data = []
    variable_for_page = 0

    while True:
        page_number = variable_for_page * 10
        variable_for_page += 1
        response = requests.get(
            f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=tr-TR&app_name=tiktok_web&browser_language=tr-TR&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F15.5%20Safari%2F605.1.15&channel=tiktok_web&cookie_enabled=true&cursor={page_number}&device_id=7121962992141714946&device_platform=web_pc&focus_state=true&from_page=search&history_len=6&is_fullscreen=false&is_page_visible=true&keyword={keyword}&os=mac&priority_region=&referer=&region=TR&screen_height=1050&screen_width=1680&tz_name=Europe%2FIstanbul&webcast_language=tr-TR&msToken={ms_token}&X-Bogus=DFSzsIVOCatANxJRSIGDnc3WxM2p&_signature=_02B4Z6wo00001jKiCJAAAIDD16L5ufsRuPoyowwAAO6A1b',
            cookies=cookies, headers={})
        json_data = json.loads(response.text)

        if len(json_data['user_list']) < 1:
            break
        for number in json_data['user_list']:
            nick_name = number['user_info']['unique_id']
            followers_count = number['user_info']['follower_count']
            image_link = number['user_info']['avatar_thumb']['url_list']
            tiktok_dict = {
                "nickname": nick_name,
                "followers": followers_count,
                "profile_image": image_link
            }
            tiktok_data.append(tiktok_dict)
    return str(tiktok_data)


def save_on_file(result, name_of_file):
    today = datetime.date.today()
    with open(f'{name_of_file}:{today}.txt', 'w') as convert_file:
        convert_file.write(result)


def main():
    result = make_tiktok_search(keyword='simanur')
    save_on_file(result, name_of_file='simanur')


z = 0

try:
    while z < 3:
        main()
        z += 1
except:
    print("Data not found")
    print("Check your ms token and ttwid")
