items_db = {"S001": {'id': 'S001', 'name': 'Болд', 'age': 20, 'grade': 'A','major': 'Computer Science'}, "S002":{'id': 'S002', 'name': 'Намуун', 'age': 21, 'grade': 'C','major': 'Mathe'}, "S003": {'id': 'S001', 'name': 'Дорж', 'age': 19, 'grade': 'B','major': 'Chemistry'}, "S004": {'id': 'S001', 'name': 'Bilgee', 'age': 18, 'grade': 'A','major': 'Physics'}, "P001": {'id': 'P001', 'name': 'Ноутбук', 'price': 1200000,'brand': 'Dell', 'in_stock': True}, "P002": {'id': 'P002', 'name': 'phone', 'price': 5000000, 'brand': 'Apple', 'in_stock': True}, "P003": {'id': 'P003', 'name': 'TV', 'price': 10000000, 'brand': 'Samsung', 'in_stock': False}}
id_list = []
ALLOED_FIELDS = ('name', 'age', 'grade', 'major', 'price', 'brand', 'in_stocks')
REQUIRED_FIELDS = ('id', 'name')

# Zuil nemeh
def add_item(item_id, **properties):
    """
    Шинэ зүйл нэмэх.
    Аргументууд:
    item_id: Зүйлийн дахин давтагдашгүй ID
    name: Зүйлийн нэр
    **properties: Нэмэлт шинж чанарууд (түлхүүр-утга хослолууд)
    Буцаах утга:
    Нэмэгдсэн зүйлийн мэдээллийг агуулсан толь бичиг
    Алдаа:
    ValueError: Хэрэв ID давхардвал эсвэл шаардлагатай талбарууд дутуу
    байвал
    """
    try:
        if item_id in id_list:
            raise ValueError("Id dawhatssan baina!")
        id_list.append(item_id)
        items_db[item_id] = {"id": item_id, **properties}
        return items_db[item_id]
    except ValueError:
        print("Id dawhatsaj baina")
    except TypeError:
        print("Shaardlagatai talbaruud dutuu baina!")
    except Exception as e:
        print("Aldaa garlaa!")

for i in items_db:
    add_item(i, **items_db[i])
# Zuil shinechleh
def update_item(item_id, field, value):
    """
    """
    try:
        if item_id not in id_list:
            raise AttributeError("error")
        items_db[item_id][field] = value
        return True
    except AttributeError:
        print("Id oldsongui!")
        return False
    except ValueError:
        print("Talbariin ner buruu baina")
        return False

# Zuil ustgah
def remove_item(item_id):
    """
    Зүйлийг ID-гаар устгах.
    Аргументууд:
    item_id: Устгах зүйлийн ID
    Буцаах утга:
    True хэрэв амжилттай устгасан бол, False хэрэв зүйл олдоогүй бол
    """
    try:
        if item_id not in id_list:
            raise ValueError
        id_list.remove(item_id)
        del items_db[item_id]
        return True
    except ValueError:
        return False
    except Exception as e:
        print("Aldaa garlaa!")

def search_items(criteria):
    """
    Өгөгдсөн шалгуураар зүйлсийг хайх.
    Аргументууд:
    criteria: Хайх шалгууруудыг агуулсан толь бичиг
    Буцаах утга:
    Шалгуурт тохирох зүйлсийн жагсаалт
    """
    content = []
    try:
        for i in items_db:
            if i[criteria.keys[0]] == criteria[criteria.keys[0]]:
                content.append
        return content
    except Exception as e:
        print("Shalguurt niitseh zuil òldsongui!")

def get_all_items():
    return list(items_db.values())

def calculate_statistics(field=None):
    study_object = []
    try:
        if field == None:
            raise ValueError("aldaa!")
        for i in items_db:
            study_object.append(items_db[i][field])
        return {'min': min(study_object), 'max': max(study_object), 'average': sum(study_object) / len(study_object), 'count': len(study_object)}
    except ValueError:
        student = 0
        product = 0
        for i in items_db:
            if 'S' in items_db[i]['id']:
                student+=1
            if 'P' in items_db[i]['id']:
                student+=1
        return {'total_items': len(items_db), 'categories': {'student': student, 'product': product}}
    except KeyError:
        print("Talbariin aguulsan zuil oldsongui!")
    
if __name__ == "__main__":
        # Жишээ ашиглалт:
    # Насны статистик
    age_stats = calculate_statistics("age")
    print(age_stats) # {'min': 18, 'max': 25, 'average': 21.5, 'count': 10}
    # Ерөнхий статистик
    general_stats = calculate_statistics()
    print(general_stats) # {'total_items': 15, 'categories': {'students': 10,'products': 5}}
    # Жишээ ашиглалт:
    # Бүх зүйлсийг авах
    all_items = get_all_items()
    print(f"Нийт зүйлсийн тоо: {len(all_items)}")
    for item in all_items:
        print(f"ID: {item['id']}, Нэр: {item['name']}")
    print(items_db)
    # Жишээ ашиглалт:
    # Оюутны мэдээллийг устгах
    success = remove_item("S001")
    print(success) # True
    # Устгагдсан зүйлийг дахин устгах оролдлого
    success = remove_item("S001")
    print(success) # False
    # Жишээ ашиглалт:
    # Оюутны насыг шинэчлэх
    success = update_item("S001", "age", 21)
    print(success) # True
    # Бүтээгдэхүүний үнийг шинэчлэх
    success = update_item("P001", "price", 1300000)
    print(success) # True
    # Байхгүй зүйлийг шинэчлэх оролдлого
    success = update_item("X999", "name", "Байхгүй зүйл")
    print(success) # False
    # Жишээ ашиглалт:
    # Оюутны мэдээлэл нэмэх
    student = add_item("S001", "Болд", age=20, grade="A", major="ComputerScience")
    print(student) # {'id': 'S001', 'name': 'Болд', 'age': 20, 'grade': 'A','major': 'Computer Science'}
    # Бүтээгдэхүүний мэдээлэл нэмэх
    product = add_item("P001", "Ноутбук", price=1200000, brand="Dell",
    in_stock=True)
    print(product) # {'id': 'P001', 'name': 'Ноутбук', 'price': 1200000,'brand': 'Dell', 'in_stock': True}