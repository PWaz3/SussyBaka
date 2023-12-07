from netmiko import ConnectHandler
import requests
import json

# Define your API URL and API token
api_url = 'http://localhost:8080/api/v0'  # Replace with your LibreNMS API URL
api_token = '8cb9a0c868ec941994434e7ba0248a41'  # Replace with your API token
# Define the API endpoint to list devices
endpoint = 'devices'

# Set the request headers with the API token for authentication
headers = {
    'X-Auth-Token': api_token,
    'Content-Type': 'application/json',
}

# Make the API request to list devices
try:
    response = requests.get(f'{api_url}/{endpoint}', headers=headers)
    response.raise_for_status()  # Check for HTTP status code errors

    # Parse the JSON response into a Python dictionary
    response_data = json.loads(response.text)

    # Check if devices are nested under a key, e.g., "devices"
    if "devices" in response_data:
        devices = response_data["devices"]
    else:
        devices = response_data  # Assume devices are at the root level

    for device in devices:
    
        # Extract specific fields
        deviceID = device.get('device_id', '')
        #host = device.get('ip', '')
        #operatingSys = device.get('os', '')

        if deviceID == 2:
            deviceID = device.get('device_id','') 
            host = device.get('hostname', '')
            operatingSys = device.get('os', '')
            
            if operatingSys == "iosxr":
                operatingSys = "cisco_xr"
    
    print(deviceID, host, operatingSys)
    cisco_881 = {
        'device_type': operatingSys,
        'host': host,
        'username': 'username',
        'password': 'password', 
    }

    
    net_connect = ConnectHandler(**cisco_881)
    
    commandList = [
        'show interfaces descriptions',
        'show controllers optics',
        'show inventory',
        'show log | exc SSHD',
        'show alarms brief',
        'show alarms detail',
        'show watchdog memory-state',
        'show ethernet loopback active',
        'show version',
        'show l2vpn xconnect',
        'show l2vpn bridge-domain',
        'show l2vpn xconnect detail',
        'show running-config l2vpn',
        'show bfd session',
        'show isis adjacency',
        'show run router isis',
        'show bgp sessions',
        'show bgp neighbors',
        'show run router bgp',
        'show arp'
    ]
    file= open ('myfile.txt','w')
    
    for x in commandList:
        print("running: ", x)
        #print(net_connect.send_command(x, expect_string=r"#"))
        #json.dump((net_connect.send_command(x, expect_string=r"#")), file, indent=2)
        file.write(net_connect.send_command(x, expect_string=r"#"))
        file.write('\n')
    print("Data has been saved to myfile.txt")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
