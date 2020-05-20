import os

os.system('pkg install python-y')
os.system('pip install V7xStyle')
os.system('apt-get install python3-pip')
os.system('pip install V7xStyle')
####################################################
import os
from V7xStyle import Animation
from time import sleep as timeout
import time
##################################################################################

os.system('pip install V7xStyle')
os.system('clear')
os.system('pip3 install V7xStyle')
os.system('clear')
###############################
#Colors 
Black="\[\033[0;30m\]" # Black
Red="\[\033[0;31m\]" # Red
Green="\[\033[0;32m\]" # Green
Yellow="\[\033[0;33m\]" # Yellow
Blue="\[\033[0;34m\]" # Blue
Purple="\[\033[0;35m\]" # Purple
Cyan="\[\033[0;36m\]" # Cyan
White="\[\033[0;37m\]" # White

############################
def D() :
    Animation.DL(text='khaled ',
                t=0.5,
    )
######################################################
def k() :
    Animation.Text(text=' ',
                   AT='Done...',
                   CLT='\033[0;36m',
                   CUT='\033[0;35m',
                   t=0.3,
    )

###################################################3


def h() :
    os.system('clear')
    print ("\033[0;31m _     _   _____   _____   _   _   ")
    time.sleep(0.2)
    print ("\033[0;32m| |   / / /  _  \ /  ___| | | / /  ")
    time.sleep(0.2)
    print ("\033[0;33m| |  / /  | |_| | | |___  | |/ /   ")
    time.sleep(0.2)
    print ("\033[0;34m| | / /   }  _  { |  _  \ | |\ \   ")
    time.sleep(0.2)
    print ("\033[0;35m| |/ /    | |_| | | |_| | | | \ \  ")
    time.sleep(0.2)
    print ("\033[0;36m|___/     \_____/ \_____/ |_|  \_\ ")
    print (" ")
    k()
    print (" ")
    os.system('clear')
#####################################################################################3
def termux() :
    os.system('pkg install python -y')
    os.system('clear')
    D()
    os.system('apt update && apt upgrade -y')

    os.system('pip install V7xStyle')
    os.system('clear')
    D()
    os.system('chmod +x *')
    os.system('clear')
    D()
    os.system('pkg install git -y')
    os.system('pkg install python2 -y')
    os.system('pkg install python3 -y')
    os.system('mkdir khaled-hash')

    os.system('clear')
    D()
    os.system('clear')
########################################################################################3
def lunix() :
    os.system('apt-get update')
    os.system('apt-get upgrade -y')
    os.system('apt-get install python3 -y')
    D()
    os.system('clear')
    D()
    os.system('pip3 install V7xStyle')
    os.system('clear')
    D()
    os.system('apt-get install python -y')
    os.system ('apt-get install git -y')

    os.system('chmod +x *')
    os.system('clear')
    D()
    os.system('mkdir khaled-hash')
    D()
    os.system('clear')

#########################################################################################

E = '''
\033[0;31m _____                       
\033[0;32m| ____|  _ __    ___    _ __ 
\033[0;33m|  _|   | '__|  / _ \  | '__|
\033[0;34m| |___  | |    | (_) | | |   
\033[0;35m|_____| |_|     \___/  |_|   
\033[0;36m                             
'''

##########################################################################################
def hhh() :
    h()
    print ("\033[0;32m_______________________________")
    time.sleep(0.2)
    print ("\033[0;32m||                            ||")
    time.sleep(0.2)
    print ("\033[0;33m||1. termux                   ||")
    time.sleep(0.2)
    print ("\033[0;32m||                            ||")
    time.sleep(0.2)
    print ("\033[0;32m||                            ||")
    time.sleep(0.2)
    print ("\033[0;33m||2. lunix                    ||")
    time.sleep(0.2)
    print ("\033[0;32m||                            ||")
    time.sleep(0.2)
    print ("\033[0;32m||----------------------------||")
    time.sleep(0.2)
    print (" ")
    i = input ("\033[0;36mchoice 1 or 2 =======>> \033[0;31m")
    if i == "1" :
        termux()
    elif i == "2" :
        lunix()
    else :
        print (E)
        time.sleep(0.6)
        os.system('clear')
        hhh()

hhh()
