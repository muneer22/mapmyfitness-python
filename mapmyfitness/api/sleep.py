from .base import BaseAPI
from ..validators.sleep import SleepValidator
from ..serializers import SleepSerializer
from .mixins import Searchable


class Sleep(BaseAPI, Searchable):
    path = '/sleep'
    validator_class = SleepValidator
    serializer_class = SleepSerializer
    embedded_name = 'sleeps'
