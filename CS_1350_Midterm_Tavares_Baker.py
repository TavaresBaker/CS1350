cart = {}

def add_item(item_name, price, quantity=1):
    if not isinstance(quantity, int) or quantity <= 0:
        return False
    if price <= 0:
        return False

    if item_name in cart:
        cart[item_name]["quantity"] += quantity
        cart[item_name]["price"] = price
    else:
        cart[item_name] = {"price": price, "quantity": quantity}
    return True

def calculate_total():
    if not cart:
        return 0
    return sum(item["price"] * item["quantity"] for item in cart.values())












def add_student_to_club(clubs_dict, club_name, student_name):
    if club_name not in clubs_dict:
        clubs_dict[club_name] = set()
    clubs_dict[club_name].add(student_name)

def get_students_in_multiple_clubs(clubs_dict):
    student_counts = {}
    for members in clubs_dict.values():
        for student in members:
            student_counts[student] = student_counts.get(student, 0) + 1
   
    return [student for student, count in student_counts.items() if count > 1]

def find_exclusive_members(clubs_dict, club1_name, club2_name):
    club1 = clubs_dict.get(club1_name, set())
    club2 = clubs_dict.get(club2_name, set())
   
    return club1 - club2



if __name__ == "__main__":
    clubs = {}
    add_student_to_club(clubs, "Chess", "Alice")
    add_student_to_club(clubs, "Chess", "Bob")
    add_student_to_club(clubs, "Drama", "Alice")
    add_student_to_club(clubs, "Drama", "Charlie")

    print(get_students_in_multiple_clubs(clubs))  
    print(find_exclusive_members(clubs, "Chess", "Drama"))  
    print(find_exclusive_members(clubs, "Drama", "Chess"))  













    def clean_message(message):
    return message.strip()

def expand_abbreviations(message):
    abbreviations = {
        "btw": "by the way",
        "idk": "I don't know",
        "omg": "oh my god",
        "u": "you",
        "r": "are"
    }
    words = message.split()
    expanded = [abbreviations.get(word.lower(), word) for word in words]
    return " ".join(expanded)

def count_words(message):
    return len(message.split())

def censor_numbers(message):
    import re
    return re.sub(r'\d', "*", message)


if __name__ == "__main__":
    msg1 = " Hello World 123 "
    
    cleaned = clean_message(msg1)
    expanded = expand_abbreviations(cleaned)
    word_count = count_words(expanded)
    censored = censor_numbers(expanded)
    
    print(f"Original: '{msg1}'")
    print(f"Cleaned: '{cleaned}'")
    print(f"Expanded: '{expanded}'")
    print(f"Word count: {word_count}")
    print(f"Censored numbers: '{censored}'")




















import re

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    return True

def extract_hashtags(texts):
    return re.findall(r"#\w+", texts)

def validate_time(time_string):
    return bool(re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", time_string))

def find_dates(text):
    return re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)


if __name__ == "__main__":
    passwords = ["Pass1234", "weakpass", "NoDigits!", "12345678", "GoodPass99"]
    for pwd in passwords:
        print(f"Password '{pwd}': {validate_password(pwd)}")

    sample_text = "Events: 2023-05-10, 2024-01-01. Tags: #Hi #World"
    print()
    print(f"Hashtags: {extract_hashtags(sample_text)}")
    print(f"Dates: {find_dates(sample_text)}")
    times = ["14:30", "25:00", "09:59", "23:60"]
    for t in times:
        print(f"Time '{t}' valid? {validate_time(t)}")
