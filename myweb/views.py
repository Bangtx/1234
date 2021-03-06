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
    {'id': 1, 'category_name': 'Trang tr?? b??n trong', 'id_mom': -1},
    {'id': 2, 'category_name': 'Th???m c??c lo???i', 'id_mom': 1},
    {'id': 3, 'category_name': 'C???m b???o hi???m', 'id_mom': 1},
    {'id': 4, 'category_name': 'Khay h???p c??c lo???i', 'id_mom': 1},
    {'id': 5, 'category_name': 'T???a l??ng g???i ?????u', 'id_mom': 1},
    {'id': 6, 'category_name': 'Ph??? ki???n ??i???n tho???i', 'id_mom': 1},
    {'id': 7, 'category_name': 'Ph??? ki???n ????? ch??n', 'id_mom': 1},
    {'id': 8, 'category_name': 'Kh??nh v?? Tinh d???u treo', 'id_mom': 1},
    {'id': 9, 'category_name': 'T?????ng v?? Trang tr??', 'id_mom': 1},
    {'id': 10, 'category_name': 'N?????c hoa', 'id_mom': 1},
    {'id': 11, 'category_name': 'M??c kh??a bao da', 'id_mom': 1},
    {'id': 12, 'category_name': 'M??y l???c kh??ng kh??', 'id_mom': 1},
    {'id': 13, 'category_name': 'Ch???n n???ng', 'id_mom': 1},
    {'id': 14, 'category_name': 'B???c v?? l??ng', 'id_mom': 1},

    {'id': 15, 'category_name': '????? ??i???n c??ng ngh???', 'id_mom': -1},
    {'id': 16, 'category_name': '????? ??i???n kh??c', 'id_mom': 15},
    {'id': 17, 'category_name': 'Camera', 'id_mom': 15},
    {'id': 18, 'category_name': 'B??o l??i', 'id_mom': 15},

    {'id': 19, 'category_name': 'Trang tr?? b??n ngo??i', 'id_mom': -1},
    {'id': 20, 'category_name': 'Chu???t khi???n c??i', 'id_mom': 19},
    {'id': 21, 'category_name': 'Ph??? ki??n g????ng xe', 'id_mom': 19},
    {'id': 22, 'category_name': 'B???t ph??? xe v?? G???t m??a', 'id_mom': 19},
    {'id': 23, 'category_name': '????? d??n trang tr??', 'id_mom': 19},
    {'id': 24, 'category_name': 'B??m v?? D??y c??u', 'id_mom': 19},

    {'id': 25, 'category_name': 'S???n ph???m ch??m s??c', 'id_mom': -1},
    {'id': 26, 'category_name': 'D??n v?? Kh??n lau xe', 'id_mom': 25},
    {'id': 27, 'category_name': 'Dung d???ch', 'id_mom': 25},

    {'id': 28, 'category_name': 'Ph??? t??ng ????? l???c', 'id_mom': -1},
    {'id': 29, 'category_name': 'Motor b??m x??ng', 'id_mom': 28},
    {'id': 30, 'category_name': 'L???c gi??', 'id_mom': 28},
    {'id': 31, 'category_name': 'L???c d???u', 'id_mom': 28},
    {'id': 32, 'category_name': 'L???c x??ng', 'id_mom': 28},
    {'id': 33, 'category_name': 'L???c ??i???u h??a', 'id_mom': 28},

    {'id': 34, 'category_name': 'Ph??? t??ng m??y g???m', 'id_mom': -1},
    {'id': 35, 'category_name': 'Cao su c??c lo???i', 'id_mom': 34},
    {'id': 36, 'category_name': 'D??y c??c lo???i', 'id_mom': 34},
    {'id': 37, 'category_name': 'T???i l??i van h???ng nhi???t Xupap', 'id_mom': 34},
    {'id': 38, 'category_name': 'Gi???m s??c, ROTUYH', 'id_mom': 35},
]
