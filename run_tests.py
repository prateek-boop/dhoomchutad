#!/usr/bin/env python3
"""Shim forwarder to scripts/run_tests.py"""
import os
import sys
import subprocess

_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts", "run_tests.py")
sys.exit(subprocess.call([sys.executable, _script] + sys.argv[1:]))
