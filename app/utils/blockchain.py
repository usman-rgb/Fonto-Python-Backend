from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet, generate_faucet_wallet
from xrpl.models.transactions import Payment
from xrpl.utils import xrp_to_drops
from app.config import XRPL_SERVER, WALLET_SEED

# XRPL client setup
client = JsonRpcClient(XRPL_SERVER)

def generate_xrpl_wallet():
    if not WALLET_SEED:
        return generate_faucet_wallet(client, debug=True)
    return Wallet.from_seed(WALLET_SEED)

def mint_nft_on_xrpl(to_address: str, token_uri: str):
    wallet = generate_xrpl_wallet()
    payment = Payment(
        account=wallet.classic_address,
        destination=to_address,
        amount=xrp_to_drops(10),  # Initial payment for NFT creation
        memos=[{"data": token_uri.encode("utf-8")}]
    )
    signed_tx = wallet.sign_transaction(payment)
    tx_response = client.submit_and_wait(signed_tx)
    if tx_response.result["meta"]["TransactionResult"] == "tesSUCCESS":
        return tx_response.result["hash"]

    raise HTTPException(status_code=500, detail="Failed to mint NFT on XRPL")
