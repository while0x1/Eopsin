from eopsin.prelude import *

LOVELACE = 11000000
PAY_HASH = b"\x28\x33\xc6\xe8\x69\x65\xfb\x87\x69\x48\xa2\xbc\x89\x62\x4d\xde\xd4\x7c\x9e\xb2\x4f\xe7\x33\x8b\xc2\x0e\x15\x43"

def has_paid(txouts: List[TxOut], payhash: PubKeyHash) -> bool:
    res = False
    for txo in txouts:
        if txo.value.get(b"", {b"":0}).get(b"",0) == LOVELACE:
            cred = txo.address.credential
            if isinstance(cred, PubKeyCredential):
                pkh = cred.pubkeyhash
                if pkh == payhash:
                   res = True 
    assert res, "Incorrect Address/Amount Used"
    return res

def own_spent_utxo(txins: List[TxInInfo], p: Spending) -> TxOut:
    for txi in txins:
        if txi.out_ref == p.tx_out_ref:
            own_txout = txi.resolved
    return own_txout 

def contract_utxo_count(txins: List[TxInInfo], addr: Address) -> int:
    count = 0
    for txi in txins:
        if txi.resolved.address == addr:
            count += 1
    assert count == 1, "Only 1 contract utxo allowed"
    return count 

def validator(datum: None, redeemer: None, context: ScriptContext) -> None:
    purpose = context.purpose
    allowspend = False 
    if isinstance(purpose, Spending):
        own_utxo = own_spent_utxo(context.tx_info.inputs, purpose)
        own_addr = own_utxo.address
    count = contract_utxo_count(context.tx_info.inputs,own_addr)
    paid = has_paid(context.tx_info.outputs,PAY_HASH)
    if count == 1 and paid:
        allowspend = True
    assert allowspend
