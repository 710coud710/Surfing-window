"""
Data Model - Handles business logic and data processing
"""
from pathlib import Path
from typing import List, Tuple, Optional
from datetime import datetime
import re


class DataModel:
    """Model for processing log files and extracting data"""
    
    def __init__(self):
        self.mfg_keyword = "mfg_data:"
        self.invalid_mfg = "0xFFFFFFFF"
        self.sn_keyword = "PCBA SN No          :"
        self.test_program_keyword = "Test Program        :"
        self.total_files = 0
        self.processed_files = 0
        self.found_items = []
        
    def process_folder(self, folder_path: str) -> List[Tuple[str, str, bool, str]]:
        """
        Process all files in a folder
        Returns: List of (filename, serial_number, is_invalid, check_time)
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
    
    def _process_file(self, file_path: Path) -> Optional[Tuple[str, str, bool, str]]:
        """
        Process a single file
        Returns: (filename, serial_number, is_invalid, check_time) or None
        """
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
            
            # Step 1: Check if file has "MP" in Test Program
            has_mp_program = False
            for line in lines:
                if self.test_program_keyword in line:
                    # Extract test program name
                    program_name = line.split(":")[-1].strip()
                    # Check if "MP" is after 2nd underscore
                    # Example: Hapuka_ADL1_MP_V1.1.csv
                    parts = program_name.split("_")
                    if len(parts) >= 3 and parts[2].startswith("MP"):
                        has_mp_program = True
                        break
            
            # If no MP program, skip this file
            if not has_mp_program:
                return None
            
            # Step 2: Check for mfg_data line with 0xFFFFFFFF (ONLY Invalid)
            is_invalid = False
            
            for i, line in enumerate(lines):
                if self.mfg_keyword in line:
                    # ONLY catch if this line contains 0xFFFFFFFF (invalid)
                    if self.invalid_mfg in line:
                        is_invalid = True
                        break
            
            # If not invalid (0xFFFFFFFF), skip this file
            if not is_invalid:
                return None
            
            # Step 3: Extract serial number
            serial_number = "N/A"
            for line in lines:
                if self.sn_keyword in line:
                    serial_number = line.split(":")[-1].strip()
                    break
            
            # Step 4: Get check time (current time)
            check_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            return (file_path.name, serial_number, is_invalid, check_time)
                    
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
        invalid = sum(1 for _, _, is_invalid, _ in self.found_items if is_invalid)
        valid = total - invalid
        
        return {
            "total": total,
            "valid": valid,
            "invalid": invalid
        }

