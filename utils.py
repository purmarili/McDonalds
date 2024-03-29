import hashlib

from db.dto.user_dto import UserDto
from models.enums import SessionKeyEnum
import requests
from bs4 import BeautifulSoup

REQUEST_HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def check_password(password: str, hashed_password: str) -> bool:
    if get_hashed_password(password) == hashed_password:
        return True
    return False


def get_hashed_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def assign_session_keys(user: UserDto, session_):
    session_[SessionKeyEnum.ID.value] = user.id
    session_[SessionKeyEnum.USERNAME.value] = user.username
    session_[SessionKeyEnum.AUTHORIZED.value] = True


def clear_session_keys(session_):
    session_.pop(SessionKeyEnum.ID.value, None)
    session_.pop(SessionKeyEnum.USERNAME.value, None)
    session_.pop(SessionKeyEnum.AUTHORIZED.value, None)


def get_movie_info(li):
    image_url = li.find('img').get('src')
    top_250_rating, title = li.find('h3', class_='ipc-title__text').text.split('.', 1)
    title = title[1:]
    metadata = li.find('div', class_='cli-title-metadata').findChildren()
    year = int(metadata[0].text)
    time = metadata[1].text
    rating, rating_count = li.find('span', class_='ipc-rating-star--imdb').text.split('\xa0')

    return image_url, top_250_rating, title, year, time, rating, rating_count


async def get_cast_info(li):
    result = {
        'image_url': [],
        'full_name': [],
        'movie_name': []
    }
    link = li.find('a', class_='ipc-title-link-wrapper').get('href')
    link = 'https://www.imdb.com' + link
    response = requests.get(link, headers=REQUEST_HEADERS)
    cast_html = BeautifulSoup(response.text, 'html.parser')
    cast_items = cast_html.find_all('div', class_='sc-bfec09a1-5 hNfYaW')
    for item in cast_items:
        try:
            image_url = item.find('img', class_='ipc-image').get('src')
        except AttributeError:
            image_url = None

        full_name = item.find('a', class_='sc-bfec09a1-1 gCQkeh').text

        try:
            movie_name = item.find('span', class_='sc-bfec09a1-4 kvTUwN').text
        except AttributeError:
            movie_name = None

        result['image_url'].append(image_url)
        result['full_name'].append(full_name)
        result['movie_name'].append(movie_name)
    return result

