#This is an example of how to determine the structure of the datum files to use with you eopsin custom datums. 

#ExampleDatumStructure in Eopsin contract:
"""
@dataclass()
class Listing(PlutusData):
    # the NFT which can unlock the escrowed NFT
    unlock_policy: bytes
    unlock_name: bytes
    # whoever is allowed to withdraw the listing
    owner: bytes
    # marketplace fees
    fee: int
    cancel_fee: int
    fee_hash: bytes
"""
#Import the dataclass from the eopsin python file

from contract import Listing
#recreate the datum structure in the correct order and print it to use in your transactions for locking unlocking in cardano-cli
print(Listing(b"e77b78f137cf18f7132904218595997ffa132ab5a8d4c832c3f1e315",b"56657269466169725f616c7068615f7469636b6574",b"f5b84180b5a3cca20052258fe73328c69ff8e0d41709505668101db7",5000000,2000000,b"f5b84180b5a3cca20052258fe73328c69ff8e0d41709505668101db7").to_json())


##Example Output
"""{"constructor": 0, "fields": [{"bytes": "6537376237386631333763663138663731333239303432313835393539393766666131333261623561386434633833326333663165333135"}, {"bytes": "353636353732363934363631363937323566363136633730363836313566373436393633366236353734"}, {"bytes": "6635623834313830623561336363613230303532323538666537333332386336396666386530643431373039353035363638313031646237"}, {"int": 5000000}, {"int": 2000000}, {"bytes": "6635623834313830623561336363613230303532323538666537333332386336396666386530643431373039353035363638313031646237"}]}
