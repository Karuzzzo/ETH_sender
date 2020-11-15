from web3 import Web3

address = Web3.toChecksumAddress("0x79387b8a5d09e7b1613532a180bdc3d9ef2aab25")
private_key_hex = "0x431547bea28806bd27a871333e186a05eea3c53ec6a01865f655fd244b2ea497"

rb_link = "https://rinkeby.infura.io/v3/a9ea539cf3a348fead71f4c085f20c2c"
web3 = Web3(Web3.HTTPProvider(rb_link))

def extract_key():
    with open('/home/alexey/.ethereum/rinkeby/keystore/UTC--2020-11-08T16-43-51.866107210Z--79387b8a5d09e7b1613532a180bdc3d9ef2aab25') as keyfile:
        encrypted_key = keyfile.read()
        return web3.eth.account.decrypt(encrypted_key, '79651603027erased')

def welcome():
        #Uncomment, if you want to set password on code
    #print('Type your password: ')
    #unlock_pw = input()
    #if unlock_pw != 'eth-password': exit()

    nonce = web3.eth.getTransactionCount(address)
    print('Type in receiving address: ')
    receiver = input()
    print('Now, type how much u wanna send')
    amount = int(input())
    return (receiver, amount, nonce)

def send_tx(tx):
    signed = web3.eth.account.signTransaction(tx, private_key_hex)
    web3.eth.sendRawTransaction(signed.rawTransaction)

    #Uncomment, if you need to reimport keystore, for now I imported it and stored in variable
#private_key = extract_key(web3)  
  
(receiver, amount, nonce) = welcome()
#forming JSON transaction
tx = {
    'nonce': nonce,
    'from': address,
    'to': receiver,
    'value': web3.toWei(amount, 'ether'),
    #'value': amount,
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'data': b'',
}

send_tx(tx)
print(tx)