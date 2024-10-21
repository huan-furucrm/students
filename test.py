import requests
from bs4 import BeautifulSoup

# Bước 1: Lấy nội dung trang web
url = 'https://www.pnj.com.vn/blog/gia-vang'  # Thay bằng URL của trang bạn muốn lấy dữ liệu
response = requests.get(url)

# Bước 2: Phân tích nội dung HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Bước 3: Tìm thẻ div có class là 'bang-gia-vang-outer'
div_container = soup.find('div', class_='bang-gia-vang-outer')

# Bước 4: Tìm bảng (table) bên trong thẻ div đó
if div_container:
    table = div_container.find('table')
    
    # Bước 5: Trích xuất nội dung của bảng nếu có
    if table:
        # Lấy tất cả các hàng (tr) trong bảng
        rows = table.find_all('tr')
        
        for row in rows:
            # Lấy tất cả các ô (td) trong mỗi hàng
            cols = row.find_all('td')
            # Trích xuất nội dung text của các ô
            cols = [col.text.strip() for col in cols]
            print(cols)
    else:
        print("Không tìm thấy bảng trong thẻ div.")
else:
    print("Không tìm thấy thẻ div với class 'bang-gia-vang-outer'.")
