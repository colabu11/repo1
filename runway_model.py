import subprocess
#subprocess.call("ls && ./ngrok authtoken 1siBHweElRgvcNTEIHUR49WPfcv_5rbwdTbBB5q9cMLJwYcme && ./ngrok tcp 22 --log=stdout > ngrok.log", shell=True)
subprocess.call("./ngrok tcp 22", shell=True)
