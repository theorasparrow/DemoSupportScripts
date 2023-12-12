import sys
from web3 import Web3, EthereumTesterProvider, HTTPProvider

w3_test = Web3(EthereumTesterProvider())

# w3 = Web3(HTTPProvider('https://eth.llamarpc.com'))
# print("w3 connected?", w3.is_connected())
# print("w3 latest block", w3.eth.get_block('latest'))
# account_grantor = w3.eth.personal.newAccount('pass_grantor')
# print("account grantor", account_grantor)

# 0x6813Eb9362372EEF6200f3b1dbC3f819671cBA69
account_prover = sys.argv[1].split("Eth ")[1]
# account_prover = w3_test.eth.accounts[2]
account_grantor_test = w3_test.eth.accounts[0]
account_maintainer_test = w3_test.eth.accounts[1]
# account_prover_test = w3_test.eth.accounts[2]

# print("account prover test", account_prover_test)
print("account prover", account_prover)
print("account grantor test", account_grantor_test)
print("account maintainer test", account_maintainer_test)

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

tx1 = w3_test.eth.get_transaction(tx1_hash)
tx2 = w3_test.eth.get_transaction(tx2_hash)

print("tx1", tx1)
print("tx2", tx2)

# account of grantor
# grantor = "grantor"
# account of prover
# prover = "prover"
# account of maintainer
# maintainer = "maintainer"

# bounty = 100
# commission = bounty / 10

# print("transfering", bounty, "zoots", "from", grantor, "to", prover)
# print("transfering", commission, "zoots", "from", grantor, "to", maintainer)
