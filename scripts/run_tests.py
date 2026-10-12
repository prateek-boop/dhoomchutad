#!/usr/bin/env python3
"""
EduEagle Unified Automated Test Suite Runner
Starts the local server (if not already running) and executes all verification suites.
"""

import os
import sys
import time
import subprocess
import urllib.request
import urllib.error

_curr_dir = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(_curr_dir) == "scripts":
    REPO_DIR = os.path.dirname(_curr_dir)
else:
    REPO_DIR = _curr_dir

TESTS_DIR = os.path.join(REPO_DIR, "tests")
BASE_URL = "http://127.0.0.1:8000"

TEST_SUITES = [
    ("6 Core Functional Modules & RBAC", "test_new_modules.py"),
    ("Frontend, SEO & Metadata", "test_frontend_seo.py"),
    ("Mobile UX & Institutional Compliance", "test_mobile_ux.py"),
    ("Comprehensive Security & Signatures", "test_security.py"),
    ("20-Point Defensive Security & Untrusted User", "test_untrusted_user.py"),
    ("EagleMentor AI Chatbot & NEP 2020 Derivations", "test_ai_chatbot.py"),
]

def is_server_running():
    try:
        req = urllib.request.Request(f"{BASE_URL}/robots.txt", method="GET")
        with urllib.request.urlopen(req, timeout=1.5) as resp:
            return resp.status == 200
    except Exception:
        return False

def reset_server_limits():
    try:
        req = urllib.request.Request(f"{BASE_URL}/api/test/reset-limits", data=b"{}", headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=2) as resp:
            pass
    except Exception:
        pass

def main():
    print("=" * 68)
    print("      EDUEAGLE AUTOMATED VERIFICATION & TEST SUITE RUNNER       ")
    print("=" * 68)

    started_server = False
    server_proc = None

    if not is_server_running():
        print("[*] Local EduEagle server not running. Launching server.py...")
        server_py = os.path.join(REPO_DIR, "server.py")
        test_env = os.environ.copy()
        test_env["EDUEAGLE_RATE_LIMIT_AUTH"] = "60"
        test_env["EDUEAGLE_RATE_LIMIT_API"] = "120"
        test_env["EDUEAGLE_STORAGE_DIR"] = "private_storage"
        test_env["EDUEAGLE_DB_PATH"] = "edueagle.db"
        server_proc = subprocess.Popen([sys.executable, server_py], cwd=REPO_DIR, env=test_env)
        started_server = True

        # Wait for server to come online
        for _ in range(25):
            time.sleep(0.3)
            if is_server_running():
                print("[+] Server started successfully on http://127.0.0.1:8000\n")
                break
        else:
            print("[!] Error: Timed out waiting for server to start.")
            if server_proc:
                server_proc.terminate()
            sys.exit(1)
    else:
        print("[*] Detected running server at http://127.0.0.1:8000\n")

    results = []
    overall_passed = True

    try:
        for suite_name, script_file in TEST_SUITES:
            reset_server_limits()
            script_path = os.path.join(TESTS_DIR, script_file)
            print("-" * 68)
            print(f"RUNNING: {suite_name} ({script_file})")
            print("-" * 68)

            res = subprocess.run([sys.executable, script_path], cwd=REPO_DIR)
            passed = (res.returncode == 0)
            results.append((suite_name, script_file, passed))
            if not passed:
                overall_passed = False
            print()
            # Brief cooldown between suites to allow token bucket refill
            time.sleep(0.5)

    finally:
        if started_server and server_proc:
            print("[*] Terminating temporary test server...")
            server_proc.terminate()
            server_proc.wait()
            print("[+] Test server stopped.")

    print("\n" + "=" * 68)
    print("                     TEST SUMMARY REPORT                        ")
    print("=" * 68)
    for suite_name, script_file, passed in results:
        status_tag = "[PASS]" if passed else "[FAIL]"
        print(f"  {status_tag:6}  {suite_name:46} ({script_file})")
    print("=" * 68)

    if overall_passed:
        print("\nALL TEST SUITES PASSED SUCCESSFULLY! (100% PASS)\n")
        sys.exit(0)
    else:
        print("\nSOME TESTS FAILED! Review output above for details.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
