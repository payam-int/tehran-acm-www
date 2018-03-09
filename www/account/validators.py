import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_student_id(value):
    if not re.match(r'^\d{9}$', value.strip()):
        raise ValidationError(
            _('The student id has exactly 9 digits'),
        )
