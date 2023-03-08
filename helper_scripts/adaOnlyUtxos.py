import subprocess
import time
import os
import json
from subprocess import PIPE, run

#PUT your payment Address Here
paymentaddr = "addr_test1vr6mssvqkk3uegsq2gjcleen9rrfl78q6stsj5zkdqgpmdcz3x4jh"

def findutxo():
    utxoDict = []
    cmd = ["cardano-cli", "query", "utxo", "--address", paymentaddr, "--testnet-magic", "1"]
    rs = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    if len(rs.stderr) < 1:
        lines = rs.stdout.splitlines()
        utxocount = len(lines) - 2
        if len(lines) > 2:
            print('Processing ADA Only UTXOs...')
            for ln in lines:
                lineitems = ln.split(' ')
                if not(ln.startswith(" ")) and not(ln.startswith("-")):
                    txhash = ln[0:64]
                    txid = ln[69]
                    lovelace = ln[78:ln.find("lovelace")-1]
                    #print(txhash, txid, lovelace)
                    remainder = ln[ln.find("lovelace"):]
                    assetcount = remainder.count(".")
                    
                    if assetcount > 0:
                        #nativeAssetsFound
                        #print(remainder)
                        pass
                    else:
                        #OnlyADA UTXOs
                        utxoDict.append({"txhash": txhash,"txid": txid,"lovelace":lovelace})
                    #print(remainder)
        return utxoDict
utxos = findutxo()
for n in utxos:
        print(n)
