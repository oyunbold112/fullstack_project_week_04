import data_collector as dc
import data_analyzer as da

def display_menu():
    """
    Үндсэн цэсийг харуулна.
    Буцаах утга:
    None
    """
    print("\n===== Өгөгдөл Боловсруулах Хэрэгсэл =====")
    print("1. Өгөгдөл нэмэх")
    print("2. Өгөгдөл шинэчлэх")
    print("3. Өгөгдөл устгах")
    #project_instructions_mn.md 2025-04-22
    print("4. Өгөгдөл харах")
    print("5. Дүн шинжилгээ хийх")
    print("6. Тусламж")
    print("0. Гарах")
    print("=====================================")
# Хэрэглэгчийн оролт авах фунĸц
def get_user_input(prompt, input_type=str):
    """
    Хэрэглэгчээс оролт авч, тохирох төрөлд хөрвүүлнэ.
    Аргументууд:
    prompt: Хэрэглэгчид харуулах текст
    input_type: Оролтын төрөл (str, int, float гэх мэт)
    Буцаах утга:
    Хэрэглэгчийн оролт (input_type төрөлд хөрвүүлсэн)
    """
    while True:
        try:
            user_input = input(prompt)
            return input_type(user_input)
        except ValueError:
            print(f"Алдаа: {input_type.__name__} төрлийн утга оруулна уу.")
# Өгөгдөл нэмэх цэсийн фунĸц

def add_data_menu():
    """
    Өгөгдөл нэмэх цэсийг харуулж, хэрэглэгчийн оролтыг боловсруулна.
    Буцаах утга:
    None
    """
    print("\n----- Өгөгдөл нэмэх -----")
    print("1. Оюутан нэмэх")
    print("2. Бүтээгдэхүүн нэмэх")
    print("3. Буцах")
    # project_instructions_mn.md 2025-04-22
    choice = get_user_input("Сонголт: ", int)
    if choice == 1:
    # Оюутан нэмэх
        student_id = get_user_input("Оюутны ID: ")
        name = get_user_input("Нэр: ")
        age = get_user_input("Нас: ", int)
        major = get_user_input("Мэргэжил: ")
        student = dc.add_item(student_id, name=name, age=age, major=major)
        print(f"Оюутан амжилттай нэмэгдлээ: {student}")
    elif choice == 2:
        # Бүтээгдэхүүн нэмэх
        product_id = get_user_input("Бүтээгдэхүүний ID: ")
        name = get_user_input("Нэр: ")
        price = get_user_input("Үнэ: ", float)
        brand = get_user_input("Брэнд: ")
        product = dc.add_item(product_id, name=name, price=price, brand=brand)
        print(f"Бүтээгдэхүүн амжилттай нэмэгдлээ: {product}")
    elif choice == 3:
        pass
    else:
        print("Буруу сонголт. Дахин оролдоно уу.")

# Дүн шинжилгээ хийх цэсийн фунĸц
def analysis_menu():
    """
    Дүн шинжилгээ хийх цэсийг харуулж, хэрэглэгчийн оролтыг боловсруулна.
    Буцаах утга:
    None
    """
    print("\n----- Дүн шинжилгээ хийх -----")
    print("1. Үндсэн статистик харах")
    print("2. Давтамжийн дүн шинжилгээ")
    print("3. Өгөгдөл эрэмбэлэх")
    print("4. Өгөгдөл шүүх")
    print("5. Буцах")
    choice = get_user_input("Сонголт: ", int)
    if choice == 1:
    # Үндсэн статистик харах
    # project_instructions_mn.md 2025-04-22
        try:
            field = get_user_input("Талбарын нэр (хоосон орхиж болно): ")
            if not field:
                field = None
            items = dc.get_all_items()
            stats = da.calculate_basic_stats(items, field)
            print("\n----- Статистик мэдээлэл -----")
            for key, value in stats.items():
                print(f"{key}: {value}")
        except AttributeError:
            pass
    elif choice == 2:
        # Давтамжийн дүн шинжилгээ
        items = dc.get_all_items()
        field = get_user_input("Талбарын нэр: ")
        freq = da.calculate_frequency(items, field)
        print(f"\n----- {field} талбарын давтамж -----")
        for value, count in sorted(freq.items(), key=lambda x: x[1],
            reverse=True):
            print(f"{value}: {count}")
    elif choice == 3:
        # Өгөгдөл эрэмбэлэх
        field = get_user_input("Эрэмбэлэх талбарын нэр: ")
        reverse_input = get_user_input("Буцаагаар эрэмбэлэх үү? (y/n): ")
        reverse = reverse_input.lower() == 'y'
        items = dc.get_all_items()
        sorted_items = da.sort_data(items, field, reverse)
        print(f"\n----- {field} талбараар эрэмбэлсэн өгөгдөл -----")
        for item in sorted_items:
            print(item)
    elif choice == 4:
        # Өгөгдөл шүүх
        print("Шүүлтийн шалгуурууд (хоосон орхивол алгасна):")
        criteria = {}
        field = get_user_input("Талбарын нэр: ")
        if field:
            value = get_user_input(f"{field} талбарын утга: ")
            criteria[field] = value
            min_field = get_user_input("Хамгийн бага утгатай талбар (хоосон орхиж болно): ")
        if min_field:
            min_value = get_user_input(f"{min_field}_min утга: ", float)
            criteria[f"{min_field}_min"] = min_value
            max_field = get_user_input("Хамгийн их утгатай талбар (хоосон орхиж болно): ")
        if max_field:
            max_value = get_user_input(f"{max_field}_max утга: ", float)
            criteria[f"{max_field}_max"] = max_value
        
        items = dc.get_all_items()
        filtered_items = da.filter_data(items, criteria)
        print(f"\n----- Шүүсэн өгөгдөл ({len(filtered_items)} зүйл) -----")
        for item in filtered_items:
            print(item)
    elif choice == 5:
        return
    else:
        print("Буруу сонголт. Дахин оролдоно уу.")
        
# Үндсэн програмын фунĸц

def main():
    """
    Үндсэн програмын гүйцэтгэл.
    Буцаах утга:
    None
    """
    # Нэр авах
    name = get_user_input("Нэр: ")
    print(f"Сайн байна уу, {name}!")
    # Нас авах
    age = get_user_input("Нас: ", int)
    print(f"Таны нас: {age}")
    print("Өгөгдөл Цуглуулах ба Дүн Шинжилгээний Хэрэгсэл")
    print("Хөгжүүлсэн: Оюунболд")
    while True:
        display_menu()
        choice = get_user_input("Сонголт: ", int)
        if choice == 0:
            print("Програмаас гарч байна...")
            break
        elif choice == 1:
            add_data_menu()
        elif choice == 2:
            item_id = get_user_input("Өгөгдөл ID: ")
            field = get_user_input("Талбарын нэр: ")
            value = get_user_input("Шинэ утга: ")
            print(dc.update_item(item_id, field, value))
        elif choice == 3:
            item_id = get_user_input("Өгөгдөл ID: ")
            print(dc.remove_item(item_id))
        elif choice == 4:
            data_list = dc.get_all_items()
            for item in data_list:
                print(item)
        elif choice == 5:
            analysis_menu()
        elif choice == 6:
            display_menu()
        else:
            print("Буруу сонголт. Дахин оролдоно уу.")
if __name__ == "__main__":
    main()