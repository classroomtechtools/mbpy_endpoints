# mbpy_endpoints

Interact directly with ManageBac's endpoints. It can be run directly from the command line, or used in another project.

## How to use on the command line

First, install [poetry](https://python-poetry.org/docs/), a python package manager.

```
git clone ...
cd mbpy_endpoints
poetry install 
poetry run python examples/interactive.py
>>>
```

## How to use in another project

Examples are available in examples/*.py.  Briefly, there is a `Generator` class that already has functions that start with `generate_*` that help you loop through various API calls:

```python
from mbpy_endpoints import build_generator
mb = build_generator(auth_token=auth_token, tld=tld)

for item in mb.generate_xyz():
    pprint(item)
    # ...
```

You can also use the `mb.endpoints` function to directly call with the api:

```python
result = mb.get_term_grades(class_id=123, term_id=393)  # class ID, term ID
pprint(result)
```

## Rate limit

It is hard-coded to not exceed 100 calls per every 60 seconds.  In case a `429` response is recieved, it is handled automatically.

## Mocking non-GET calls

During development, there may be cases where actually making updates is inadvisable. In that case, the `build_generator` function has `mock=True` option. When used, any POST or PATCH (or any method not GET) is called, it is not sent across the wire, but otherwise behaves exactly the same way.  For full transparency, it outputs to console (even when not verbose):

```
mb.endpoints.add_student_to_class(123, body={'students': [343]})
```

Output: 

```
POST v2/classes/123/add_students => 200: (MOCKED)
```

