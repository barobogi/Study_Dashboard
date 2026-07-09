import sys
from pathlib import Path

def main():
    file_path = Path(r"d:\AI\260623_1_study_all\study-dashboard.html")
    out_path = Path(r"d:\AI\260623_1_study_all\study-dashboard_healed.html")
    
    # Read the corrupted file as string (UTF-8)
    content = file_path.read_text(encoding='utf-8', errors='replace')
    
    # Re-encode as CP949 to recover the original raw bytes, then decode as UTF-8
    try:
        raw_bytes = content.encode('cp949', errors='replace')
        healed_content = raw_bytes.decode('utf-8', errors='replace')
        
        # Write to healed file
        out_path.write_text(healed_content, encoding='utf-8')
        print("Success! Healed file written to:", out_path.name)
    except Exception as e:
        print("Error during healing:", e)

if __name__ == '__main__':
    main()
