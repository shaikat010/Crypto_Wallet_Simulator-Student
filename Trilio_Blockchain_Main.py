#from trilio import Trilio
from trilio import *

# Creates a blockchain object
blockchain = Trilio()

valid = blockchain.validate_chain()  # True = Valid, False = Invalid

all_wallets = [] # stores all the wallets available
all_transactions_pbc = [] # stores all the public addresses which received coins
all_transactions_amount = [] # storees all the transaction's amount info
all_public_address = [] # stores all the public address generated 

# wallet = blockchain.Wallet.create_wallet()  # Will return json with wallet information
# # print("This is the wallet object ----------------------------------------------------------->")
# # print(wallet)

# address = wallet["address"]
# # print("This is the private key ------------------------------------------------------------>")
# # print(address["pve"])  # Private key
# # print("This is the public key -------------------------------------------------------------->")
# # print(address["pbc"])  # Public key

# # # Gives the summary of the addresses in the wallet
# # print(f"This is the address {address}")

# # Creating the second wallet ------------------------------------------------------------------
# wallet_02 = blockchain.Wallet.create_wallet()
# address_02 = wallet_02["address"]
# # # Gives the summary of the addresses in the wallet
# # print(f"This is the address_02 {address_02}")
# # -----------------------------------------------------------------------------------------------


# print("These are the balance details:")
# # This shows that there is zero balance
# print(blockchain.Wallet.get_balance(private_key=address["pve"], public_key=address["pbc"]))  # Get a wallet's balance


# # This shows that there is no asset currently
# print(blockchain.Wallet.get_assets(private_key=address["pve"], public_key=address["pbc"]))  # Get a wallet's assets

# # This shows that there are no collections
# print(blockchain.Wallet.get_collections(private_key=address["pve"],
#                                         public_key=address["pbc"]))  # Get a wallet's collections

# # If we want to convert the wallet key then we use this code:
# # blockchain.Wallet.get_public_key(private_key=<private_key>)

# # Crediting a wallet:
# # mention the public key and the amount that you want to credited
# blockchain.Wallet.credit_wallet(public_key=address["pbc"], amount=10)
# print("This is the current balance after crediting the wallet --------------------------------------->")
# print(blockchain.Wallet.get_balance(private_key=address["pve"], public_key=address["pbc"]))  # Get a wallet's balance



# print(blockchain.trilio.chain)

# print(blockchain)

# print("This is the chain validity------------------------------>")
# print(blockchain.validate_chain())

# #Sending tokens to the wallet:
# # Need to import datetime
# # mention the keys and the amount
# blockchain.create_transaction(
#     datetime.now(),
#     data = {
#         "type":"token-transfer",
#         "data":{
#             "to":address_02["pbc"],
#             "from":address["pve"],
#             "amount":10
#         }
#     }
# )

# # Checking the balance of teh wallet after the transaction -------------------------------------------------
# # You will see that it decreased
# print("This is the balance of the first wallet")
# print(blockchain.Wallet.get_balance(private_key=address["pve"], public_key=address["pbc"]))  # Get a wallet's balance

