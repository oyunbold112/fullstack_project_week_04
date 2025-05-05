from collections import Counter
def calculate_basic_stats(data_list, field=None):
    """
    Өгөгдсөн жагсаалтын үндсэн статистикийг тооцоолно.
    Аргументууд:
    data_list: Тооцоолох өгөгдлийн жагсаалт (толь бичгүүдийн жагсаалт
    эсвэл тоонуудын жагсаалт)
    field: Хэрэв data_list нь толь бичгүүдийн жагсаалт бол, аль
    талбарыг тооцоолохыг заана
    Буцаах утга:
    Статистик мэдээллийг агуулсан толь бичиг (дундаж, медиан, хамгийн
    их, хамгийн бага, нийт тоо)
    """
    try: 
        if field == None:
            data_list = sorted(data_list) 
            return {'mean': sum(data_list) / len(data_list), 'median': data_list[len(data_list) // 2], 'min': min(data_list), 'max': max(data_list), 'count': len(data_list)}
        field_list = []
        for i in data_list:
            # herwee talbariin nertei key bhgu bol nemehgui
            if field not in i.keys():
                continue
            if type(i[field]) == int or type(i[field]) == float:
                field_list.append(i[field])
            else:
                raise KeyError
            
        print(field_list)
        field_list = sorted(field_list)
        return  {'mean': sum(field_list) / len(field_list), 'median': field_list[len(field_list) // 2], 'min': min(field_list), 'max': max(field_list), 'count': len(field_list)}
    except KeyError:
        print("Talbariin utguud too bish baina")
        return "Talbariin utguud too bish baina"
    except Exception as e:
        return str(e)

#. Давтамж тооцоолох фунĸц

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
        if field == "":
            field = None
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
    
def filter_data(data_list, criteria):
    """
    Өгөгдсөн шалгуураар өгөгдлийг шүүнэ.
    Аргументууд:
    data_list: Шүүх өгөгдлийн жагсаалт (толь бичгүүдийн жагсаалт)
    criteria: Шүүлтийн шалгууруудыг агуулсан толь бичиг
    Жишээ: {"age_min": 20, "major": "Computer Science"}
    Буцаах утга:
    Шалгуурт тохирох өгөгдлийн жагсаалт
    """
    try:
        filtered_list = []
        for i in data_list:
            if i["age"] >= criteria["age_min"] and i["major"] == criteria["major"]:
                filtered_list.append(i)
        return filtered_list
    except Exception as e:
        print("Aldaa garlaa!")
def sort_data(data_list, key, reverse=False):
    """
    Өгөгдсөн түлхүүрээр өгөгдлийг эрэмбэлнэ.
    Аргументууд:
    data_list: Эрэмбэлэх өгөгдлийн жагсаалт (толь бичгүүдийн жагсаалт)
    key: Эрэмбэлэх талбарын нэр
    reverse: Буцаагаар эрэмбэлэх эсэх (үндсэн дээшээ эрэмбэлэлт)
    Буцаах утга:
    Эрэмбэлэгдсэн өгөгдлийн жагсаалт
    """
    try:
        sorted_list = sorted(data_list, key=lambda x: x[key], reverse=reverse)
        return sorted_list
    except Exception as e:
        pass

#. Өгөгдөл бүлэглэх фунĸц

def group_data(data_list, key):
    """
    Өгөгдсөн түлхүүрээр өгөгдлийг бүлэглэнэ.
    Аргументууд:
    data_list: Бүлэглэх өгөгдлийн жагсаалт (толь бичгүүдийн жагсаалт)
    key: Бүлэглэх талбарын нэр
    Буцаах утга:
    Бүлэглэсэн өгөгдлийг агуулсан толь бичиг, түлхүүр нь бүлгийн нэр,
    утга нь тухайн бүлэгт хамаарах өгөгдлийн жагсаалт
    """
    try:
        grouped_data = {}
        for item in data_list:
            if item[key] in grouped_data:
                grouped_data[item[key]].append(item)
            else:
                grouped_data[item[key]] = [item]
        return grouped_data
    except Exception as e:
        pass

#  Давхардсан утгуудыг олох фунĸц
def find_duplicates(data_list, key=None):
    """
    Өгөгдсөн жагсаалтаас давхардсан утгуудыг олно.
    Аргументууд:
    data_list: Шалгах өгөгдлийн жагсаалт
    key: Хэрэв data_list нь толь бичгүүдийн жагсаалт бол, аль талбарыг
    шалгахыг заана
    Буцаах утга:
    Давхардсан утгуудын олонлог
    """
    try:
        if key == None:
            return set([x for x in data_list if data_list.count(x) > 1])
        key_list = []
        for i in data_list:
            key_list.append(i[key])
        return set([x for x in key_list if key_list.count(x) > 1])
    except Exception as e:
        pass

#. Өгөгдлийн олонлогуудыг харьцуулах фунĸц

def compare_datasets(dataset1, dataset2, key=None):
    """
    Хоёр өгөгдлийн олонлогийг харьцуулна.
    Аргументууд:
    dataset1: Эхний өгөгдлийн олонлог
    dataset2: Хоёр дахь өгөгдлийн олонлог
    key: Хэрэв олонлогууд нь толь бичгүүдийн жагсаалт бол, аль
    талбарыг харьцуулахыг заана
    Буцаах утга:
    Харьцуулалтын үр дүнг агуулсан толь бичиг (нийтлэг, зөвхөн
    dataset1-д байгаа, зөвхөн dataset2-т байгаа)
    """
    try:
        if key == None:
            return {
                "common": set(dataset1).intersection(set(dataset2)),
                "only_in_first": set(dataset1).difference(set(dataset2)),
                "only_in_second": set(dataset2).difference(set(dataset1))
            }
        key_list1 = []
        key_list2 = []
        for i in dataset1:
            key_list1.append(i[key])
        for i in dataset2:
            key_list2.append(i[key])
        return {
            "common": set(key_list1).intersection(set(key_list2)),
            "only_in_first": set(key_list1).difference(set(key_list2)),
            "only_in_second": set(key_list2).difference(set(key_list1))
        }
    except Exception as e:
        pass

if __name__ == "__main__":
        # Жишээ ашиглалт:
    # Оюутнуудын насны статистик
    students = [
    {"id": "S001", "name": "Болд", "age": 20},
    {"id": "S002", "name": "Сараа", "age": 22},
    {"id": "S003", "name": "Батаа", "age": 19}
    ]
    age_stats = calculate_basic_stats(students, "age")
    print(age_stats) # {'mean': 20.33, 'median': 20, 'min': 19, 'max': 22,'count': 3}
    # Шууд тоонуудын жагсаалтын статистик
    numbers = [12, 45, 23, 67, 34, 19]
    num_stats = calculate_basic_stats(numbers)
    print(num_stats) # {'mean': 33.33, 'median': 28.5, 'min': 12, 'max': 67,'count': 6} 
    # Жишээ ашиглалт:
    # Оюутнуудын мэргэжлийн давтамж
    students = [
    {"id": "S001", "name": "Болд", "major": "Computer Science"},
    {"id": "S002", "name": "Сараа", "major": "Mathematics"},
    {"id": "S003", "name": "Батаа", "major": "Computer Science"}
    ]
    major_freq = calculate_frequency(students, "major")
    print(major_freq) # {'Computer Science': 2, 'Mathematics': 1}
    # Тоонуудын давтамж
    numbers = [1, 2, 3, 2, 1, 4, 5, 2, 3]

    #project_instructions_mn.md 2025-04-22
    num_freq = calculate_frequency(numbers)
    print(num_freq) # {1: 2, 2: 3, 3: 2, 4: 1, 5: 1}
    # . Өгөгдөл шүүх фунĸц
    # Жишээ ашиглалт:
    # Хоёр ангийн оюутнуудын мэргэжлүүдийг харьцуулах
    class_a = [{"id": "S001", "name": "Болд", "major": "Computer Science"},
    {"id": "S002", "name": "Сараа", "major": "Mathematics"}
    ]
    class_b = [
    {"id": "S003", "name": "Батаа", "major": "Computer Science"},
    {"id": "S004", "name": "Дорж", "major": "Physics"}
    ]
    comparison = compare_datasets(class_a, class_b, "major")
    print(comparison)
    # 'common': {'Computer Science'},
    # 'only_in_first': {'Mathematics'},
    # 'only_in_second': {'Physics'}
    # }
    # Жишээ ашиглалт:
    # Давхардсан мэргэжлүүдийг олох
    students = [
    {"id": "S001", "name": "Болд", "major": "Computer Science"},
    {"id": "S002", "name": "Сараа", "major": "Mathematics"},
    {"id": "S003", "name": "Батаа", "major": "Computer Science"}
    ]
    duplicate_majors = find_duplicates(students, "major")
    print(duplicate_majors) # {'Computer Science'}
    # Давхардсан тоонуудыг олох
    numbers = [1, 2, 3, 2, 1, 4, 5, 2, 3]
    duplicate_nums = find_duplicates(numbers)
    print(duplicate_nums) # {1, 2, 3}
    #project_instructions_mn.md 2025-04-22
    # Жишээ ашиглалт:
    # Оюутнуудыг насаар нь эрэмбэлэх
    students = [
    {"id": "S001", "name": "Болд", "age": 20},
    {"id": "S002", "name": "Сараа", "age": 22},
    {"id": "S003", "name": "Батаа", "age": 19}
    ]
    sorted_by_age = sort_data(students, "age")
    print(sorted_by_age) # [{"id": "S003", ...}, {"id": "S001", ...}, {"id":"S002", ...}]
    # Оюутнуудыг насаар нь буцаагаар эрэмбэлэх
    sorted_by_age_desc = sort_data(students, "age", reverse=True)
    print(sorted_by_age_desc) # [{"id": "S002", ...}, {"id": "S001", ...},{"id": "S003", ...}]
    # Жишээ ашиглалт:
    # Оюутнуудыг мэргэжлээр нь бүлэглэх
    students = [
    {"id": "S001", "name": "Болд", "major": "Computer Science"},
    {"id": "S002", "name": "Сараа", "major": "Mathematics"},
    {"id": "S003", "name": "Батаа", "major": "Computer Science"}
    ]
    grouped = group_data(students, "major")
    print(grouped)
    # {
    # 'Computer Science': [{"id": "S001", ...}, {"id": "S003", ...}],
    # 'Mathematics': [{"id": "S002", ...}]
    # }
    # Жишээ ашиглалт:
    # 20-с дээш настай компьютерийн ухааны оюутнуудыг шүүх
    students = [{"id": "S001", "name": "Болд", "age": 20, "major": "Computer Science"},{"id": "S002", "name": "Сараа", "age": 22, "major": "Mathematics"},{"id": "S003", "name": "Батаа", "age": 19, "major": "Computer Science"}
    ]
    filtered = filter_data(students, {"age_min": 20, "major": "Computer Science"})
    print(filtered) # [{"id": "S001", "name": "Болд", "age": 20, "major":"Computer Science"}]

    #. Өгөгдөл эрэмбэлэх фунĸц
