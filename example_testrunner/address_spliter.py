import unittest
import re


def split_addr(address):
    patterns = [
        r"(?P<number>^\d+), (?P<street>.+)$",
        r"^(?P<number>\d+) (?P<street>.+)$",
        r"^(?P<street>\D+|\S?), (?P<number>\d+)$",
        r"^(?P<street>.*) (?P<number>No .*)$",
        r"^(?P<street>\D+|\S?) (?P<number>\d+\w?$|\d+\s\w$)"
    ]
    for pattern in patterns:
        result = re.match(pattern, address)
        if result:
            return result.group("street"), result.group("number")

    raise Exception("Can't Parse Address")


class AddressSpliterSimpleCasesTestCase(unittest.TestCase):
    def test_parse_simple_streets(self):
        # Key -> Address; Value -> Expected Response
        addresses = {
            "Winterallee 3": ("Winterallee", "3"),
            "Musterstrasse 45": ("Musterstrasse", "45"),
            "Blaufeldweg 123B": ("Blaufeldweg", "123B")
        }
        for key in addresses.keys():
            response = split_addr(key)
            self.assertEqual(addresses[key], response)


class AddressSplitComplicatedTestCase(unittest.TestCase):
    def test_complicated_addresses(self):
        # Key -> Address; Value -> Expected Response
        addresses = {
            "Am Bächle 23": ("Am Bächle", "23"),
            "Auf der Vogelwiese 23 b": ("Auf der Vogelwiese", "23 b"),
        }
        for key in addresses.keys():
            response = split_addr(key)
            self.assertEqual(addresses[key], response)

class AddressSplitOtherCountriesTestCase(unittest.TestCase):
    def test_other_countries_addresses(self):
        # Key -> Address; Value -> Expected Response
        addresses = {
            "4, rue de la revolution": ("rue de la revolution", "4"),
            "200 Broadway Av": ("Broadway Av", "200"),
            "Calle Aduana, 29": ("Calle Aduana", "29"),
            "Calle 39 No 1540": ("Calle 39", "No 1540")
        }
        for key in addresses.keys():
            response = split_addr(key)
            self.assertEqual(addresses[key], response)


if __name__ == "__main__":
    unittest.main()
