from sh import ssh
import os, sys

# open stdout in unbuffered mode
sys.stdout = os.fdopen(sys.stdout.fileno(), "wb", 0)

aggregated = ""
def ssh_interact(char, stdin):
    global aggregated
    sys.stdout.write(char.encode())
    aggregated += char
    if aggregated.endswith("password: "):
        stdin.put("cs351\n")

p = ssh("1PI09IS020@119.82.126.182", _out=ssh_interact, _out_bufsize=0 ,_tty_in=True)
p.wait()