'''只修改测试函数达到测试目的'''
from prctice_code.D26_bank_text import Bank
import pytest

@pytest.fixture                         #“准备函数”每次被调用都会new一个 ret对象
def init_bank():
    balance = 100
    ret = Bank(balance)
    return ret

def test_deposit(init_bank):
    init_bank.deposit(100)              #调用deposit方法存款100

    assert init_bank.balance == 200
    with pytest.raises(ValueError):     #判断是否抛出对应异常并捕获
        init_bank.deposit(-1)
    with pytest.raises(ValueError):
        init_bank.deposit(0)

def test_withdrow(init_bank):
    init_bank.withdraw(100)

    assert init_bank.balance == 0
    with pytest.raises(ValueError):
        init_bank.withdraw(500)
