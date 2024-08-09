from abc import ABC, abstractmethod


class AccountService(ABC):
    @abstractmethod
    def checkEmailDuplication(self, email):
        pass

    @abstractmethod
    def checkNicknameDuplication(self, nickname):
        pass

    @abstractmethod
    def checkPasswordDuplication(self, password):
        pass

    @abstractmethod
    def registerAccount(self,nickname,password,email,loginType):
        pass

    @abstractmethod
    def findAccountByEmail(self, email):
        pass

    @abstractmethod
    def findAccountById(self, accountId):
        pass