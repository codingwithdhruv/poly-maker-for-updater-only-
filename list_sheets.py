from poly_utils.google_utils import get_spreadsheet

print("Connecting...")
try:
    spreadsheet = get_spreadsheet()
    print(f"Connected to: '{spreadsheet.title}'")
    print("Worksheets found:")
    for ws in spreadsheet.worksheets():
        print(f" - '{ws.title}' (ID: {ws.id})")
except Exception as e:
    print(f"Error: {e}")
