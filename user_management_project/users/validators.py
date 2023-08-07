import datetime as dt
import re

from django.core.exceptions import ValidationError


class ValidateUsername:
    """Username validation."""

    def validate_username(self, value):
        """Cannot use 'me' as username."""

        if value.lower() == 'me':
            raise ValidationError(
                'You cannot create user with a "me" username.'
            )
        if not re.match(r"^[\w.@+-]+\Z", value):
            raise ValidationError(
                'Username has invalid characters.'
            )
        return value