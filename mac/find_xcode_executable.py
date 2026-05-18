#!/usr/bin/env python3
# Copyright 2020 The Lynx Authors. All rights reserved.

"""Find the full path to executable NAME in the provided SDK and toolchain of Xcode.

Usage:
  python find_xcode_executable.py clang
"""

import subprocess
import sys

from argparse import ArgumentParser


def main():
  parser = ArgumentParser()
  parser.add_argument("name", help="The name of the executable to find")
  args = parser.parse_args()

  job = subprocess.Popen(['xcrun', '-find', args.name],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
  out, err = job.communicate()
  out = out.decode().strip()
  if job.returncode == 0 and out:
    return out

  job = subprocess.Popen(['xcodebuild', '-find-executable', args.name],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
  out, err = job.communicate()
  out = out.decode().strip()
  if job.returncode != 0 or not out:
    sys.stderr.writelines([out, err.decode()])
    raise Exception(('Error %d running xcodebuild, please check if you have Xcode installed on your system') % job.returncode)

  return out


if __name__ == '__main__':
  if sys.platform != 'darwin':
    raise Exception("This script only runs on Mac")
  print((main()))
