from rich.pretty import pprint
from mbpy_endpoints import Generator
from mbpy_endpoints.environs import get_environment_variable

auth_token = get_environment_variable('TOKEN')
tld = get_environment_variable('TOKEN', 'com')

if auth_token is None:
    raise Exception('Please define TOKEN environment variable whose value is the auth token in the API Manager.\ne.g.:\nexport TOKEN=abcdefggfedcba')


# output the classes
mb = Generator(auth_token=auth_token, tld=tld)
for clss in mb.generate_classes(archived=False):
    pprint(clss)


# since verbosity==1, it'll output the requests and responses
# (useful for troubleshooting)
#mb.verbosity = 1
for term_grade in mb.generate_term_grades():
    pprint(term_grade)
