# 1. Phân tích Input / Output
# Input:
# - Lựa chọn menu
# - Mã đơn hàng cần thêm
# - Mã đơn hàng cần xóa
# Output:
# - Danh sách đơn hàng hiện tại
# - Thông báo thêm/xóa thành công
# - Thông báo lỗi nếu dữ liệu không hợp lệ
# 2. Đề xuất giải pháp
# - Dùng while True để tạo menu lặp liên tục
# - Dùng match-case để xử lý menu
# - Dùng strip() để xóa khoảng trắng
# - Dùng upper() để chuẩn hóa mã đơn hàng
# - Dùng append() để thêm đơn hàng
# - Dùng remove() để xóa đơn hàng
# - Dùng isdigit() để kiểm tra menu hợp lệ
# 3. Thiết kế thuật toán (Pseudocode)
# B1: Khởi tạo danh sách đơn hàng
# B2: Hiển thị menu
# B3: Người dùng nhập lựa chọn
# Nếu chọn 1:
# -> Hiển thị danh sách đơn hàng
# Nếu chọn 2:
#   -> Nhập mã đơn hàng mới
#   -> Chuẩn hóa dữ liệu
#   -> Thêm vào danh sách
# Nếu chọn 3:
#     -> Nhập mã đơn hàng cần xóa
#     -> Kiểm tra tồn tại
#     -> Nếu có -> xóa
#     -> Nếu không -> báo lỗi
# Nếu chọn 4:
#     -> Thoát chương trình
# Nếu nhập sai:
#     -> Báo lỗi và nhập lại

# TRIỂN KHAI SOURCE CODE
order_list = ["GE001", "GE002", "GE003"]
choice = 1
while choice != 4:
    choice = input("""
===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Thêm đơn hàng mới
3. Xóa đơn hàng theo mã
4. Thoát chương trình

Nhập lựa chọn: 
                       """)
    match choice:
        case "1":
            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống. ")
            else: 
                for i, order in enumerate():
                   print(f"{i+1}. {order}")
        case "2":
            new_order = input("Nhập mã đơn hàng mới: ")
            new_order = new_order.upper().strip()
            order_list.append(new_order)
        case "3":
            remove_order = input("Nhập mã cần xóa: ").strip().upper()
            if remove_order in order_list:
                order_list.remove(remove_order)
                print("Xóa thành công! ")
            else:
                print("Không tìm thấy mã đơn hàng!")
       
        case "4":
            print("Thoát chương trình")
            
        case _:
            print("Lựa chọn không hợp lệ")
    