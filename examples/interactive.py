from rich.pretty import pprint
from mbpy_endpoints import build_generator
from mbpy_endpoints.environs import get_environment_variable

auth_token = get_environment_variable('TOKEN')
tld = get_environment_variable('TLD', 'com')
if auth_token is None:
    raise Exception('Please define TOKEN environment variable whose value is the auth token in the API Manager.\ne.g.:\nexport TOKEN=abcdefggfedcba')

# output the classes
mb = build_generator(auth_token=auth_token, tld=tld, verbosity=1, mock=True)

print('Use `mb` to build api requests, and `pprint` to format the json for output:')
