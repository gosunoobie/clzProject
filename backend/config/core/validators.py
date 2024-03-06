
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_file_size(value):
    limit = 1048576 * 2
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')
