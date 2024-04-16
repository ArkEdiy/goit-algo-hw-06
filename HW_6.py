from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if value:
            super().__init__(value)
        else:
            raise ValueError("Name cannot be empty")


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Phone number must be a 10-digit number")


class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = [p for p in self.phones if str(p) != phone_number]

    def edit_phone(self, old_phone_number, new_phone_number):
        self.remove_phone(old_phone_number)
        self.add_phone(new_phone_number)

    def find_phone(self, phone_number):
        for p in self.phones:
            if str(p) == phone_number:
                return p
        return None

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    def add_record(self, record_name, phone_numbers):
        record = Record(record_name)
        for phone_number in phone_numbers:
            record.add_phone(phone_number)
        self.data[record_name] = record

    def find_records_by_name(self, name):
        return [record for record in self.data.values() if record.name.value == name]

    def delete_record_by_name(self, name):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Додавання записів
    book.add_record("John", ["1234567890", "5555555555"])
    book.add_record("Jane", ["9876543210"])

    # Виведення всіх записів у книзі
    for record in book.data.values():
        print(record)

    # Знаходження та редагування телефону для John
    john_records = book.find_records_by_name("John")
    if john_records:
        john = john_records[0]
        john.edit_phone("1234567890", "1112223333")

    # Виведення запису John після редагування
    john = book.find_records_by_name("John")
    if john:
        print(john[0])

    # Пошук конкретного телефону у записі John
    found_phone = john[0].find_phone("5555555555")
    if found_phone:
        print(f"Found phone in John's record: {found_phone}")

    # Видалення запису Jane
    book.delete_record_by_name("Jane")
