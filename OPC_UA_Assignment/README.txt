OPC UA Client Development and Data Logging

Prerequisites:
- Python 3.x
- VS Code (optional)
- OPC UA Python library

Setup Steps:

1. Install required library:
   pip install opcua

2. Start OPC UA demo server:
   python opcua_demo_server.py

   Server runs at:
   opc.tcp://localhost:4840

   The server creates 10 dummy tags:
   Tag1 to Tag10.

3. Run OPC UA client:
   python opcua_client.py

4. Client behavior:
   - Reads 10 tags every minute
   - Logs data into CSV files
   - Creates a new CSV file every hour

Output:
- CSV files are generated inside 'sample_output' folder.
- File naming format:
  OPC_Log_YYYY-MM-DD_HH.csv
