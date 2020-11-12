from web3 import Web3
from eth_account import Account
my_address = "0x79387B8a5d09E7B1613532a180bdc3d9Ef2aAB25"
private_key = "9412462ca9e849426141fef9a7f92116588035324d7c1cdda9a51cd4989b1859"
#rinkeby_link = "https://rinkeby.infura.io/v3/a9ea539cf3a348fead71f4c085f20c2c"
#web3 = Web3(Web3.HTTPProvider(rinkeby_link))
ganache_link = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_link))

account_1 = '0x8F95bdb2F2492C8BDc929dDb4C60d15237e193E6' # Fill me in
account_2 = '0xe3e66d9ba21d358c3dAd781E31cffcD5eB8A53d4' # Fill me in
private_key = '5a527dcdaa19028c74ded3884c7e9b65ae0b0a577d3e4a4c439e0d9008bce9c5' # Fill me in

nonce = web3.eth.getTransactionCount(account_1)
receiver = input()
amount = int(input())

tx = {
    'nonce': nonce,
    'to': receiver,
    'value': web3.toWei(amount, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}
signed = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed.rawTransaction)
#print(web3.toHex(tx_hash))
print('your transaction is: ', tx)
