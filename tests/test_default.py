from wake.testing import *

from pytypes.contracts.example import HelloWorld

# Print failing tx call trace
# def revert_handler(e: TransactionRevertedError):
#     if e.tx is not None:
#         print(e.tx.call_trace)

@default_chain.connect()
# @on_revert(revert_handler)
def test_default():
    hello_world = HelloWorld.deploy()

    tx = hello_world.sayHello()
    print(tx.events)
    assert not isinstance(tx.events[0], HelloWorld.Hello)
    pass
