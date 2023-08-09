import subprocess

def get_connected_wifi_ssids():
    result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
    output = result.stdout

    connected_ssids = []
    lines = output.split('\n')
    for line in lines:
        if "SSID" in line:
            ssid = line.split(":")[1].strip()
            connected_ssids.append(ssid)

    return connected_ssids

def main():
    connected_ssids = get_connected_wifi_ssids()

    if connected_ssids:
        print("Connected Wi-Fi SSIDs:")
        for ssid in connected_ssids:
            print(ssid)
    else:
        print("No Wi-Fi networks are currently connected.")

if __name__ == "__main__":
    main()