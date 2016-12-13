from subprocess import Popen, PIPE
import sys


p = Popen([sys.argv[1], sys.argv[2]], stdout=PIPE)
p.communicate()
if p.returncode == -11:
    print ">Programe crashed"
