import datetime
import pytest
from dags import example as e


class TestSample:

    def test_hello_world(self):
        hello = e.HelloWorld()()
        assert hello == 'Hello, TaskHuman!'
