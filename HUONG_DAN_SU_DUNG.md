# Hướng Dẫn Sử Dụng - Surfing ADL1 Data Sorting Tool

## Giới Thiệu

Surfing là ứng dụng desktop hiện đại được phát triển bằng PySide6, giúp phân loại và phân tích các file log test ADL1.

## Cài Đặt

### 1. Yêu Cầu Hệ Thống
- Python 3.8 trở lên
- Windows/Linux/MacOS

### 2. Cài Đặt Thư Viện

```bash
pip install -r requirements.txt
```

## Chạy Ứng Dụng

### Cách 1: Chạy trực tiếp
```bash
python main.py
```

### Cách 2: Sử dụng file batch (Windows)
```bash
run.bat
```

## Giao Diện Ứng Dụng

### 1. Sidebar (Thanh Điều Hướng Bên Trái)
- **Dashboard**: Màn hình chính để xử lý file
- **Process Files**: Chức năng xử lý file
- **Results**: Xem kết quả đã xử lý
- **Settings**: Cài đặt (đang phát triển)
- **About**: Thông tin ứng dụng

### 2. Header (Phần Đầu)
- Hiển thị tiến trình xử lý real-time
- Số file đã xử lý / Tổng số file
- Phần trăm hoàn thành với thanh progress bar

### 3. Content Area (Vùng Nội Dung Chính)

#### Dashboard Tab
- **Folder Selection**: Chọn thư mục chứa file log
- **Filter Options**: 
  - Show All Results: Hiển thị tất cả kết quả
  - Show Only Invalid: Chỉ hiển thị các file có giá trị 0xFFFFFFFF
  - Show Only Valid: Chỉ hiển thị các file hợp lệ
- **Search Keywords**: Thông tin về các từ khóa tìm kiếm

#### Results Tab
- Bảng kết quả với các cột:
  - **#**: Số thứ tự
  - **File Name**: Tên file
  - **Serial Number**: Số serial PCBA
  - **Status**: Trạng thái (Valid ✅ / Invalid ❌)
- Thống kê: Total, Valid, Invalid
- Nút Export để xuất kết quả ra CSV

### 4. Terminal (Phần Cuối)
- Hiển thị log messages
- Mã màu:
  - 🔵 [INFO]: Thông tin
  - 🟢 [SUCCESS]: Thành công
  - 🔴 [ERROR]: Lỗi
  - 🟡 [WARNING]: Cảnh báo

## Hướng Dẫn Sử Dụng Chi Tiết

### Bước 1: Chọn Thư Mục
1. Click vào nút **"Browse"**
2. Chọn thư mục chứa các file log ADL1 (ví dụ: folder "Logs")
3. Đường dẫn sẽ hiển thị trong ô text

### Bước 2: Chọn Bộ Lọc
- **Show All Results**: Xem tất cả các file có chứa mfg_data: 0x0A050000
- **Show Only Invalid**: Chỉ xem các file có giá trị 0xFFFFFFFF (không hợp lệ)
- **Show Only Valid**: Chỉ xem các file không có 0xFFFFFFFF (hợp lệ)

### Bước 3: Bắt Đầu Xử Lý
1. Click nút **"▶ Start Processing"**
2. Theo dõi tiến trình ở phần Header
3. Xem log chi tiết ở Terminal
4. Kết quả sẽ tự động hiển thị khi hoàn thành

### Bước 4: Xem và Xuất Kết Quả
1. Ứng dụng tự động chuyển sang tab Results
2. Xem bảng kết quả với các thông tin:
   - Tên file
   - Serial number
   - Trạng thái Valid/Invalid
3. Click **"📥 Export"** để xuất ra file CSV
4. Chọn vị trí lưu file

## Tiêu Chí Tìm Kiếm

Ứng dụng tìm kiếm các file dựa trên:

1. **Từ khóa bắt buộc**: `mfg_data: 0x0A050000`
   - File phải chứa từ khóa này mới được xử lý

2. **Kiểm tra Invalid**: `0xFFFFFFFF`
   - Nếu file chứa giá trị này → đánh dấu Invalid ❌
   - Nếu không chứa → đánh dấu Valid ✅

3. **Trích xuất Serial Number**: `PCBA SN No          :`
   - Lấy số serial từ dòng này

## Kiến Trúc Ứng Dụng

### MVP Pattern (Model-View-Presenter)

```
┌─────────────┐         ┌──────────────┐         ┌─────────┐
│    View     │ ←────→  │  Presenter   │ ←────→  │  Model  │
│  (UI/GUI)   │         │ (Điều phối)  │         │ (Logic) │
└─────────────┘         └──────────────┘         └─────────┘
```

### Cấu Trúc Thư Mục

```
Surfing/
├─ main.py                      # Điểm khởi đầu
├─ views/                       # Các thành phần UI
│   ├─ main_window.py           # Cửa sổ chính
│   ├─ sidebar_widget.py        # Sidebar
│   ├─ header_widget.py         # Header
│   ├─ content_widget.py        # Nội dung
│   ├─ result_widget.py         # Bảng kết quả
│   └─ terminal_widget.py       # Terminal
├─ model/                       # Logic nghiệp vụ
│   └─ data_model.py            # Xử lý dữ liệu
├─ presenter/                   # Điều phối
│   └─ main_presenter.py        # Presenter + Threading
└─ requirements.txt             # Thư viện
```

## Tính Năng Nổi Bật

### ✅ Multi-threading
- Xử lý file trong background thread
- UI luôn mượt mà, không bị đơ

### ✅ Real-time Progress
- Cập nhật tiến trình theo thời gian thực
- Hiển thị số file đã xử lý và phần trăm

### ✅ Modular Design
- Mỗi component là một module riêng
- Dễ dàng bảo trì và phát triển
- Tuân theo nguyên tắc Single Responsibility

### ✅ Modern UI
- Giao diện đẹp mắt, hiện đại
- Responsive design
- Color-coded messages

### ✅ Export Feature
- Xuất kết quả ra file CSV
- Dễ dàng chia sẻ và phân tích

## Troubleshooting

### Lỗi: ModuleNotFoundError: No module named 'PySide6'
**Giải pháp**: Cài đặt PySide6
```bash
pip install PySide6
```

### Lỗi: Không hiển thị kết quả
**Giải pháp**: 
- Kiểm tra file log có chứa từ khóa `mfg_data: 0x0A050000`
- Xem log ở Terminal để biết chi tiết

### Lỗi: Application không chạy
**Giải pháp**:
- Kiểm tra Python version (phải >= 3.8)
- Kiểm tra đã cài đặt requirements.txt chưa

## Phát Triển Thêm

### Thêm Tính Năng Mới

1. **Model**: Thêm logic vào `model/data_model.py`
2. **View**: Tạo widget mới trong `views/`
3. **Presenter**: Cập nhật `presenter/main_presenter.py`

### Tùy Chỉnh Giao Diện

- Màu sắc: Sửa `stylesheet` trong mỗi widget
- Layout: Điều chỉnh trong `views/main_window.py`
- Font: Thay đổi trong `main.py`

## Thông Tin Version

**Version 1.0.0**
- ✅ Dashboard UI với sidebar
- ✅ Xử lý file log ADL1
- ✅ Bộ lọc Valid/Invalid
- ✅ Export CSV
- ✅ Real-time progress
- ✅ Terminal logs
- ✅ Multi-threading

## Liên Hệ Hỗ Trợ

Nếu gặp vấn đề hoặc cần hỗ trợ, vui lòng liên hệ team phát triển.

---

**Chúc bạn sử dụng hiệu quả! 🎉**

