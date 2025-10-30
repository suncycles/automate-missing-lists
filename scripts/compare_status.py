#!/usr/bin/env python3
import json
import sys
import csv

# KEYWORDS. Edit as needed. 
EMS_MAP = {
    'Delivered': 0,
    'Lost': 0,
    'Available': 1
}

FOLIO_MAP = {
    'Missing': 0,
    'Available': 1,
    'Claimed returned': 1
}

def load_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        sys.exit(1)

"""
normalize_status( args: Source File, Keyword status ) 
    Use Keyword Map to compare statuses between FOLIO and EMS
returns comparison as according to map.
"""

def normalize_status(source, status):
    mapping = FOLIO_MAP if source == 'FOLIO' else EMS_MAP
    return mapping.get(status, None)
    
"""
compare_files( args: file (FOLIO Search Result), file (EMS Search Results)
    Compare FOLIO and EMS data.
    Preserves the original order of FOLIO entries, so you can directly copy-paste the csv into the sheet afterward.
returns: results as csv with complete context. 
"""
def compare_files(folio_data, ems_data):
    
    results = []
    seen_keys = set()

    for key in folio_data.keys():
        folio_status = folio_data.get(key)
        ems_status = ems_data.get(key)
        folio_val = normalize_status('FOLIO', folio_status)
        ems_val = normalize_status('EMS', ems_status)

        match = folio_val == ems_val if folio_val is not None and ems_val is not None else None
        results.append({
            'item_id': key,
            'FOLIO_status': folio_status,
            'EMS_status': ems_status,
            'match': match
        })
        seen_keys.add(key)

    return results
    
"""
    Write to csv.
    uses "No mismatch" and "Mismatch" 
"""
def write_csv(results, filename="../results.csv"):

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Item ID', 'FOLIO Status', 'EMS Status', 'Result'])

        for r in results:
            if r['match'] is None:
                result_text = 'Unknown (missing data)'
            elif r['match']:
                result_text = 'No mismatch'
            else:
                result_text = 'Mismatch'

            writer.writerow([r['item_id'], r['FOLIO_status'], r['EMS_status'], result_text])

    print(f"{len(results)} results written to {filename}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py FOLIOfile EMSfile")
        sys.exit(1)

    folio_file = sys.argv[1]
    ems_file = sys.argv[2]

    folio_data = load_json(folio_file)
    ems_data = load_json(ems_file)

    results = compare_files(folio_data, ems_data)
    
    # Write results to csv
    write_csv(results)

if __name__ == "__main__":
    main()
