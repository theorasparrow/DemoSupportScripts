import os
import sys
from web3 import Web3, EthereumTesterProvider, HTTPProvider
from web3.middleware import construct_sign_and_send_raw_middleware


w3_test = Web3(EthereumTesterProvider())
w3 = Web3(HTTPProvider('https://eth.llamarpc.com'))

# print("w3 connected?", w3.is_connected())
# print("w3 latest block", w3.eth.get_block('latest'))

# 0x6813Eb9362372EEF6200f3b1dbC3f819671cBA69
account_prover = sys.argv[1].split("Eth ")[1]
account_grantor_test = w3_test.eth.accounts[0]
account_maintainer_test = w3_test.eth.accounts[1]
# account_prover_test = w3_test.eth.accounts[2]

print("account prover", account_prover)
print("account grantor test", account_grantor_test)
print("account maintainer test", account_maintainer_test)

balance_before = w3_test.eth.get_balance(account_prover)
print("balance before", balance_before)

tx1_hash = w3_test.eth.send_transaction({
  "from" : account_grantor_test,
  "to" : account_prover,
  "value" : 100
})

tx2_hash = w3_test.eth.send_transaction({
  "from" : account_grantor_test,
  "to" : account_maintainer_test,
  "value" : 10
})

balance_after = w3_test.eth.get_balance(account_prover)
print("balance after", balance_after)

tx1 = w3_test.eth.get_transaction(tx1_hash)
tx2 = w3_test.eth.get_transaction(tx2_hash)

# print("tx1", tx1)
# print("tx2", tx2)

bounty = 100
commission = bounty / 10

print("transfering", "zoots", "from grantor to prover")
print("transfering", "zoots", "from grantor to maintainer")

grantor_pk = os.environ.get('GRANTOR_PK')
maintainer_pk = os.environ.get('MAINTAINER_PK')

print("maintainer pk", maintainer_pk)

# Instantiate Account object from key:
grantor_acc = w3.eth.account.from_key(grantor_pk)
maintainer_acc = w3.eth.account.from_key(maintainer_pk)

prover_address = sys.argv[1].split("Eth ")[1]

# auto-signer:
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(grantor_acc))
# pk also works: w3.middleware_onion.add(construct_sign_and_send_raw_middleware(grantor_pk))

# Transactions signed, under the hood, in the middleware:
tx1_hash = w3.eth.send_transaction({
    "from": grantor_acc.address,
    "value": 100,
    "to": prover_address
})

tx2_hash = w3.eth.send_transaction({
    "from": grantor_acc.address,
    "value": 10,
    "to": maintainer_acc.address
})

tx1 = w3.eth.get_transaction(tx1_hash)
assert tx1["from"] == grantor_acc.address
tx2 = w3.eth.get_transaction(tx2_hash)
assert tx2["from"] == grantor_acc.address

