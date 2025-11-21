"""
Data Model - Handles business logic and data processing
"""
from pathlib import Path
from typing import List, Tuple, Optional


class DataModel:
    """Model for processing log files and extracting data"""
    
    def __init__(self):
        self.mfg_keyword = "mfg_data: 0x0A050000"
        self.invalid_mfg = "0xFFFFFFFF"
        self.sn_keyword = "PCBA SN No          :"
        self.total_files = 0
        self.processed_files = 0
        self.found_items = []
        
    def process_folder(self, folder_path: str) -> List[Tuple[str, str, bool]]:
        """
        Process all files in a folder
        Returns: List of (filename, serial_number, is_invalid)
        """
        results = []
        folder = Path(folder_path)
        
        if not folder.exists():
            return results
            
        files = list(folder.glob("*.*"))
        self.total_files = len(files)
        self.processed_files = 0
        
        for file in files:
            result = self._process_file(file)
            if result:
                results.append(result)
            self.processed_files += 1
                
        self.found_items = results
        return results
    
    def _process_file(self, file_path: Path) -> Optional[Tuple[str, str, bool]]:
        """
        Process a single file
        Returns: (filename, serial_number, is_invalid) or None
        """
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
                
            # Check for mfg_keyword
            has_mfg_keyword = any(self.mfg_keyword in line for line in lines)
            if not has_mfg_keyword:
                return None
            
            # Check if it's invalid (0xFFFFFFFF)
            has_invalid_mfg = any(self.invalid_mfg in line for line in lines)
            
            # Extract serial number
            for line in lines:
                if self.sn_keyword in line:
                    sn = line.split(":")[-1].strip()
                    return (file_path.name, sn, has_invalid_mfg)
                    
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            
        return None
    
    def get_progress(self) -> Tuple[int, int, float]:
        """
        Returns: (processed, total, percentage)
        """
        if self.total_files == 0:
            return (0, 0, 0.0)
        percentage = (self.processed_files / self.total_files) * 100
        return (self.processed_files, self.total_files, percentage)
    
    def get_statistics(self) -> dict:
        """Get statistics about processed data"""
        total = len(self.found_items)
        invalid = sum(1 for _, _, is_invalid in self.found_items if is_invalid)
        valid = total - invalid
        
        return {
            "total": total,
            "valid": valid,
            "invalid": invalid
        }

