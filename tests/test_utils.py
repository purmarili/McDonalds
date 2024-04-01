import asyncio
import pickle
import unittest
from unittest.mock import patch, MagicMock

from db.dto.user_dto import UserDto
from models.enums import SessionKeyEnum
from utils import get_hashed_password, check_password, assign_session_keys, clear_session_keys, get_cast_info


class TestUtils(unittest.TestCase):
    def test_get_hashed_password(self):
        self.assertEqual(get_hashed_password('password123'),
                         'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f')
        with self.assertRaises(ValueError):
            get_hashed_password('')
        with self.assertRaises(ValueError):
            get_hashed_password(None)
        with self.assertRaises(ValueError):
            get_hashed_password('asdf')
        with self.assertRaises(ValueError):
            get_hashed_password('hellohellohellohellohello')

    def test_check_password(self):
        self.assertEqual(check_password(
            password='password123',
            hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f'),
            True)
        self.assertTrue(check_password(
            password='password123',
            hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f'))
        self.assertFalse(check_password(
            password='password12',
            hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f'))
        with self.assertRaises(ValueError):
            check_password(password='',
                           hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f')

    def test_assign_session_keys(self):
        dc = {}
        assign_session_keys(user=UserDto(id=1, username='user'), session_=dc)
        self.assertTrue(dc.get(SessionKeyEnum.AUTHORIZED.value, False))
        self.assertEqual(dc.get(SessionKeyEnum.ID.value, None), 1)
        self.assertEqual(dc.get(SessionKeyEnum.USERNAME.value, None), 'user')

    def test_clear_session_keys(self):
        dc = {}
        assign_session_keys(user=UserDto(id=1, username='user'), session_=dc)
        clear_session_keys(session_=dc)
        self.assertIsNone(dc.get(SessionKeyEnum.AUTHORIZED.value))
        self.assertIsNone(dc.get(SessionKeyEnum.ID.value))
        self.assertIsNone(dc.get(SessionKeyEnum.USERNAME.value))

    @patch('utils.requests.get')
    def test_get_cast_info(self, mock_get):
        # Mock the response.text of requests.get
        mock_get.return_value = pickle.load(open('files/cast_li.pickle', 'rb'))

        # Create a mock for `li` to simulate find().get() returning a specific href
        mock_li = MagicMock()
        mock_a_tag = MagicMock()
        mock_a_tag.get.return_value = '/title/tt0111161/'  # Mocked href value
        mock_li.find.return_value = mock_a_tag

        # Call get_cast_info with the mocked `li`
        result = asyncio.run(get_cast_info(mock_li))

        # Your assertions here
        self.assertIsInstance(result, dict)
