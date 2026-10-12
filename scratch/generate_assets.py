#!/usr/bin/env python3
"""Shim forwarder to scripts/generate_assets.py"""
import os
import sys

_script = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "generate_assets.py")
with open(_script, "r", encoding="utf-8") as f:
    exec(compile(f.read(), _script, "exec"), globals())
