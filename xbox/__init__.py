from .client import Client

__VERSION__ = '0.1.0'

# This instance of client is imported and used everywhere
client = Client()

from .resource import GamerProfile, Clip
