"""
    This is the token creator file for the reset password feature 
    of Eshopper ecommerce web application.
    Coded and maintained by Jotham Prince
"""
# necessary imports
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class MyPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)
        )


password_reset_token = MyPasswordResetTokenGenerator()
