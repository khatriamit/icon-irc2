from iconservice import *
from .base import IRC2


class IRC2Burnable(IRC2):
    """
    Implementation of IRC2Burnable
    """

    @external
    def burn(self, _amount: int) -> None:
        """
        Destroys `_amount` number of tokens from the caller account.
        Decreases the balance of that account and total supply.
        See {IRC2-_burn}

        :param _amount: Number of tokens to be destroyed.
        """
        super()._burn(self.msg.sender, _amount)

    @external
    def burnFrom(self, _account: Address, _amount: int) -> None:
        """
        Destroys `_amount` number of tokens from the specified `_account` account.
        Decreases the balance of that account and total supply.
        See {IRC2-_burn}

        :param _account: The account at which token is to be destroyed.
        :param _amount: Number of tokens to be destroyed at the `_account`.
        """

        # decreasedAllowance = SafeMath.sub(self._allowance(_account, self.msg.sender), _amount)

        # super()._approve(_account, self.msg.sender, decreasedAllowance)
        super()._burn(_account, _amount)
