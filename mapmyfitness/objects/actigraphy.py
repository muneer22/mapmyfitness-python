from .base import BaseObject
from ..utils import privacy_enum_to_string


class ActigraphObject(BaseObject):
    simple_properties = {
        'name': None, 'start_locale_timezone': None, 'source': None,
        'has_time_series': None,
    }

    datetime_properties = {
        'start_datetime': None, 'created_datetime': None, 'updated_datetime': None,
    }

    @property
    def id(self):
        return int(self.original_dict['_links']['user'][0]['id'])

    @property
    def timezones(self):
        if 'timezones' in self.original_dict:
            return self.original_dict['timezones']

    #
    # Aggregates
    #

    # These should always exist
    @property
    def heart_rate_resting_total(self):
        return self.original_dict['aggregates']['heart_rate_resting']["latest"]

    @property
    def active_time_total(self):
        return self.original_dict['aggregates']['active_time']['sum']

    @property
    def target_net_energy_total(self):
        return self.original_dict['aggregates']['target_net_energy']['latest']

    @property
    def bodymass_total(self):
        return self.original_dict['aggregates']['bodymass']["latest"]

    @property
    def energy_consumed_total(self):
        return self.original_dict['aggregates']['energy_consumed']["sum"]

    @property
    def distance_total(self):
        return self.original_dict['aggregates']['distance']["sum"]

    @property
    def bmi_total(self):
        return self.original_dict['aggregates']['bmi']["latest"]

    @property
    def rest_day_total(self):
        return self.original_dict['aggregates']['rest_day']

    @property
    def fat_mass_percent_total(self):
        return self.original_dict['aggregates']['fat_mass_percent']["latest"]

    @property
    def nutrients_consumed_total(self):
        return self.original_dict['aggregates']['nutrients_consumed']

    @property
    def sleep_total(self):
        return self.original_dict['aggregates']['sleep']["sum"]

    @property
    def steps_total(self):
        return self.original_dict['aggregates']['steps']['sum']

    @property
    def energy_expended_total(self):
        return self.original_dict['aggregates']['energy_expended']["sum"]

    @property
    def metabolic_energy_total(self):
        return self.original_dict['aggregates']['metabolic_energy_total']["sum"]

    # These might not exist

    @property
    def workouts_total(self):
        if 'workouts' in self.original_dict:
            return self.original_dict['workouts']

    @property
    def workouts_total(self):
        if 'metrics' in self.original_dict:
            return self.original_dict['metrics']

    @property
    def privacy(self):
        if 'privacy' in self.original_dict['_links']:
            privacy_enum = int(self.original_dict['_links']['privacy'][0]['id'])
            return privacy_enum_to_string(privacy_enum)
        return None
