import typing

from project.serializers import DataIn


def welcome(name=None) -> typing.Dict:
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def datain(datain: DataIn) -> typing.Dict:
    datain = DataIn(datain)
    return datain
