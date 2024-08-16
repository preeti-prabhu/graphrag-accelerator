import requests

api_key = 'QZU8LBoiLm1YqnT5nw2H6vVR+dAMRDlwacxd3T7xidw='
headers = {
    'Authorization': f'Basic {api_key}',
    'Content-Type': 'application/json'
}

# Replace 'BW LNG' and 'XYZ' with your actual company and vessel code
company = 'Hafnia'
vessel_code = 'ADA'
status = 'Scheduled'

url = f'http://dev-int.shippalm-bc.com:7048/SHIPPALM/api/aot/purchase/v1.0/workOrders?company={company}&vesselCode={vessel_code}&status={status}'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Upcoming Maintenance Schedules:")
    for work_order in data:
        print(f"Work Order: {work_order['number']}, Description: {work_order['description']}, Scheduled Date: {work_order['scheduledDate']}, Assigned To: {work_order['assignedPersonnel']}")
else:
    print(f'Error: {response.status_code}')
