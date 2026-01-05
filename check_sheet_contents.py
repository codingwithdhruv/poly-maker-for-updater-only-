from poly_utils.google_utils import get_spreadsheet
import pandas as pd

print("--- Checking Sheet Contents ---")
spreadsheet = get_spreadsheet()

# 1. Check Selected Markets
print("\nReading 'Selected Markets'...")
wk_sel = spreadsheet.worksheet("Selected Markets")
sel_data = wk_sel.get_all_records()
if not sel_data:
    print("❌ 'Selected Markets' is EMPTY.")
else:
    print(f"✅ Found {len(sel_data)} rows in 'Selected Markets'.")
    print("First few selections:")
    for row in sel_data[:3]:
        print(f" - '{row.get('question', 'UNKNOWN')}'")

# 2. Check All Markets
print("\nReading 'All Markets'...")
wk_all = spreadsheet.worksheet("All Markets")
all_data = wk_all.get_all_records()
if not all_data:
    print("❌ 'All Markets' is EMPTY.")
else:
    print(f"✅ Found {len(all_data)} rows in 'All Markets'.")
    
    # 3. Cross-Reference
    if sel_data:
        print("\nChecking if Selections exist in All Markets...")
        all_questions = {row.get('question') for row in all_data}
        for row in sel_data:
            q = row.get('question')
            if q in all_questions:
                print(f"✅ Found: '{q}'")
            else:
                print(f"❌ NOT FOUND in 'All Markets': '{q}'")
                print("   (This means the market name doesn't match anything in the current Polymarket feed)")

print("\n--- End Check ---")
