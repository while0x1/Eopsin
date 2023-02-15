from eopsin.prelude import *

LOVELACE = 5250000
PAY_HASH = b"\x28\x33\xc6...<your_hex_escaped_public_key_hash>..."

def has_paid(txouts: List[TxOut], payhash: PubKeyHash) -> bool:
    res = False
    for txo in txouts:
        if txo.value.get(b"", {b"":0}).get(b"",0) == LOVELACE:
            cred = txo.address.credential
            if isinstance(cred, PubKeyCredential):
                pkh = cred.pubkeyhash
                if pkh == payhash:
                   res = True 
    return res

def validator(datum: None, redeemer: None, context: ScriptContext) -> None:
    paid = has_paid(context.tx_info.outputs,PAY_HASH)
    assert paid, "Incorrect Address/Amount Used"
