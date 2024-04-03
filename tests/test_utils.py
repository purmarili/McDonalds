# # import asyncio
# # import pickle
# # import unittest
# # from unittest.mock import patch, MagicMock
# #
# # from db.dto.user_dto import UserDto
# # from models.enums import SessionKeyEnum
# # from utils import get_hashed_password, check_password, assign_session_keys, clear_session_keys, get_cast_info
# #
# #
# # class TestUtils(unittest.TestCase):
# #     def test_get_hashed_password(self):
# #         self.assertEqual(get_hashed_password('password123'),
# #                          'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f')
# #         with self.assertRaises(ValueError):
# #             get_hashed_password('')
# #         with self.assertRaises(ValueError):
# #             get_hashed_password(None)
# #         with self.assertRaises(ValueError):
# #             get_hashed_password('asdf')
# #         with self.assertRaises(ValueError):
# #             get_hashed_password('hellohellohellohellohello')
# #
# #     def test_check_password(self):
# #         self.assertEqual(check_password(
# #             password='password123',
# #             hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f'),
# #             True)
# #         self.assertTrue(check_password(
# #             password='password123',
# #             hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f'))
# #         self.assertFalse(check_password(
# #             password='password12',
# #             hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f'))
# #         with self.assertRaises(ValueError):
# #             check_password(password='',
# #                            hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f')
# #
# #     def test_assign_session_keys(self):
# #         dc = {}
# #         assign_session_keys(user=UserDto(id=1, username='user'), session_=dc)
# #         self.assertTrue(dc.get(SessionKeyEnum.AUTHORIZED.value, False))
# #         self.assertEqual(dc.get(SessionKeyEnum.ID.value, None), 1)
# #         self.assertEqual(dc.get(SessionKeyEnum.USERNAME.value, None), 'user')
# #
# #     def test_clear_session_keys(self):
# #         dc = {}
# #         assign_session_keys(user=UserDto(id=1, username='user'), session_=dc)
# #         clear_session_keys(session_=dc)
# #         self.assertIsNone(dc.get(SessionKeyEnum.AUTHORIZED.value))
# #         self.assertIsNone(dc.get(SessionKeyEnum.ID.value))
# #         self.assertIsNone(dc.get(SessionKeyEnum.USERNAME.value))
# #
# #     @patch('utils.requests.get')
# #     def test_get_cast_info(self, mock_get):
# #         # Mock the response.text of requests.get
# #         mock_get.return_value = pickle.load(open('files/cast_li.pickle', 'rb'))
# #
# #         # Create a mock for `li` to simulate find().get() returning a specific href
# #         mock_li = MagicMock()
# #         mock_a_tag = MagicMock()
# #         mock_a_tag.get.return_value = '/title/tt0111161/'  # Mocked href value
# #         mock_li.find.return_value = mock_a_tag
# #
# #         # Call get_cast_info with the mocked `li`
# #         result = asyncio.run(get_cast_info(mock_li))
# #
# #         # Your assertions here
# #         self.assertIsInstance(result, dict)
# import pickle
# import time
#
# import pytest
#
# from db.dto.user_dto import UserDto
# from models.enums import SessionKeyEnum
# from utils import get_hashed_password, check_password, assign_session_keys, clear_session_keys
#
# TEMP_VAR = 'hello'
#
#
# @pytest.mark.order(1)
# @pytest.mark.parametrize("x, y, expected",
#                          [(1, 2, 3),
#                           (4, 5, 9),
#                           (10, 20, 30)])
# def test_get_hashed_password(numbers, x, y, expected):
#     assert x + y == expected
#     if x == 10:
#         assert numbers == [i for i in range(10)]
#         numbers.append(10)
#     assert get_hashed_password('password123') == 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f'
#     with pytest.raises(ValueError):
#         get_hashed_password('')
#     with pytest.raises(ValueError):
#         get_hashed_password(None)
#     with pytest.raises(ValueError):
#         get_hashed_password('asdf')
#     with pytest.raises(ValueError):
#         get_hashed_password('hellohellohellohellohello')
#
#
# @pytest.mark.order(2)
# def test_check_password(numbers):
#     assert numbers == [i for i in range(11)]
#     numbers.append(11)
#     assert check_password(
#         password='password123',
#         hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f') == True
#     assert check_password(
#         password='password123',
#         hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f') == True
#     assert check_password(
#         password='password12',
#         hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f') == False
#     with pytest.raises(ValueError):
#         check_password(password='',
#                        hashed_password='ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f')
#
#
# @pytest.mark.order(3)
# def test_assign_session_keys(numbers):
#     assert numbers == [i for i in range(12)]
#     numbers.append(12)
#     dc = {}
#     assign_session_keys(user=UserDto(id=1, username='user'), session_=dc)
#     assert dc.get(SessionKeyEnum.AUTHORIZED.value, False) == True
#     assert dc.get(SessionKeyEnum.ID.value, None) == 1
#     assert dc.get(SessionKeyEnum.USERNAME.value, None) == 'user'
#
#
# # @pytest.mark.skipif(TEMP_VAR == 'hell', reason='TEST')
# # @pytest.mark.xfail
# @pytest.mark.order(4)
# def test_clear_session_keys(numbers):
#     assert numbers == [i for i in range(13)]
#     dc = {}
#     assign_session_keys(user=UserDto(id=1, username='user'), session_=dc)
#     clear_session_keys(session_=dc)
#     assert dc.get(SessionKeyEnum.AUTHORIZED.value) is None
#     assert dc.get(SessionKeyEnum.ID.value) is None
#     assert dc.get(SessionKeyEnum.USERNAME.value) is None
#
# #
# # # @patch('utils.requests.get')
# # def test_get_cast_info(numbers):
# #     # Mock the response.text of requests.get
# #     # mock_get.return_value = pickle.load(open('files/cast_li.pickle', 'rb'))
# #
# #     assert True
# #     # Create a mock for `li` to simulate find().get() returning a specific href
# #     # mock_li = MagicMock()
# #     # mock_a_tag = MagicMock()
# #     # mock_a_tag.get.return_value = '/title/tt0111161/'  # Mocked href value
# #     # mock_li.find.return_value = mock_a_tag
# #     #
# #     # # Call get_cast_info with the mocked `li`
# #     # result = asyncio.run(get_cast_info(mock_li))
# #     #
# #     # # Your assertions here
# #     # self.assertIsInstance(result, dict)
