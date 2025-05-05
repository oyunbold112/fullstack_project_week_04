from collections import Counter

def calculate_frequency(data_list, field=None):
    """
    Өгөгдсөн жагсаалтын утгуудын давтамжийг тооцоолно.
    Аргументууд:
    data_list: Тооцоолох өгөгдлийн жагсаалт
    field: Хэрэв data_list нь толь бичгүүдийн жагсаалт бол, аль
    талбарыг тооцоолохыг заана
    Буцаах утга:
    Утга бүрийн давтамжийг агуулсан толь бичиг
    """
    try:
        counter = Counter()
        
        if field is None:
            for d in data_list:
                counter.update(str(v) for v in d.values())
        else:
            for d in data_list:
                if field in d:
                    counter.update([str(d[field])])
        
        return dict(counter)
    except Exception as e:
        return str(e)

data = [
    {'id': 'S001', 'name': 'Болд', 'age': 20, 'grade': 'A', 'major': 'Computer Science'},
    {'id': 'S002', 'name': 'Намуун', 'age': 21, 'grade': 'C', 'major': 'Mathe'},
    {'id': 'S001', 'name': 'Дорж', 'age': 19, 'grade': 'B', 'major': 'Chemistry'},
    {'id': 'S001', 'name': 'Bilgee', 'age': 18, 'grade': 'A', 'major': 'Physics'},
    {'id': 'P001', 'name': 'Ноутбук', 'price': 1200000, 'brand': 'Dell', 'in_stock': True},
    {'id': 'P002', 'name': 'phone', 'price': 5000000, 'brand': 'Apple', 'in_stock': True},
    {'id': 'P003', 'name': 'TV', 'price': 10000000, 'brand': 'Samsung', 'in_stock': False}
]

print(calculate_frequency(data)) 
print(calculate_frequency(data, "id"))
