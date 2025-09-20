from faker import Faker

fake = Faker()

def random_username():
    return fake.user_name()

def random_password():
    return fake.password()
