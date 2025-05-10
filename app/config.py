<<<<<<< HEAD
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
XRPL_SERVER = os.getenv("XRPL_SERVER")
WALLET_SEED = os.getenv("WALLET_SEED")
IPFS_API_URL = os.getenv("IPFS_API_URL")
=======
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
XRPL_SERVER = os.getenv("XRPL_SERVER")
WALLET_SEED = os.getenv("WALLET_SEED")
IPFS_API_URL = os.getenv("IPFS_API_URL")
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
PINATA_JWT = os.getenv("PINATA_JWT")