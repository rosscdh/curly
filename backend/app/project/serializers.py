from apistar import types, validators


class DataIn(types.Type):
    name = validators.String(max_length=100)
    rating = validators.Integer(minimum=1, maximum=5)
    in_stock = validators.Boolean(default=False)
    size = validators.String(enum=['small', 'medium', 'large'])