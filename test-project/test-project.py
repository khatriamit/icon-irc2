from iconservice import *
from .tokens.mintable import IRC2Mintable
from .tokens.burnable import IRC2Burnable

TAG = "TestProject"


class TestProject(IRC2Burnable, IRC2Mintable):
    pass
