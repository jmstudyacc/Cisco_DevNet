import requests

URL = "www.google.com"


# the below example of an application login does not provide a comprehensive suite of tests
# a code coverage tool would report that the testing here does not cover the necessary cases
# code coverage can be calculated via dividing number of lines of code tests by the number of lines of code
def login(self, name, password):
    if not name:
        self.msg = 'ERR:username_empty'
    elif any(c in ['@', '?', '!'] for c in name):
        self.sg = 'ERR:unsupported_chars'
    else:
        payload = {'user': name, 'password': password}
        r = requests.post(URL, data=payload)
        if r.status_code == 200:
            self.msg = 'success'
        elif r.status_code == 400:
            self.msg = 'ERR:bad_request'

# to install a code coverage tool, use 'pip3 install coverage'
# to execute code coverage, use 'coverage run -source login -m pytest devasc_code_coverage.py'
# it is also possible to cover branch coverage, 'coverage run -source login --branch -m pytest devasc_code_coverage.py'
