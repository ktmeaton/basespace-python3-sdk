import six
from BaseSpacePy.api.BaseSpaceException import UndefinedParameterException,UnknownParameterException,IllegalParameterException

legal    = { 'Tags':[], 'ProductIds':[] }

class QueryParametersPurchasedProduct(object):
    '''
    This class can be passed as an optional argument for a filtering getUserProducts list response
    '''
    def __init__(self, pars=None):
        if pars is None:
            pars = {}
        self.passed = {}
        for k in six.iterkeys(pars):
            self.passed[k] = pars[k]
        self.validate()

    def __str__(self):
        return str(self.passed)

    def __repr__(self):
        return str(self)

    def getParameterDict(self):
        return self.passed

    def validate(self):
        for p in six.iterkeys(self.passed):
            if not p in legal:
                raise UnknownParameterException(p)
