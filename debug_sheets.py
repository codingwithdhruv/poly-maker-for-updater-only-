from poly_utils.google_utils import get_spreadsheet
import pandas as pd

print("Connecting to Google Sheets...")
spreadsheet = get_spreadsheet()

print("Fetching 'Selected Markets'...")
wk = spreadsheet.worksheet('Selected Markets')
df = pd.DataFrame(wk.get_all_records())
df = df[df['question'] != ""].reset_index(drop=True)
print(f"Selected Markets rows: {len(df)}")
if not df.empty:
    print(f"First Question in Selected: '{df.iloc[0]['question']}'")

print("Fetching 'All Markets'...")
wk2 = spreadsheet.worksheet('All Markets')
df2 = pd.DataFrame(wk2.get_all_records())
df2 = df2[df2['question'] != ""].reset_index(drop=True)
print(f"All Markets rows: {len(df2)}")

# Check for match
if not df.empty:
    target = df.iloc[0]['question']
    match = df2[df2['question'] == target]
    if match.empty:
        print(f"\nNO MATCH FOUND for: '{target}'")
        # fuzzy search manually
        print("Checking if it exists in 'All Markets' with slight differences...")
        for q in df2['question']:
            if target in q or q in target:
                print(f"Potential partial match: '{q}'")
    else:
        print(f"\nMATCH FOUND: '{target}'")

# Check merge
print("\nAttempting Merge...")
result = df.merge(df2, on='question', how='inner')
print(f"Merged Result rows: {len(result)}")
