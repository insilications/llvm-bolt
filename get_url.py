#!/usr/bin/env python

import re
import sys
import os
import requests
import subprocess
import shutil

def write_out(filename, content, mode="w"):
    """File.write convenience wrapper."""
    with open_auto(filename, mode) as require_f:
        require_f.write(content)

def open_auto(*args, **kwargs):
    """Open a file with UTF-8 encoding.

    Open file with UTF-8 encoding and "surrogate" escape characters that are
    not valid UTF-8 to avoid data corruption.
    """
    # 'encoding' and 'errors' are fourth and fifth positional arguments, so
    # restrict the args tuple to (file, mode, buffering) at most
    assert len(args) <= 3
    assert "encoding" not in kwargs
    assert "errors" not in kwargs
    return open(*args, encoding="utf-8", errors="surrogateescape", **kwargs)

def main():
    cwd = os.getcwd()
    filename = ""
    filename = [f.path for f in os.scandir(cwd) if f.is_file() and "llvm-bolt-" in f.name]

    if not filename:
        dirname = f"llvm-bolt-14.0.0"
        filename_tar = f"{cwd}/llvm-bolt-14.0.0.tar.gz"
        git_cmd = f"git clone -j8 --depth=1 --branch=main https://github.com/llvm/llvm-project.git {dirname}"
        try:
            process = subprocess.run(
                git_cmd,
                check=True,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                universal_newlines=True,
                cwd=cwd,
            )
        except subprocess.CalledProcessError as err:
            print(f"Unable to git in {cwd}: {err}")
            sys.exit(1)

        if not os.path.exists(filename_tar):
            tar_cmd = f"tar --create --file=- {dirname}/ | pigz -9 -p 16 > {filename_tar}"
            try:
                process = subprocess.run(
                    tar_cmd,
                    check=True,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    universal_newlines=True,
                    cwd=cwd,
                )
            except subprocess.CalledProcessError as err:
                print(f"Unable to tar {filename_tar} in {cwd}: {err}")
                sys.exit(1)

            try:
                shutil.rmtree(dirname, ignore_errors=False)
            except OSError as e:
                print("Error: %s : %s" % (dirname, e.strerror))
                sys.exit(1)

            filename_uri = f"file://{filename_tar}"
            print(filename_uri)
    else:
        filename_absolute = f"{filename[0]}"
        filename_uri = f"file://{filename_absolute}"
        print(filename_uri)

if __name__ == "__main__":
    main()
