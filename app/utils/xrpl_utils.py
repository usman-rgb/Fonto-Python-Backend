from xrpl.clients import JsonRpcClient, WebsocketClient
from xrpl.wallet import Wallet, generate_faucet_wallet
from xrpl.models.transactions import Payment, NFTokenMint
from xrpl.utils import xrp_to_drops
from app.config import XRPL_SERVER, WALLET_SEED
from fastapi import HTTPException

class XRPLClient:
    def __init__(self):
        self.client = WebsocketClient(XRPL_SERVER)
        self.wallet = Wallet.from_seed(WALLET_SEED) if WALLET_SEED else None

    def generate_xrpl_wallet(self):
        with self.client as client:
            if not WALLET_SEED:
                return generate_faucet_wallet(client, debug=True)
            return Wallet.from_seed(WALLET_SEED)

    def mint_nft(self, to_address: str, token_uri: str):
        with self.client as client:
            wallet = self.generate_xrpl_wallet()
            payment = Payment(
                account=wallet.classic_address,
                destination=to_address,
                amount=xrp_to_drops(10),
                memos=[{"data": token_uri.encode("utf-8").hex()}]
            )
            signed_tx = wallet.sign(payment)
            tx_response = client.submit_and_wait(signed_tx)
            if tx_response.result["meta"]["TransactionResult"] == "tesSUCCESS":
                return tx_response.result["hash"]
            raise HTTPException(status_code=500, detail="Failed to mint NFT on XRPL")

    def send_payment(self, destination_address: str, amount: float):
        with self.client as client:
            payment = Payment(
                account=self.wallet.classic_address,
                destination=destination_address,
                amount=xrp_to_drops(amount)
            )
            response = client.submit_and_wait(payment)
            return response.result

    def get_balance(self, address: str = None):
        with self.client as client:
            account_info = client.request({
                "command": "account_info",
                "account": address or self.wallet.classic_address
            })

            return account_info.result["account_data"]["Balance"]
