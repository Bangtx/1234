from django.shortcuts import render
from django.http import *
from .models import *
from .my_function import *

# Create your views here.


class myweb:

    def __init__(self):
        self.all_category = category.objects.all()
        self.all_product = list(product.objects.all())
        self.all_category_name = [cate.category_name for cate in self.all_category]
        self.all_product_name = [prod.product_name for prod in self.all_product]
        for i in list_category_must_insert:
            if not is_exists(i['category_name'], self.all_category_name):
                cate = category(**i)
                cate.save()
        self.all_category = list(category.objects.all())
        self.all_product = list(product.objects.all())
        self.all_category_mom = get_category_mom(self.all_category)
        self.context = {
            'all_category': self.all_category,
            'all_category_mom': self.all_category_mom,
        }
        # self.all_category_mom = get_category_mom(self.all_category)
        # self.all_category_child = get_category_child_of_mom(self.all_category_mom, self.all_category)

    def test(self, r):
            return HttpResponse(self.all_category)

    def index(self, r):
        return render(request=r, template_name='home.html', context=self.context)

    def product(self, r, id):
        product_show = list()
        for i in self.all_product:
            if int(i.category_id) == int(id):
                product_show.append(i)
        self.context['all_product'] = product_show
        return render(request=r, template_name='products.html', context=self.context)

    def product_details(self, r, id):
        product_detail = None
        for i in self.all_product:
            if int(i.id) == int(id):
                product_detail = i
        self.context['product_detail'] = product_detail

        print(product_detail)
        return render(request=r, template_name='productDetails.html', context=self.context)

    def insert_category_if_not_exit(self):
        self.all_category = category.objects.all()
        self.all_product = product.objects.all()
        self.all_category_name = [cate.category_name for cate in self.all_category]
        self.all_product_name = [prod.product_name for prod in self.all_product]


list_category_must_insert = [
    {'id': 1, 'category_name': 'Trang trí bên trong', 'id_mom': -1},
    {'id': 2, 'category_name': 'Thảm các loại', 'id_mom': 1},
    {'id': 3, 'category_name': 'Cằm bảo hiểm', 'id_mom': 1},
    {'id': 4, 'category_name': 'Khay hộp các loại', 'id_mom': 1},
    {'id': 5, 'category_name': 'Tựa lưng gối đầu', 'id_mom': 1},
    {'id': 6, 'category_name': 'Phụ kiện điện thoại', 'id_mom': 1},
    {'id': 7, 'category_name': 'Phụ kiện để chân', 'id_mom': 1},
    {'id': 8, 'category_name': 'Khánh và Tinh dầu treo', 'id_mom': 1},
    {'id': 9, 'category_name': 'Tượng và Trang trí', 'id_mom': 1},
    {'id': 10, 'category_name': 'Nước hoa', 'id_mom': 1},
    {'id': 11, 'category_name': 'Móc khóa bao da', 'id_mom': 1},
    {'id': 12, 'category_name': 'Máy lọc không khí', 'id_mom': 1},
    {'id': 13, 'category_name': 'Chắn nắng', 'id_mom': 1},
    {'id': 14, 'category_name': 'Bọc vô lăng', 'id_mom': 1},

    {'id': 15, 'category_name': 'Đồ điện công nghệ', 'id_mom': -1},
    {'id': 16, 'category_name': 'Đồ điện khác', 'id_mom': 15},
    {'id': 17, 'category_name': 'Camera', 'id_mom': 15},
    {'id': 18, 'category_name': 'Báo lùi', 'id_mom': 15},

    {'id': 19, 'category_name': 'Trang trí bên ngoài', 'id_mom': -1},
    {'id': 20, 'category_name': 'Chuột khiển còi', 'id_mom': 19},
    {'id': 21, 'category_name': 'Phụ kiên gương xe', 'id_mom': 19},
    {'id': 22, 'category_name': 'Bạt phủ xe và Gạt mưa', 'id_mom': 19},
    {'id': 23, 'category_name': 'Đồ dán trang trí', 'id_mom': 19},
    {'id': 24, 'category_name': 'Bơm và Dây câu', 'id_mom': 19},

    {'id': 25, 'category_name': 'Sản phẩm chăm sóc', 'id_mom': -1},
    {'id': 26, 'category_name': 'Dán và Khăn lau xe', 'id_mom': 25},
    {'id': 27, 'category_name': 'Dung dịch', 'id_mom': 25},

    {'id': 28, 'category_name': 'Phụ tùng đồ lọc', 'id_mom': -1},
    {'id': 29, 'category_name': 'Motor bơm xăng', 'id_mom': 28},
    {'id': 30, 'category_name': 'Lọc gió', 'id_mom': 28},
    {'id': 31, 'category_name': 'Lọc dầu', 'id_mom': 28},
    {'id': 32, 'category_name': 'Lọc xăng', 'id_mom': 28},
    {'id': 33, 'category_name': 'Lọc điều hòa', 'id_mom': 28},

    {'id': 34, 'category_name': 'Phụ tùng máy gầm', 'id_mom': -1},
    {'id': 35, 'category_name': 'Cao su các loại', 'id_mom': 34},
    {'id': 36, 'category_name': 'Dây các loại', 'id_mom': 34},
    {'id': 37, 'category_name': 'Tụi lái van hằng nhiệt Xupap', 'id_mom': 34},
    {'id': 38, 'category_name': 'Giảm sóc, ROTUYH', 'id_mom': 35},
]
