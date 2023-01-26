from web3 import Web3
import time
import asyncio
import requests
from termcolor import cprint


alchemy_url = "https://opt-mainnet.g.alchemy.com/v2/h8ZAPU9TJ0sU7Bau2K1geFBbEhHSmJn9"
w3 = Web3(Web3.HTTPProvider(alchemy_url))
abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"newMinter","type":"address"}],"name":"EventMinterAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oldMinter","type":"address"}],"name":"EventMinterRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"minter","type":"address"}],"name":"addMinter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"burnBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"cid","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNumMinted","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isOwnerOf","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"cid","type":"uint256"}],"name":"mint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256[]","name":"cidArr","type":"uint256[]"}],"name":"mintBatch","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"minters","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"minter","type":"address"}],"name":"removeMinter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newName","type":"string"}],"name":"setName","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newSymbol","type":"string"}],"name":"setSymbol","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"transferable","type":"bool"}],"name":"setTransferable","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newURI","type":"string"}],"name":"setURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"transferable","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'
contract_address = '0xfA14e1157F35E1dAD95dC3F822A9d18c40e360E2'
contract = w3.eth.contract(address=Web3.toChecksumAddress(
    contract_address), abi=abi)
main_private_key = '0x3809cd4a0816bf8e0a0281ab226e5432d69493462f9eb2018c4963092fab059c'
n = 0
with open('C:/Users/admin/Documents/softs/polynomial/private_keys.txt', 'r') as f:
  private_keys = f.read().splitlines()
#for private_key in private_keys:
  
  # try:  
  #   account = w3.eth.account.privateKeyToAccount(private_key)
  #   nonce = w3.eth.get_transaction_count(account.address)
  #   balance = contract.functions.balanceOf(account.address).call()
  #   if balance == 0:
  #       n+=1
  #       with open('C:/Users/admin/Documents/softs/polynomial/addresses no nft.txt', 'a') as f:
  #         f.write(account.address+"\n")
  #   print(f'{account.address} - {balance}')
      
  # except Exception as e:
  #   continue



# address = w3.toChecksumAddress('0x7c981217944593351f36f2cf9f0556444b772db0')
# url = f"https://opt-mainnet.g.alchemy.com/nft/v2/h8ZAPU9TJ0sU7Bau2K1geFBbEhHSmJn9/getNFTs?owner={address}&pageSize=100&withMetadata=false"

# headers = {"accept": "application/json"}

# response = requests.get(url, headers=headers)

# print(response.json()['ownedNfts'][0]['id']['tokenId'][-5:])



# print(n)
# account = w3.eth.account.privateKeyToAccount(main_private_key)
# token_info = w3.eth.get_token_info(account.address)
# print(token_info)


n = 0
for private_key in private_keys:
  try:
    n+=1
    main_account = w3.eth.account.privateKeyToAccount(main_private_key)
    account = w3.eth.account.privateKeyToAccount(private_key)
    address = account.address
    nonce = w3.eth.get_transaction_count(account.address)
    balance = contract.functions.balanceOf(account.address).call()
    ether_balance = w3.from_wei(w3.eth.get_balance(address), "ether")
    if balance == 0 or account.address == w3.toChecksumAddress('0x6e665dee4fb1ca124451e3ac7ff75d57afb1e51e'):
      continue
    # if ether_balance < 0.00020896:
    #   nonce = w3.eth.get_transaction_count(main_account.address)

    #   #build a transaction in a dictionary
    #   tx = {
    #       'nonce': nonce,
    #       'to': address,
    #       'value': w3.to_wei(0.00020896-float(ether_balance), 'ether'),
    #       'gas': 2000000,
    #       'gasPrice': w3.eth.gas_price
    #   }

    #   #sign the transaction
    #   signed_tx = w3.eth.account.sign_transaction(tx, main_private_key)

    #   #send transaction
    #   tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    #   cprint(f'Sent ETH - https://optimistic.etherscan.io/tx/{tx_hash.hex()}','green')
    #   w3.eth.wait_for_transaction_receipt(
    #     transaction_hash=tx_hash, poll_latency=1)
    url = f"https://opt-mainnet.g.alchemy.com/nft/v2/h8ZAPU9TJ0sU7Bau2K1geFBbEhHSmJn9/getNFTs?owner={address}&pageSize=100&withMetadata=false"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    token_id = response.json()['ownedNfts'][0]['id']['tokenId'][-6:]
    # print(response.text)
    # print(token_id)
    
    
    tx = dict(
      nonce=w3.eth.get_transaction_count(address),
      gasPrice=w3.eth.gas_price,
      gas=100000,
      to=w3.toChecksumAddress(
          '0xfa14e1157f35e1dad95dc3f822a9d18c40e360e2'),
      data=f'0x42842e0e000000000000000000000000{account.address[2:]}0000000000000000000000006e665dee4fb1ca124451e3ac7ff75d57afb1e51e0000000000000000000000000000000000000000000000000000000000{token_id}360c6ebe',
      value=0,
      chainId=w3.eth.chain_id
      )
    signed_tx = w3.eth.account.sign_transaction(
        tx, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(
        transaction_hash=tx_hash, poll_latency=1)
    if receipt['status'] == 1:
      cprint(f'Transfer NFT tx - https://optimistic.etherscan.io/tx/{tx_hash.hex()}','green')
    else:
      cprint(f'Transfer NFT tx - https://optimistic.etherscan.io/tx/{tx_hash.hex()}','red')
  except Exception as e:
    cprint(f'Error - {e}','red')
    break