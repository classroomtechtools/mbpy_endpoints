from mbpy_endpoints import Generator
from mbpy_endpoints.environs import get_environment_variable

auth_token = get_environment_variable('TOKEN')
tld = get_environment_variable('TLD', 'com')

# initiate the `mb` object which we'll use to interact with the apis
mb = Generator(auth_token='secret', tld=tld)

# turn on verbosity so that it'll output what it's doing to the console
mb.verbose()

page = 1
while True:
    response_dictionary = mb.endpoints.get_students(page=page)
    students = response_dictionary.get('students', [])
    if len(students) == 0:
        break  # no more students, we're done

    for student in students:
        print(student.get('id'), end=', ')
    print()
    page += 1