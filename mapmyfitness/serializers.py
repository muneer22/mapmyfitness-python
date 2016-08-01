from .objects.activity_type import ActivityTypeObject
from .objects.route import RouteObject
from .objects.workout import WorkoutObject
from .objects.actigraphy import ActigraphObject
from .objects.weight import WeightObject
from .objects.sleep import SleepObject
from .objects.user import UserObject, UserProfilePhotoObject


class BaseSerializer(object):
    def __init__(self, dict_):
        obj = self.object_class(dict_)
        self.serialized = obj


class RouteSerializer(BaseSerializer):
    object_class = RouteObject


class WorkoutSerializer(BaseSerializer):
	object_class = WorkoutObject


class UserSerializer(BaseSerializer):
	object_class = UserObject


class UserProfilePhotoSerializer(BaseSerializer):
    object_class = UserProfilePhotoObject


class ActivityTypeSerializer(BaseSerializer):
    object_class = ActivityTypeObject


class ActigraphSerializer(BaseSerializer):
	object_class = ActigraphObject


class WeightSerializer(BaseSerializer):
	object_class = WeightObject

class SleepSerializer(BaseSerializer):
    object_class = SleepObject
