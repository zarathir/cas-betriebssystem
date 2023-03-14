import os
import subprocess

if __name__ == "__main__":

    tail = subprocess.Popen(["tail", "-f", "logdatei"], cwd=os.getcwd())

    while not tail.stderr:
        out = tail.stdout
        if out is not None:
            print(tail.stdout)