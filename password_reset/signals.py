from django.dispatch import Signal

# signal sent when users successfully recover their passwords
# Provided args are 'user', 'request'
user_recovers_password = Signal()
