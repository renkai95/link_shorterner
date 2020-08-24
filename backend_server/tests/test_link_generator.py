import backend_server.link_generator
from backend_server.link_generator import generator
import mock
import pytest

backend_server.link_generator.getTime  = mock.Mock(return_value=1234)

class TestShortener():
    def testHashing(self):
        '''
        Happy case to check if the result is generated properly with a fixed salt
        '''
        res = generator("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        assert res == '0fe5af9c'

    def testFailedHashing(self):
        '''
        unhappy case to check if there is an error if a string is not provided
        '''
        with pytest.raises(TypeError):
            res = generator(42069)