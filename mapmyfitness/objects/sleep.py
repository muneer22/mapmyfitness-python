from .base import BaseObject
from ..utils import privacy_enum_to_string


class SleepObject(BaseObject):
    simple_properties = {
        'name': None, 'start_locale_timezone': None, 'source': None,
        'has_time_series': None,
    }

    datetime_properties = {
        'datetime_utc': None, 'created_datetime': None, 'updated_datetime': None,
    }

    @property
    def id(self):
        return int(self.original_dict['_links']['self'][0]['id'])

    @property
    def user_id(self):
        return int(self.original_dict['_links']['user'][0]['id'])

    @property
    def data_source_id(self):
        return int(self.original_dict['_links']['data_source'][0]['id'])

    @property
    def external_id(self):
        return self.original_dict['external_id']

    @property
    def timezones(self):
        if 'timezones' in self.original_dict:
            return self.original_dict['datetime_timezone']

    # These should always exist
    @property
    def total_deep_sleep(self):
        if 'aggregates' in self.original_dict:
            return self.original_dict['aggregates']["details"]["deep_sleep"]["sum"]
        return None
    
    @property
    def total_time_to_sleep(self):
        if 'aggregates' in self.original_dict:
            return self.original_dict['aggregates']["details"]["time_to_sleep"]["sum"]
        return None

    @property
    def total_awake(self):
        if 'aggregates' in self.original_dict:
            return self.original_dict['aggregates']["details"]["awake"]["sum"]
        return None

    @property
    def total_times_awakened(self):
        if 'aggregates' in self.original_dict:
            return self.original_dict['aggregates']["details"]["times_awakened"]["sum"]
        return None

    @property
    def total_light_sleep(self):
        if 'aggregates' in self.original_dict:
            return self.original_dict['aggregates']["details"]["light_sleep"]["sum"]
        return None



    @property
    def privacy(self):
        if 'privacy' in self.original_dict['_links']:
            privacy_enum = int(self.original_dict['_links']['privacy'][0]['id'])
            return privacy_enum_to_string(privacy_enum)
        return None
