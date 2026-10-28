# Cờ Vua — Royal Clash

Game cờ vua chạy bằng Streamlit.

## Tính năng
- Trang bắt đầu và chọn chế độ: chơi với AI hoặc hai người chơi.
- Bấm vào quân cờ để xem các nước đi hợp lệ; ô đi được đánh dấu, ô có thể ăn quân được viền xanh.
- Không cho thực hiện nước đi sai luật; quân bị ăn sẽ biến mất khỏi bàn cờ.
- AI có 3 mức: Dễ, Trung bình, Khó.
- Nhạc nền bật/tắt và âm báo khi di chuyển/ăn quân.
- Lịch sử nước đi, đi lại, chơi lại và đổi góc nhìn bàn cờ.

## Chạy trên Streamlit Community Cloud
1. Tải các file `app.py`, `requirements.txt`, `README.md` lên repository GitHub.
2. Trên Streamlit Community Cloud, tạo app từ repository đó, nhánh `main`, file chính `app.py`.
3. Nhấn Deploy.

Nhạc được tạo trực tiếp bằng Web Audio API, không cần tải thêm file nhạc. Khi vào ván, nhấn **Bật nhạc** để trình duyệt cho phép phát âm thanh.
