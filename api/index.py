import sys
import os

# Add parent directory to sys.path so all core modules (server, database, security, validator) import seamlessly
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import server

# Vercel Serverless Function entry point
class handler(server.EduEagleAPIHandler):
    pass

