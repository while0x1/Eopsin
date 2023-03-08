from subprocess import PIPE, run
#VeriFair_alpha_Winners
assetname = input("Enter Policy Name: ")
#YourAddresshere
paymentaddr = "addr_test1vr6mssvqkk3uegsq2gjcleen9rrfl78q6stsj5zkdqgpmdcz3x4jh"
def getassetutxo(assetname):
    asset = assetname.encode('utf-8')
    assethex = asset.hex()
    assetdict = []
    cmd = ["cardano-cli", "query", "utxo", "--address", paymentaddr, "--testnet-magic", "1"]
    rs = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    if len(rs.stderr) < 1:
        lines = rs.stdout.splitlines()
        if len(lines) > 2:
            for l in lines:
                assetcount = l.count(".") 
                if l.find(assethex) > -1:  
                    txhash = l[0:64]
                    txid = l[69]
                    lovelace = l[78:l.find("lovelace")-1]
                    #print(txhash, txid, lovelace)
                    remainder = l[l.find("lovelace") + 11: l.find("+ TxOutDatum") -1]
                    assetdict.append({"txhash": txhash,"txid": txid,"lovelace":lovelace,"assets": remainder})
    if len(assetdict) > 0:
        for a in assetdict:
            for k,v in a.items():
                print(k,v)
            #print(a)
        print(f"AssetName {asset} in Hex is {assethex}")
    else:
        print("No Assets found - Check your Spelling")
