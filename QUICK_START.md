# ⚡ Quick Start Guide - Surfing

Get up and running in 2 minutes!

---

## 🚀 Installation (30 seconds)

```bash
# Install dependencies
pip install -r requirements.txt
```

That's it! Just one dependency: **PySide6**

---

## ▶️ Run the Application (5 seconds)

### Option 1: Python Command
```bash
python main.py
```

### Option 2: Batch File (Windows)
```bash
run.bat
```

The application will launch immediately!

---

## 📝 Basic Usage (1 minute)

### Step 1: Select Folder
1. Click **"Browse"** button
2. Navigate to your folder containing log files
3. Select the folder (e.g., `D:\Beta\Surfing\Logs`)

### Step 2: Choose Filter (Optional)
- **Show All Results** ← Default, shows everything
- **Show Only Invalid** ← Only files with 0xFFFFFFFF
- **Show Only Valid** ← Only valid files

### Step 3: Process
1. Click **"▶ Start Processing"**
2. Watch the progress bar in real-time
3. Results appear automatically when done!

### Step 4: Export (Optional)
1. View results in the table
2. Click **"📥 Export"**
3. Save as CSV file

---

## 📂 Test with Sample Data

The project includes sample log files in the `Logs/` folder:

```bash
# Run and test with included files
python main.py

# Then browse to: D:\Beta\Surfing\Logs
```

---

## 🎯 What Does It Do?

Searches log files for:
- ✅ Keyword: `mfg_data: 0x0A050000`
- ✅ Invalid marker: `0xFFFFFFFF`
- ✅ Serial numbers: `PCBA SN No`

Results show:
- File names
- Serial numbers
- Status (Valid ✅ or Invalid ❌)

---

## 🎨 Navigation

### Sidebar Menu
- **📊 Dashboard** - Main screen, file processing
- **🔄 Process Files** - Same as Dashboard
- **📋 Results** - View processed results
- **⚙️ Settings** - Coming soon
- **ℹ️ About** - Application info

### Sections
- **Header** - Progress bar and stats
- **Content** - Main work area
- **Terminal** - Logs and messages

---

## 💡 Quick Tips

### Tip 1: Watch the Terminal
The terminal at the bottom shows what's happening:
- 🔵 **[INFO]** - Normal information
- 🟢 **[SUCCESS]** - Operation completed
- 🔴 **[ERROR]** - Something went wrong
- 🟡 **[WARNING]** - Be careful

### Tip 2: Resize Sections
Drag the divider between Content and Terminal to adjust sizes!

### Tip 3: Clear Terminal
Click **"🗑️ Clear"** button to clear terminal logs

### Tip 4: Check Statistics
Results view shows:
- **Total**: All files found
- **Valid**: Files without 0xFFFFFFFF
- **Invalid**: Files with 0xFFFFFFFF

---

## 🔧 Troubleshooting

### Problem: Application won't start
**Solution**: Make sure PySide6 is installed
```bash
pip install PySide6
```

### Problem: No results found
**Solution**: Check if files contain `mfg_data: 0x0A050000`

### Problem: Can't see terminal
**Solution**: Drag the splitter up to make terminal larger

---

## 📁 Project Structure (Simple View)

```
Surfing/
├── main.py          ← Run this!
├── requirements.txt ← Install this!
├── run.bat          ← Or run this! (Windows)
│
├── views/           ← UI components
├── model/           ← Data processing
└── presenter/       ← Coordination
```

---

## 🎓 Next Steps

Once you're comfortable with basic usage:

1. **Read Full Documentation**
   - `README.md` - Complete guide (English)
   - `HUONG_DAN_SU_DUNG.md` - Full guide (Vietnamese)

2. **Understand Architecture**
   - `ARCHITECTURE.md` - Technical details
   - `UI_GUIDE.md` - Design system

3. **Customize**
   - Modify colors in widget stylesheets
   - Add new features following MVP pattern
   - Extend model with new processing logic

---

## 🎯 Common Workflows

### Workflow 1: Quick Check
```
1. Launch app
2. Browse → Select folder
3. Start Processing
4. Review results
```
**Time**: < 1 minute

### Workflow 2: Filter Invalid Only
```
1. Launch app
2. Browse → Select folder
3. Choose "Show Only Invalid"
4. Start Processing
5. Export → Save as CSV
```
**Time**: < 2 minutes

### Workflow 3: Process Multiple Batches
```
1. Process first folder → View results
2. Click "Dashboard" in sidebar
3. Select new folder
4. Process again
5. Click "Results" to see latest
```
**Time**: Repeat as needed

---

## 📊 Example Output

### Console Output
```
[INFO] Starting to process folder: D:\Beta\Surfing\Logs
[INFO] Filter mode: all
[SUCCESS] Processing complete! Found 15 items
[INFO] Displaying 15 items after filter
```

### CSV Export
```csv
#,File Name,Serial Number,Status
1,Hoki_ADL1_...txt,GT54M503546500JW,Valid
2,Hapuka_ADL1_...txt,GT54FJ03545502V5,Invalid
```

---

## 🆘 Need Help?

1. **Check Terminal** - Often tells you what's wrong
2. **Read Documentation** - Comprehensive guides available
3. **Check File Format** - Ensure logs match expected format

---

## ✅ Checklist for First Run

Before your first use, make sure:

- [ ] Python 3.8+ installed
- [ ] PySide6 installed (`pip install -r requirements.txt`)
- [ ] You have log files to process
- [ ] Log files contain the expected keywords

---

## 🎉 You're Ready!

That's all you need to know to get started!

```bash
python main.py
```

**Happy sorting! 🏄‍♂️**

---

**Quick Start Version**: 1.0  
**Last Updated**: November 2025  
**Estimated Reading Time**: 2 minutes  
**Estimated Setup Time**: 30 seconds

