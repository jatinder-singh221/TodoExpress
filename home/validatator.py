from django.core import validators
from django.core.exceptions import ValidationError


def valid_data(data_get):
    if all(x.isalpha() or x.isspace() for x in data_get):
        pass
    else:
        raise ValidationError('Enter only letters are allowed')
