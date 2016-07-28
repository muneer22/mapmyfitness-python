from .base import BaseAPI
from ..validators.actigraphy import ActigraphyValidator
from ..serializers import ActigraphSerializer
from .mixins import Searchable


class Actigraphy(BaseAPI, Searchable):
    path = '/actigraphy'
    validator_class = ActigraphyValidator
    serializer_class = ActigraphSerializer
    embedded_name = 'actigraphies'
