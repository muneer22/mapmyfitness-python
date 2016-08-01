import re
from .base import BaseValidator


class SleepValidator(BaseValidator):
    def validate_search(self):

        search_kwargs = self.search_kwargs
        # https://developer.underarmour.com/docs/v71_BodyMass

        datetime_args = ['target_start_datetime', 'target_end_datetime']
        datetime_format = re.compile(r'^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$')
        for datetime_arg in datetime_args:

            # start_date is required and should be ISO 8601 Datetime (2016-04-12T09:00:42+00:00) format
            if datetime_arg == "target_start_datetime" and datetime_arg not in search_kwargs:
                self.add_error('target_start_datetime is required field')

            elif not datetime_format.match(search_kwargs[datetime_arg]):
                    self.add_error('{0}  must be an ISO8601 string with offset.'.format(datetime_arg))

        if not search_kwargs.get("field_set"):
            search_kwargs.pop("field_set")