# 1. Phân tích Input / Output
# Input:
# - Lựa chọn menu
# - Mã đơn hàng
# - Trạng thái đơn hàng
# - Vị trí cần sửa / xóa
# Output:
# - Danh sách đơn hàng
# - Kết quả cập nhật đơn hàng
# - Thống kê số lượng đơn hàng theo trạng thái
# - Thông báo lỗi nếu dữ liệu không hợp lệ
# 2. Đề xuất giải pháp
# - Dùng while True để tạo menu lặp
# - Dùng match-case để xử lý menu
# - Dùng strip() để xóa khoảng trắng
# - Dùng upper() để chuẩn hóa dữ liệu
# - Dùng append() để thêm đơn hàng
# - Dùng pop() để xóa đơn hàng theo vị trí
# - Dùng split("-") để tách trạng thái đơn hàng
# - Dùng isdigit() để kiểm tra dữ liệu số hợp lệ
# 3. Thiết kế thuật toán (Pseudocode)
# B1: Khởi tạo danh sách đơn hàng
# B2: Hiển thị menu chính
# Nếu chọn 1:
#    -> Hiển thị danh sách đơn hàng
# Nếu chọn 2:
#    -> Hiển thị menu cập nhật
#     Nếu chọn thêm:
#         -> Nhập mã và trạng thái
#         -> Chuẩn hóa
#         -> Thêm vào danh sách
#     Nếu chọn sửa:
#         -> Nhập vị trí
#         -> Kiểm tra hợp lệ
#         -> Cập nhật đơn hàng
#     Nếu chọn xóa:
#         -> Nhập vị trí
#         -> Kiểm tra hợp lệ
#         -> Xóa đơn hàng
# Nếu chọn 3:
#     -> Thống kê số lượng theo trạng thái
# Nếu chọn 4:
#     -> Thoát chương trình
# Nếu nhập sai:
#     -> Báo lỗi

# TRIỂN KHAI SOURCE CODE
order_list = ["GE001 - PENDING", "GE002 - DELIVERING", "GE003 - CANCELLED"]
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")
    choice = input("\nNhập lựa chọn của bạn (1-4): ").strip()
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
    match int(choice):
        case 1:
            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("\n===== DANH SÁCH ĐƠN HÀNG =====")
                for index, order in enumerate(order_list, start=1):
                    print(f"{index}. {order}")
        case 2:
            while True:
                print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
                print("1. Thêm đơn hàng mới")
                print("2. Sửa đơn hàng theo vị trí")
                print("3. Xóa đơn hàng theo vị trí")
                print("4. Quay lại menu chính")
                sub_choice = input("\nNhập lựa chọn: ").strip()
                if not sub_choice.isdigit():
                    print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
                    continue
                match int(sub_choice):
                    case 1:
                        order_code = input("Nhập mã đơn hàng: ").strip().upper()
                        order_status = input("Nhập trạng thái đơn hàng: ").strip().upper()
                        new_order = f"{order_code} - {order_status}"
                        order_list.append(new_order)
                        print("Thêm đơn hàng thành công!")
                    case 2:
                        edit_position = input("Nhập vị trí cần sửa: ").strip()
                        if not edit_position.isdigit():
                            print("Vị trí không hợp lệ!")
                            continue
                        edit_position = int(edit_position)
                        if (edit_position < 1 or edit_position > len(order_list)):
                            print("Không tồn tại đơn hàng ở vị trí này!")
                        else:
                            order_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                            order_status = input("Nhập trạng thái mới: ").strip().upper()
                            updated_order = (order_code + " - " + order_status)
                            order_list[edit_position - 1] = updated_order
                            print("Cập nhật đơn hàng thành công!")
                    case 3:
                        delete_position = input("Nhập vị trí cần xóa: ").strip()
                        if not delete_position.isdigit():
                            print("Vị trí không hợp lệ!")
                            continue
                        delete_position = int(delete_position)
                        if (delete_position < 1 or delete_position > len(order_list)):
                            print("Không tồn tại đơn hàng ở vị trí này!")
                        else:
                            removed_order = order_list.pop(delete_position - 1)
                            print("Đã xóa đơn hàng:", removed_order)
                    case 4:
                        break
                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        case 3:
            pending_count = 0
            delivering_count = 0
            completed_count = 0
            cancelled_count = 0

            for order in order_list:
                parts = order.split("-")
                status = parts[1].strip()
                if status == "PENDING":
                    pending_count += 1
                elif status == "DELIVERING":
                    delivering_count += 1
                elif status == "COMPLETED":
                    completed_count += 1
                elif status == "CANCELLED":
                    cancelled_count += 1

            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
            print("PENDING:", pending_count)
            print("DELIVERING:", delivering_count)
            print("COMPLETED:", completed_count)
            print("CANCELLED:", cancelled_count)
            print("Tổng số đơn hàng:", len(order_list))
        case 4:
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")