import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    HUNTERIO_KEY = os.getenv("HUNTERIO_KEY")


conf = Config()
