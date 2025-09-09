from .masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция обработки информации о карте и о счете"""
    choice_acc = account_card.split()
    if choice_acc[0] in "Visa":
        result = f"{choice_acc[0]} {choice_acc[1]} {get_mask_card_number(int(choice_acc[-1]))}"
    elif choice_acc[0] in ["Maestro", "MasterCard"]:
        result = f"{choice_acc[0]} {get_mask_card_number(int(choice_acc[-1]))}"
    elif choice_acc[0] == "Счет":
        result = f"{choice_acc[0]} {get_mask_account(int(choice_acc[-1]))}"
    else:
        result = "Данные отсутствуют"

    return result


def get_date(date: str) -> str:
    """Функция возвращает дату из строки определенного формата"""
    new_date = date.split("-")
    result = f"{new_date[2][:2]}.{new_date[1]}.{new_date[0]}"
    return result
