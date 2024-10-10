# Main Redirect Url: https://www.roblox.com/download/client

import requests
import os
import dmglib
import subprocess
import time
# import psutil

print("Downloading Roblox installer... This may take a minute.")
response = requests.get("https://www.roblox.com/download/client", headers={
	"Sec-Ch-Ua-Platform": "macOS",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
})

print("Mounting installer")
with open("roblox.dmg", "wb") as f:
	f.write(response.content)

try:
	dmg = dmglib.DiskImage("roblox.dmg")
	dmg.attach()
except dmglib.AlreadyAttached:
	pass

print("Installing Roblox... This may take 2-3 minutes.")
process = subprocess.Popen("/Volumes/RobloxPlayerInstaller/RobloxPlayerInstaller.app/Contents/MacOS/RobloxPlayerInstaller", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

while True:
	if process.poll() is not None:
		break

process.kill()

print("Patching Roblox... this will take a few seconds.")

home_dir = os.path.expanduser("~")
roblox_dir = home_dir + "/Applications/Roblox.app/Contents/MacOS"
app_dir = home_dir + "/Applications/Roblox.app"

time.sleep(0.2)

dummy_name = "COPYCOPYCOPYTESTCOPY"

os.rename(app_dir, home_dir + f"/Applications/{dummy_name}.app")
os.rename(roblox_dir + "/RobloxPlayer", roblox_dir + "/robloxPlayer")

time.sleep(12)

os.rename(home_dir + f"/Applications/{dummy_name}.app", app_dir)

print("Roblox has been successfully patched! You can now open Roblox on your dock.")