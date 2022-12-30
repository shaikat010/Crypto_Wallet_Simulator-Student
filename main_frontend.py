import streamlit as st # importing streamlit package
import Trilio_Blockchain_Main as tbm # importing Trilio_Blockchain_Main.py
from datetime import datetime
from tabulate import tabulate
from PIL import Image



# st. set_page_config(layout="wide") # full screen width for streamlit

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.write("")

with col2:
    img = Image.open("MetaMask_Fox.png")
    # display image using streamlit
    # width is used to set the width of an image
    st.image(img, width=200)

with col3:
    st.write("")


st.markdown("<h1 style='text-align: center; color: orange; '>Blockchain Wallet Simulator</h1>", unsafe_allow_html=True)

# importing variables from main
blockchain = tbm.blockchain
all_wallets = tbm.all_wallets 
total_wallets = len(all_wallets)
all_transactions_pbc = tbm.all_transactions_pbc
all_transactions_amount = tbm.all_transactions_amount
all_public_address = tbm.all_public_address
valid = tbm.valid



st.markdown("<h3 style='text-align: center; color: white; '>Your Wallet at Your Disposal</h3>", unsafe_allow_html=True)

st.subheader("Actions: ")

# Wallet creation
st.title('Create a Wallet')
if st.button("Generate a wallet"): # button to run the wallet creating code
    create_wallet = blockchain.Wallet.create_wallet()
    all_wallets.append(create_wallet) # appending every wallet created to a list
    address = create_wallet['address']
    all_public_address.append(create_wallet['address']['pbc'])
    st.text('Your private key is:')
    st.success(address['pve'])

# Wallet Top up
st.title('Top up your wallet')
if total_wallets > 0:
    public_key = st.text_input('Your public key') # taking public key from user input
    credit_amount = st.number_input('Enter the amount') # taking amount of coins from user input to credit
    if st.button('credit your wallet'):
        blockchain.Wallet.credit_wallet(public_key=str(public_key), amount=credit_amount) # crediting the wallet 
else:
    st.text('No wallets available')
st.text(all_wallets)

# Trransfer Coins
st.title('Transfer Funds')
sender_key = st.text_input('Enter your private key') # taking sender's pve 
receiver_address = st.text_input('Enter the receivers public address') # taking receiever's pbc
transfer_amount = st.number_input('Amount to send') # taking as input the amount to transfer
if st.button('Transfer'):
    if str(receiver_address) in all_public_address: # checking if provided pbc exists 
        blockchain.create_transaction(  # transfer execution code
        datetime.now(),
        data = {
            "type":"token-transfer",
            "data":{
                "to":receiver_address,
                "from":sender_key,
                "amount":transfer_amount
            }
        }
        )
        all_transactions_pbc.append(receiver_address) # storing all the public addresses that has received coins
        all_transactions_amount.append(transfer_amount) # storing all the amounts of coins transferred
    else:
        st.error('This public address does not exist')

# Check validity of chain

st.title('Check the validity of the chain')
if st.button('Check Validity'):
    if valid == True:
        st.success('The chain is valid')
    
    elif valid == None:
        st.info('None')

    else:
        st.error('The chain is invalid')

# Sidebar

with st.sidebar:
    st.title("Trilio: About the network")
    st.write("This is a crypto wallet simulation project made with streamlit. Refresh after every actions to see the results")

    st.title("Total number of wallets in the network: " + str((total_wallets)))
    st.title("Block height: " + str((len(all_transactions_amount))))

    st.write("The block height is the same as the length of the block, this means it is the number of transactions that occured")
# View all transactions
st.title('All transactions')
if st.button('View all transactions'):
    for i in all_transactions_pbc:
        for j in all_transactions_amount:
            table = [['Public Address', 'Amount Received'], 
            [i, j]]
            st.text(tabulate(table))
            break