import jwt

from datetime import datetime, timedelta

SECRET_KEY = 'NsVuHQsVVpAb9KJC3M4D'

def create_access_token(user, days=7):
    data = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(days=days)
    }
    
    return jwt.encode(data, SECRET_KEY, algorithm='HS256')