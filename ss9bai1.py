delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]
#thêm đơn hàng
delivery_orders.append("GE004")
delivery_orders.insert(0, "GE000")
delivery_orders[2] = "GE002-UPDATED"
delivery_orders.remove("GE003-CANCEL")
#lấy đơn hàng cuối cùng
transferred_order = delivery_orders.pop(0)
print(f"Danh sách đơn hàng còn lại: {delivery_orders} ")
print(f"Đơn hàng được bàn giao: {transferred_order}")