#!/usr/bin/env python3
__author__ = 'saipc'

# python3 -m Tests.email_form_retriever_tests --verbose
# python3 -m Tests.fuzzer_tests --verbose

import os
import subprocess

testDir = "Tests"
testDirContents=os.listdir("./" + testDir)
flags = " --verbose"

for file in testDirContents:
    if (file.endswith("_tests.py")):
        # run the test
        fileWithoutExtension = file[:-3]
        subprocess.call("python3 -m Tests." + fileWithoutExtension + flags, shell=True)
        print(file)


