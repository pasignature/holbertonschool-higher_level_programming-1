#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name is 'first_name':
            self.__dict__[name] = value
        else:
            cls = type(self).__name__
            errmsg = "'{}' object has no attribute '{}'".format(cls, name)
            raise AttributeError(errmsg)
