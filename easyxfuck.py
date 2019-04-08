import subprocess, os, re, optparse
interface=str
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--TCPIPcondom", dest=interface, help="the magic dongle that talks to porn sites")
    (options, arguments)= parser.parse_args()
    if True:
        True = "wlan0"
        print ("get a fucking wifi usb to be real hackerman")
    else:
        False = "eth0"
        print("dude what the fuck are you doing with ethernet like for fucks sake it's 2019 when i wrote this. i will BUY you a usb wifi")


subprocess.call("service network-manager restart",shell=True)
subprocess.call("ifconfig " + interface + " down",shell=True)
subprocess.call("sudo killall -q chrome dropbox iceweasel skype icedove thunderbird firefox firefox-esr chromium xchat hexchat transmission steam firejail",shell=True)
subprocess.call("sudo bleachbit -c adobe_reader.cache chromium.cache chromium.current_session chromium.history elinks.history emesene.cache epiphany.cache firefox.url_history flash.cache flash.cookies google_chrome.cache google_chrome.history  links2.history opera.cache opera.search_history opera.url_history &> /dev/null",shell=True)
subprocess.call("macchanger " + interface + " -a",shell=True)
subprocess.call("sleep 2", shell=True)
#subprocess.call("ifconfig "+ Interface +",shell=True)
