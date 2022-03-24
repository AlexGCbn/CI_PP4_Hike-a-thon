from django.core.exceptions import ValidationError


def validate_comment(value):
    """
    Validate a comment's length
    """

    if len(value) < 5:
        raise ValidationError('Please input more than 5 characters.')
