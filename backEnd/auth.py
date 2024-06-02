import firebase_admin
from firebase_admin import credentials, auth

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate('config/google-services.json')
firebase_admin.initialize_app(cred)

def create_user(email, password):
    user = auth.create_user(email=email, password=password)
    print(f'Successfully created new user: {user.uid}')
    return user

def get_user(uid):
    user = auth.get_user(uid)
    print(f'Successfully fetched user data: {user.uid}')
    return user

# Contoh penggunaan
if __name__ == '__main__':
    user = create_user('user@example.com', 'password')
    user_data = get_user(user.uid)
