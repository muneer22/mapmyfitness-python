from .base import BaseAPI
from ..validators.weight import WeightValidator
from ..serializers import WeightSerializer
from .mixins import Searchable


class BodyMass(BaseAPI, Searchable):
    path = '/bodymass'
    validator_class = WeightValidator
    serializer_class = WeightSerializer
    embedded_name = 'bodymasses'
