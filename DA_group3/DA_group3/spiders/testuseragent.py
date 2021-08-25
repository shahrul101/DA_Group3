import unittest


class TestUserAgent(unittest.TestCase):
    def test_Browser(self):
        rh = requests.get(Script.url)

print("User Agent:")
print(Script.rh.text)

headers = {
    "User-Agent ": 'Mobile'
}

print("User Agent:")
print(Script.rh.text)

if __name__ == '__main__':
    unittest.main()