from apistar import types, validators


class DataIn(types.Type):
    name = validators.String(max_length=100)
    request_id = validators.Any()
    payload = validators.String()