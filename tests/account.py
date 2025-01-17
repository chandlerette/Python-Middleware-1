#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PythonMiddleware.graphene import Graphene
from PythonMiddleware.instance import set_shared_graphene_instance
from pprint import pprint
from PythonMiddleware.account import Account
from PythonMiddleware.storage import configStorage as config

nodeAddress = "ws://127.0.0.1:8049" 
gph = Graphene(node=nodeAddress, blocking=True) 
set_shared_graphene_instance(gph) 

#account info for test
defaultAccount="nicotest"
privateKey="5KgiWEMJPYbLpMhX6jvS9yBehhr4mWZhxX7hfxZQEo3rs8iakUQ"
pub="COCOS5X4bfMnAmeWhLoiHKUNrRu7D3LTXKBZQkZvWGj9YCTDBAYaSXU"

#创建钱包
if gph.wallet.created() is False: 
    gph.newWallet("123456")

#钱包解锁
if gph.wallet.locked() is True:
    gph.wallet.unlock("123456")

#add key
if gph.wallet.getAccountFromPublicKey(pub) is None:
    gph.wallet.addPrivateKey(privateKey) #账号私钥导入钱包
pprint(gph.wallet.getPrivateKeyForPublicKey(pub))

#config
config["default_prefix"] = gph.rpc.chain_params["prefix"] # 向钱包数据库中添加默认信息
config["default_account"] = defaultAccount # 向钱包数据库中添加默认信息

#account test
pprint(gph.wallet.removeAccount(None))
pprint(gph.wallet.getAccounts())

#创建账号
# try:
#     pprint(gph.create_account(account_name="test3", password="123456"))
# except Exception as e:
#     print(repr(e))
#     gph.wallet.removeAccount(None)
#pprint(gph.wallet.getAccounts())
account="nicotest"
#pprint(gph.register_nh_asset_creator(account))
#pprint(gph.create_world_view("snacktest", account))

pprint(gph.create_nh_asset(account, "COCOS", "snacktest", '{"name":"test1"}', account))


