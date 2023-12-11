import can

# Create a CAN bus interface
bus = can.interface.Bus(channel='can0', bustype='socketcan')

# Define a UDS message for ECU ID 0x04 and DID F188
uds_request = can.Message(
    arbitration_id=0x04,  # ECU ID
    data=[0xF1, 0x88],  # DID and sub-function
    extended_id=False,
)

# Send the UDS message
bus.send(uds_request)

# Receive UDS response
uds_response = bus.recv()

# Check for successful response
if uds_response.id == 0x7E8:
    # Extract fault codes from response data
    fault_codes = uds_response.data
    print("Fault codes:", fault_codes)
else:
    print("UDS request failed. Response ID:", uds_response.id)