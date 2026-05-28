# 1. PHÂN TÍCH LỖI
# Sau khi chạy: express_orders.insert(0, "GE100-FAST")
# Danh sách sẽ trở thành: ['GE100-FAST', 'GE101', 'GE102-WRONG', 'GE103-CANCEL', 'GE104']
# Vì insert(0, value) sẽ chèn phần tử vào đầu danh sách
# và đẩy các phần tử cũ sang phải 1 vị trí
# Vì sao dòng dưới sửa nhầm "GE101"?
# express_orders[1] = "GE102-UPDATED"
# Sau khi insert(), phần tử tại index 1 là "GE101", không còn là "GE102-WRONG" nữa.
# "GE102-WRONG" lúc này nằm ở index 2.
# Vì sao dòng sau xóa sai? express_orders.pop(3)
# pop(3) sẽ xóa phần tử ở index 3.
# Sau khi insert(), index 3 là "GE102-WRONG", không phải "GE103-CANCEL".
# Muốn xóa đúng đơn hàng bị hủy nên dùng:
# express_orders.remove("GE103-CANCEL")
# remove(value) xóa theo giá trị.
# Phương thức pop() không truyền index sẽ lấy phần tử cuối danh sách.
# Vì sao dòng sau lấy sai đơn hàng?
# current_order = express_orders.pop()
# Vì pop() mặc định lấy phần tử cuối, nên lấy "GE104" thay vì "GE100-FAST".
# Muốn lấy đơn hàng đầu tiên: current_order = express_orders.pop(0)

# 2.SOURCE CODE ĐÚNG
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]
express_orders.append("GE104")
express_orders.insert(0, "GE100-FAST")
express_orders[2] = "GE102-UPDATED"
express_orders.remove("GE103-CANCEL")
current_order = express_orders.pop(0)
print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)