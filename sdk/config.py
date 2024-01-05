import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Represent the storage for config constants."""

    hunterio_key = os.getenv('HUNTERIO_KEY')


conf = Config()
