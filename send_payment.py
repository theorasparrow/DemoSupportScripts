import sys
from web3 import Web3, EthereumTesterProvider

w3 = Web3(EthereumTesterProvider())

account_prover = sys.argv[1].split("Eth ")[1]
account_grantor = w3.eth.accounts[0]
account_maintainer = w3.eth.accounts[1]

print("account prover", account_prover)
print("account grantor", account_grantor)
print("account maintainer", account_maintainer)

tx1_hash = w3.eth.send_transaction({
  "from" : account_grantor,
  "to" : account_prover,
  "value" : 100
})

tx2_hash = w3.eth.send_transaction({
  "from" : account_grantor,
  "to" : account_maintainer,
  "value" : 10
})

tx1 = w3.eth.get_transaction(tx1_hash)
tx2 = w3.eth.get_transaction(tx2_hash)

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
