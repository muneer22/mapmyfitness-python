from .api.config import APIConfig
from .api.route import Route
from .api.actigraphy import Actigraphy
from .api.activity_type import ActivityType
from .api.user import User, UserProfilePhoto
from .api.workout import Workout
from .api.weight import BodyMass
from .api.sleep import Sleep
from .exceptions import NotInitializedException


class MapMyFitness(object):
    """
    Creating a singleton instance of this class, so that we can easily referr to
    it from anywhere in the code without re-creating the instance and again
    providing the api_key and access_token.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MapMyFitness, cls).__new__(cls)

        return cls._instance

    def __init__(self, api_key, access_token, cache_finds=False):
        api_config = APIConfig(api_key=api_key, access_token=access_token)
        self.route = Route(api_config=api_config, cache_finds=cache_finds)
        self.actigraphy = Actigraphy(api_config=api_config, cache_finds=cache_finds)
        self.workout = Workout(api_config=api_config, cache_finds=cache_finds)
        self.user = User(api_config=api_config, cache_finds=cache_finds)
        self._user_profile_photo = UserProfilePhoto(api_config=api_config, cache_finds=cache_finds)
        self.activity_type = ActivityType(api_config=api_config, cache_finds=cache_finds)
        self.bodymass = BodyMass(api_config=api_config, cache_finds=cache_finds)
        self.sleep = Sleep(api_config=api_config, cache_finds=cache_finds)


    @classmethod
    def instance(cls):
        """
        Returns the singleton instance of MapMyFitness if initializaed.
        If there is no initialized singleton instance, it raises a not initialized exception.

        ::raises:: NotInitializedException
        """
        if cls._instance:
            return cls._instance

        raise NotInitializedException("MapMyFitness has not been initialized")

    @classmethod
    def _drop(cls):
        """
        Drops the instance of the singleton (for testing purposes)
        """
        cls._instance = None

if __name__ == '__main__':
    api_key = "vd9aadfjcrd6ncae2wx92mc8tm4zfnx2"
    access_token = "1b657391aceca2d50db6b4c98af6d5d5b70156e5"

    workouts_paginator = MapMyFitness(api_key, access_token).sleep.search(
                target_start_datetime="2016-04-12T09:00:42+00:00",\
                 target_end_datetime="2016-08-01T09:00:42+00:00", \
                 field_set='')
    

    page_count = workouts_paginator.num_pages  # 2
    page_range = workouts_paginator.page_range # [1, 2]
    total_count = workouts_paginator.count # 58

    for page_num in page_range:
        the_page = workouts_paginator.page(page_num)
        for workout in the_page:
            print (workout.original_dict)#.energy_expended_total
