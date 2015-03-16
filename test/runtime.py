import types

def _search_prototype_chain(cls, item):
    if item in cls.prototype:
        return cls.prototype[item]
    else:
        for base in cls.__bases__:
            if base != object:
                if item in base.prototype:
                    return base.prototype[item]
    for base in cls.__bases__:
        if base != object:
            return _search_prototype_chain(base, item)
    return None


class JSObject(object):
    prototype = {}

    def __getattr__(self, item):
        value = _search_prototype_chain(self.__class__, item)
        if value:
            return types.MethodType(value, self)
        else:
            raise AttributeError
