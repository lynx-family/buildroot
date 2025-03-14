#!/usr/bin/env python3
# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import shutil
import subprocess
import sys

def clean(output_dir):
  if os.path.exists(output_dir):
        shutil.rmtree(output_dir, ignore_errors=True)
  return


def generate_headers(output_dir):
  """Run cppwinrt.exe on the installed Windows SDK version and generate
  cppwinrt headers in the output directory.
  """
  
  cppwinrt_exe = os.path.join(
  __file__,
  '..\\..\\..\\third_party\\cppwinrt\\bin\\cppwinrt.exe')

  args = [cppwinrt_exe, '-in', 'sdk',
      '-out', '%s' % output_dir]

  subprocess.check_output(args)

  return 0


def main(argv):
  generated_dir = os.path.join(
  __file__,
  '..\\..\\..\\third_party\\cppwinrt\\generated')
  clean(generated_dir)
  return generate_headers(generated_dir)

if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]))
