import json

class EmployeeContract:
    def __init__(self, employee_id, name, position, start_date):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.start_date = start_date

def load_contracts():
    try:
        with open('contracts.json', 'r') as file:
            data = json.load(file)
            return [EmployeeContract(**item) for item in data]
    except FileNotFoundError:
        return []

def save_contracts(contracts):
    contracts_data = [
        {'employee_id': c.employee_id,
         'name': c.name,
         'position': c.position,
         'start_date': c.start_date}
        for c in contracts
    ]
    with open('contracts.json', 'w') as file:
        json.dump(contracts_data, file, indent=4)

def add_new_contract(contracts):
    print("Введите данные нового договора:")
    employee_id = input("ID сотрудника: ")
    name = input("ФИО сотрудника: ")
    position = input("Должность: ")
    start_date = input("Дата начала контракта (ДД.ММ.ГГГГ): ")
    new_contract = EmployeeContract(employee_id, name, position, start_date)
    contracts.append(new_contract)
    save_contracts(contracts)
    print(f"Договор № {employee_id} успешно добавлен.")

def show_all_contracts(contracts):
    if not contracts:
        print("Нет зарегистрированных контрактов.")
    else:
        print("\nСписок текущих договоров:\n")
        for contract in contracts:
            print(f"ID сотрудника: {contract.employee_id}, ФИО: {contract.name}, Должность: {contract.position}, Дата начала: {contract.start_date}")

def edit_contract(contracts):
    target_id = input("Введите ID сотрудника, чей контракт хотите изменить: ")
    found = False
    for i, contract in enumerate(contracts):
        if contract.employee_id == target_id:
            found = True
            print(f"Текущие данные сотрудника ({target_id}):")
            print(f"ФИО: {contract.name}, Должность: {contract.position}, Дата начала: {contract.start_date}\n")
            
            # Изменяем поля договора
            new_name = input("Новое имя сотрудника (оставьте пустым, чтобы оставить прежнее значение): ").strip()
            new_position = input("Новая должность (оставьте пустым, чтобы оставить прежнюю): ").strip()
            new_start_date = input("Новая дата начала (формат ДД.ММ.ГГГГ, оставьте пустым, чтобы сохранить старую): ").strip()
        
            if new_name != "":
                contract.name = new_name
            if new_position != "":
                contract.position = new_position
            if new_start_date != "":
                contract.start_date = new_start_date
                
            save_contracts(contracts)
            print(f"Данные по сотруднику с ID {target_id} обновлены!")
    
    if not found:
        print(f"Сотрудник с таким ID не найден.")

def delete_contract(contracts):
    target_id = input("Введите ID сотрудника, чью запись удалим: ")
    removed = False
    for i, contract in enumerate(contracts):
        if contract.employee_id == target_id:
            del contracts[i]
            removed = True
            break
    if removed:
        save_contracts(contracts)
        print(f"Запись о договоре сотрудника с ID {target_id} удалена.")
    else:
        print(f"Сотрудника с указанным ID не существует.")

# Главное меню программы
def main_menu():
    while True:
        print("\nМеню управления трудовыми договорами:")
        print("1. Создать новый договор")
        print("2. Показать все действующие договоры")
        print("3. Обновить данные договора")
        print("4. Удалить договор")
        print("5. Выход\n")
        choice = input("Выберите пункт меню (1–5): ")
        
        if choice == '1':
            add_new_contract(contracts)
        elif choice == '2':
            show_all_contracts(contracts)
        elif choice == '3':
            edit_contract(contracts)
        elif choice == '4':
            delete_contract(contracts)
        elif choice == '5':
            print("Завершение работы...")
            break
        else:
            print("Ошибка! Выберите правильный пункт меню.")

if __name__ == "__main__":
    contracts = load_contracts()  # Загрузка предыдущих записей
    main_menu()