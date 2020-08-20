import requests
import unittest

from unittest.mock import patch

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):

    def create_ap(self)

        #pass in configurations for test database 
        return app