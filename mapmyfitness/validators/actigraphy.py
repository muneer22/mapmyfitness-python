import datetime

from .base import BaseValidator


class ActigraphyValidator(BaseValidator):
    def validate_search(self):

        search_kwargs = self.search_kwargs
        # https://developer.underarmour.com/docs/v71_Actigraphy

        datetime_args = ['start_date', 'end_date']
        for datetime_arg in datetime_args:

            # start_date is required and should be ISO 8601 Date (YYYY-mm-dd) format
            if datetime_arg == "start_date" and datetime_arg not in search_kwargs:
                if not isinstance(datetime.datetime.strptime(search_kwargs[datetime_arg], '%Y-%m-%d'), datetime.datetime):
                    self.add_error('Workout {0} must be of type datetime.datetime.'.format(datetime_arg))
                self.add_error('start_date is required field')

            # end_date is optional and should be in ISO 8601 Date format
            elif datetime_arg in search_kwargs and not isinstance(datetime.datetime.strptime(search_kwargs[datetime_arg], '%Y-%m-%d'), datetime.datetime):
                self.add_error('Workout {0} must be of type datetime.datetime.'.format(datetime_arg))

            # todo: validate  user href
            if 'user' in search_kwargs and not isinstance(search_kwargs['user'], int):
                self.add_error('Workout user must exist and be of type int.')