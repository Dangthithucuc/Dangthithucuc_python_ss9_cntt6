branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]
target_achieved = [True, True, False, True, False] #(True là Đạt chỉ tiêu, False là Không đạt)

choice = 0

while choice != 4:
    choice = input('''
===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
1. Hiển thị báo cáo doanh thu tổng hợp
2. Thống kê chi nhánh Cao nhất / Thấp nhất
3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
4. Thoát chương trình
================================================
Nhập lựa chọn của bạn (1-4): _''')
    
    if choice.isdigit() != True:
        print("Nhập số nguyên từ 1-4")
    else:
        choice = int(choice) # ép lại kiểu là int 
        match choice:
            case 1:
                total_revenue = sum(daily_revenues)
                print("--- BÁO CÁO DOANH THU TỔNG HỢP ---")
                print(f"{'Tên Cơ Sở':<30}| {'Doanh Thu':<15}| {'Trạng Thái':<10}")
                print("-" * 60)

                for i, branch in enumerate(branch_names):
                    print(f"{branch:<30}| {daily_revenues[i]:<15}| {'Đạt' if target_achieved[i] else 'Không đạt':<10}")
                
                print("-" * 60)
                print(f"=> TỔNG DOANH THU TOÀN VÙNG: {total_revenue} VND")
            case 2:
                max_revenues = max(daily_revenues)
                min_revenues = min(daily_revenues)

                max_index = daily_revenues.index(max_revenues)
                min_index = daily_revenues.index(min_revenues)

                max_branch = branch_names[max_index]
                min_branch = branch_names[min_index]
                print(f'''
---THỐNG KÊ CƠ SỞ NỔI BẬT---
-Cơ sở có doanh thu CAO NHẬT: {max_branch} ({max_revenues} VND)
-Cơ sở có doanh thu THẤP NHẤT: {min_branch} ({min_revenues} VND)''')
            case 3:
                branch_false = []

                for i, target in enumerate(target_achieved):
                    if target == False:
                        branch_false.append(branch_names[i])

                print(f'''
---DANH SÁCH CƠ SỞ CẦN HỖ TRỢ TRA CỨU ĐƯỢC---
{branch_false}''')
            case 4:
                print("Thoát chương trình")
                break
            case _:
                print("Lỗi! nhập lại")