from faker import Faker

fake = Faker()


def generate_strings_array(n):
    return [fake.ascii_email() for _ in range(n)]
