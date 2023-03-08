import json
from subprocess import PIPE, run
#YourAddressHere
addr = 'addr_test1vr6mssvqkk3uegsq2gjcleen9rrfl78q6stsj5zkdqgpmdcz3x4jh'

def findassets(addr):
    assetdict = []
    cmd = ["cardano-cli", "query", "utxo", "--address", addr, "--testnet-magic", "1"]
    rs = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    if len(rs.stderr) < 1:
        lines = rs.stdout.splitlines()
        if len(lines) > 2:
            for l in lines:
                assetcount = l.count(".") 
                if assetcount > 0:
                    assetdict.append(l)
    if len(assetdict) > 0:
        return assetdict
        
x = findassets(addr)
for a in x:
    print(a)
