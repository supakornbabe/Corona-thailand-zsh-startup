import requests


def get_json_data():
    r = requests.get(
        'https://covid19-cdn.workpointnews.com/api/constants.json')
    return r.json()


if __name__ == "__main__":
    data = get_json_data()
    print('🗓  {}'.format(data['เพิ่มวันที่']), end=' -> ')
    print('🦠  {}'.format(data['ผู้ติดเชื้อ']), end=' ')
    print('(🔺  {})'.format(data['เพิ่มวันนี้']), end=' | ')
    print('🥳  {}'.format(data['หายแล้ว']), end=' | ')
    print('🏥  {}'.format(data['กำลังรักษา']), end=' | ')
    print('⚰️  {}'.format(data['เสียชีวิต']))
