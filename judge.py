import glob
import subprocess
import os
path = os.path

SCRIPT = "script.py"
OUTPUT = "outputs"

if not path.exists(OUTPUT):
    os.mkdir(OUTPUT)

for f in glob.glob("inputs/*.in"):
    fin = open(f, 'r')
    fout = open(path.join(OUTPUT, path.basename(f).replace(".in", ".out")), 'w')
    p = subprocess.Popen(["py", "-3", SCRIPT], stdin=fin, stdout=fout, shell=True)
    p.wait()
    fout.close()


