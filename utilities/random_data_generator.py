from faker import Faker
import random

fake = Faker("en_IN")


class RandomDataGenerator:

    @staticmethod
    def random_carpet_area():
        return str(random.randint(500, 3000))

    @staticmethod
    def random_first_name():
        return fake.unique.first_name()

    @staticmethod
    def random_last_name():
        return fake.unique.last_name()

    @staticmethod
    def random_indian_mobile():
        return f"{random.choice([9, 8, 7, 6])}{fake.random_number(digits=9, fix_len=True)}"

    @staticmethod
    def random_email():
        return fake.email()

    @staticmethod
    def random_pincode():
        return str(random.randint(100000, 999999))

    @staticmethod
    def random_property_price():
        return str(random.randint(500000, 10000000))

    @staticmethod
    def random_property_title():
        prefixes = [
            "Royal", "Green", "Skyline", "Sunrise", "Silver",
            "Golden", "Elite", "Prime", "Grand", "Harmony"
        ]

        property_types = [
            "Residency", "Heights", "Villa", "Apartments",
            "Homes", "Estate", "Residences", "Park", "Enclave", "Tower"
        ]

        return f"{random.choice(prefixes)} {random.choice(property_types)}"

    @staticmethod
    def random_property_description():
        return fake.paragraph(nb_sentences=5)

    @staticmethod
    def random_address():
        return fake.address().replace("\n", ", ")

    @staticmethod
    def random_comment():
        return fake.sentence(nb_words=8)