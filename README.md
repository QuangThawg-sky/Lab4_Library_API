# Library API – Thư viện số Khoa CNTT

## 1. Giới thiệu

Dự án xây dựng Web API quản lý sách bằng FastAPI, hỗ trợ xem danh sách, tìm kiếm, phân trang, thêm, cập nhật và xóa sách.

## 2. Công nghệ

- Python
- FastAPI
- Pydantic
- Postman

## 3. Cài đặt và chạy

Mở PowerShell tại thư mục dự án và kích hoạt môi trường ảo trên Windows:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Mở tài liệu API tại: http://127.0.0.1:8000/docs

## 4. Các endpoint

| Phương thức | Endpoint | Chức năng |
|---|---|---|
| GET | `/health` | Kiểm tra API |
| GET | `/books` | Danh sách, tìm kiếm và phân trang |
| GET | `/books/{id}` | Chi tiết sách |
| POST | `/books` | Thêm sách |
| PUT | `/books/{id}` | Cập nhật toàn bộ sách |
| PATCH | `/books/{id}` | Cập nhật một phần |
| DELETE | `/books/{id}` | Xóa sách |

## 5. Kiểm thử bằng Postman

1. Mở Collection `Library API` trong thư mục `postman/`.
2. Import Environment `Library-Local`.
3. Đặt `baseUrl` thành `http://localhost:8000`.
4. Khởi động API bằng Uvicorn.
5. Chạy toàn bộ 12 test case theo thứ tự từ TC01 đến TC12 bằng Collection Runner.

## 6. Ảnh minh chứng

Các ảnh minh chứng được lưu trong thư mục `docs/`:

- `swagger.png`: giao diện tài liệu API Swagger.
- `postman_runner.png`: kết quả chạy Postman Runner.
- `postman2_runner.png`: ảnh kết quả Postman Runner bổ sung.