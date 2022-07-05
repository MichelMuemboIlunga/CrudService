import re
from datetime import datetime
from flask import jsonify

class Helper:

    def __init__(self, user_email, created_at):
        self.user_email = user_email
        self.created_at = created_at

    def validate_email(self):

        # validate email address using regex pattern
        pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        message = 'failed'

        if re.match(pattern, self.user_email):
            return self.user_email

        else:
            return message

    def validate_created_at(self):
        # check if date time was not supply on the request and set that to cureent date
        if not self.created_at:
            self.created_at = datetime.now()
            return self.created_at
