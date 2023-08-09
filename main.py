import subprocess
import time
import argparse

def disconnect_wifi(ssid):
    subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=disable"])
    print(f"Disconnected from {ssid}")

def connect_wifi(ssid):
    subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=enable"])
    subprocess.run(["netsh", "wlan", "connect", "name=", f'"{ssid}"'])
    print(f"Connected to {ssid}")

def main():
    parser = argparse.ArgumentParser(description="Connect to a Wi-Fi network and run for a specified duration.")
    parser.add_argument("--ssid", required=True, help="Wi-Fi network SSID")
    parser.add_argument("--run_dur", type=int, required=True, help="Run duration in seconds ( 3600 ~ 1h ; 7200 ~ 2h ; 10800 ~ 3h)")
    parser.add_argument("--disc_dur", type=int, required=True, help="Duration to disconnect in seconds ( 4 recommended)")
    parser.add_argument("--conn_dur", type=int, required=True, help="Duration that will remain connected in seconds ( 240 ~ 4 min)")
    args = parser.parse_args()

    wifi_ssid = args.ssid
    run_duration = args.run_dur
    disconnect_duration = args.disc_dur
    connected_duration = args.conn_dur

    start_time = time.time()
    while time.time() - start_time < run_duration:
        disconnect_wifi(wifi_ssid)
        time.sleep(disconnect_duration)
        connect_wifi(wifi_ssid)
        time.sleep(connected_duration)

if __name__ == "__main__":
    main()

#example: python main.py --ssid internetSSID --run_dur 10800 --disc_dur 3 --conn_dur 240