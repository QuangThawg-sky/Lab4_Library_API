\# Library API – Thư viện số Khoa CNTT



\## 1. Giới thiệu

Dự án xây dựng Web API quản lý sách bằng FastAPI, hỗ trợ xem danh sách, tìm kiếm, phân trang, thêm, cập nhật và xóa sách.



\## 2. Công nghệ

\- Python

\- FastAPI

\- Pydantic

\- Postman



\## 3. Cài đặt và chạy

Kích hoạt môi trường ảo trên Windows:



```powershell

.\\.venv\\Scripts\\Activate.ps1

pip install -r requirements.txt

uvicorn app.main:app --reload

```



Mở tài liệu API: http://127.0.0.1:8000/docs



\## 4. Các endpoint



| Phương thức | Endpoint | Chức năng |

|---|---|---|

| GET | /health | Kiểm tra API |

| GET | /books | Danh sách, tìm kiếm và phân trang |

| GET | /books/{id} | Chi tiết sách |

| POST | /books | Thêm sách |

| PUT | /books/{id} | Cập nhật toàn bộ sách |

| PATCH | /books/{id} | Cập nhật một phần |

| DELETE | /books/{id} | Xóa sách |



\## 5. Kiểm thử bằng Postman

Mở Postman Collection trong thư mục `postman/`, đặt `baseUrl` thành `http://localhost:8000` và chạy Collection Runner.



\## 6. Ảnh minh chứng

Ảnh Swagger và kết quả Postman Runner được lưu trong thư mục `docs/` nếu đã được tạo.

