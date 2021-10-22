# For testing, see your physical device's long lat coord: https://www.whatsmygps.com/
# IMPORTANT! GPS location must be enabled in Windows 10 manually

# Code adapted from https://stackoverflow.com/questions/44400560/using-windows-gps-location-service-in-a-python-script

#install pywin32 using `pip install pywin32` to use python in windows
import subprocess as sp
import re
import time

wt = 5 # Wait time -- I purposefully make it wait before the shell command
accuracy = 3 # 3 meters around the laptop but this can change
'''
while True:
    # Wait before powershell command or else the coordinates returned are from IP
    time.sleep(wt)

    # Access powershell
    pshellcomm = ['powershell']
    ''
    Breakdown of powershell commands:

    1. add-type -assemblyname system.device is needed to access Windows' System.Device.Location namespace
    2. new-object system.device.location.geocoordinatewatcher creates a location object
    3. loc.start will begin the process to get the device's current 
    4. while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied")) this checks the location permissions for the windows device
    5. start-sleep -milliseconds 100 is to wait for the location to be found
    ''

    pshellcomm.append('add-type -assemblyname system.device; '\
                      '$loc = new-object system.device.location.geocoordinatewatcher;'\
                      '$loc.start(); '\
                      'while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied")) '\
                      '{start-sleep -milliseconds 100}; '\
                      '$acc = %d; '\
                      'while($loc.position.location.horizontalaccuracy -gt $acc) '\
                      '{start-sleep -milliseconds 100; $acc = [math]::Round($acc*1.5)}; '\
                      '$loc.position.location.latitude; '\
                      '$loc.position.location.longitude; '\
                      '$loc.position.location.horizontalaccuracy; '\
                      '$loc.stop()' %(accuracy))

    # opens powershell and inputs the commands above
    p = sp.Popen(pshellcomm, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.STDOUT, text=True)
    (out, err) = p.communicate()

    # Get longitude and latitude from tuple
    out = re.split('\n', out)

    lat = float(out[0])
    long = float(out[1])

    print(lat, long)
    # This will go on forever unless you do Ctrl+C in the terminal
'''

# Wait before powershell command or else the coordinates returned are from IP
time.sleep(wt)

# Access powershell
pshellcomm = ['powershell']
'''
Breakdown of powershell commands:

1. add-type -assemblyname system.device is needed to access Windows' System.Device.Location namespace
2. new-object system.device.location.geocoordinatewatcher creates a location object
3. loc.start will begin the process to get the device's current 
4. while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied")) this checks the location permissions for the windows device
5. start-sleep -milliseconds 100 is to wait for the location to be found
'''

pshellcomm.append('add-type -assemblyname system.device; '\
                    '$loc = new-object system.device.location.geocoordinatewatcher;'\
                    '$loc.start(); '\
                    'while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied")) '\
                    '{start-sleep -milliseconds 100}; '\
                    '$acc = %d; '\
                    'while($loc.position.location.horizontalaccuracy -gt $acc) '\
                    '{start-sleep -milliseconds 100; $acc = [math]::Round($acc*1.5)}; '\
                    '$loc.position.location.latitude; '\
                    '$loc.position.location.longitude; '\
                    '$loc.position.location.horizontalaccuracy; '\
                    '$loc.stop()' %(accuracy))

# opens powershell and inputs the commands above
p = sp.Popen(pshellcomm, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.STDOUT, text=True)
(out, err) = p.communicate()

# Get longitude and latitude from tuple
out = re.split('\n', out)

lat = float(out[0])
lon = float(out[1])

print(lat, lon)

#https://stackoverflow.com/questions/1801732/how-do-i-link-to-google-maps-with-a-particular-longitude-and-latitude
url = "https://maps.google.com/?q=" + str(lat) + "," + str(lon)
print(url)
