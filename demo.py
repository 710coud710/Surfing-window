from pathlib import Path

folder_path = Path(r"D:\Beta\Surfing\Logs")  # dùng raw string

mfg_keyword = "mfg_data: 0x0A050000"
sn_keyword = "PCBA SN No          :"

files = list(folder_path.glob("*.*"))

for file in files:
    try:
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            
            # Kiểm tra mfg_keyword
            if any(mfg_keyword in line for line in lines):
                # Lấy các dòng có SN
                for line in lines:
                    if sn_keyword in line:
                        sn = line.split(":")[-1].strip()
                        print(f"File: {file.name} | SN: {sn}")
                        
    except Exception as e:
        print(f"Error reading file {file}: {e}")
