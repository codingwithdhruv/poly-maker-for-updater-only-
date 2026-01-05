from poly_utils.google_utils import get_spreadsheet
from datetime import datetime
import os

print("--- Google Sheets Write Verification ---")

# 1. Check URL
url = os.getenv("SPREADSHEET_URL")
print(f"Target Spreadsheet URL: {url}")
if not url:
    print("❌ ERROR: SPREADSHEET_URL is missing from .env")
    exit(1)

# 2. Connect
try:
    print("Connecting to Google Sheets...")
    spreadsheet = get_spreadsheet()
    print(f"Successfully connected to: {spreadsheet.title}")
except Exception as e:
    print(f"❌ Connection Failed: {e}")
    exit(1)

# 3. Test Write
try:
    print("Attempting to write to 'All Markets' sheet...")
    wk = spreadsheet.worksheet("All Markets")
    
    # Write a test value to cell Z1 (far away)
    test_val = f"Test Write {datetime.now()}"
    print(f"Writing '{test_val}' to cell Z1...")
    wk.update_acell("Z1", test_val)
    
    # 4. Verify Read
    print("Reading back cell Z1...")
    read_val = wk.acell("Z1").value
    
    if read_val == test_val:
        print("\n✅ SUCCESS: Write verified! The Service Account has EDITOR permissions.")
        print("Please check your Google Sheet for 'Test Write...' in cell Z1.")
    else:
        print(f"\n❌ FAILURE: Read back '{read_val}' but expected '{test_val}'")
        
except Exception as e:
    print(f"\n❌ WRITE FAILED: {e}")
    print("Possible causes:")
    print("1. Service Account is 'Viewer' not 'Editor'")
    print("2. Wrong Spreadsheet URL")
