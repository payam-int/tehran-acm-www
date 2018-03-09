import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_student_id(value):
    if not re.match(r'^\d{9}$', str(value).strip()):
        raise ValidationError(
            _('The student id has exactly 9 digits'),
        )
def email_validator(value):
    if not re.match(
                r'^([A-Z|a-z|0-9](\.|_){0,1})+[A-Z|a-z|0-9]\@ut.ac.ir$', value):
        raise ValidationError(
            _('This email does not belong to ut.'),
        )