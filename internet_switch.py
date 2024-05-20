import subprocess
import time
primary_ssid = "GDHathway5.8G"
primary_password = "87654321"
secondary_ssid = "Ghanshyam Digital 5G"
secondary_password = "87654321"

def connect_to_wifi(ssid, password):
    try:
        print(f"Connecting to {secondary_ssid}")
        subprocess.run(['nmcli','GDHathway2.4G','wifi', 'connect', 'ssid', '87654321', password],check=True)
        print(f"Connected to {secondary_ssid}")
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to connect to {secondary_ssid}")
        return False
    
    def is_connected():
        try: 
            result = subprocess.run(['nmcli', '-t', '-f', 'ACTIVE,SSID','con', 'show', '--active'], check=True, capture_output=True, text=True)
            if primary_ssid in result.stdout:
                print(f"currently connected to {primary_ssid}")
                return True
            elif secondary_ssid in result.stdout:
                print(f"currently connected to {secondary_ssid}")
                return True
            else:
                print("not connected to any preffered network")
                return False
        except subprocess.CalledProcessError:
            print("Error checking connection status")
            return False
        
        def main():
          while True:
              if not is_connected ():
                  if not connect_to_wifi(primsry_ssid, primary_password):
                      connect_to_wifi(secondary_ssid,secondary_password)
              time.sleep(10) #check every 10 seconds 
              if __name__ == "__main__":
                  main()              
