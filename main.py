def warning_time(city: str) -> int:
    warning_times = {
        'Tel-Aviv': 90,
        'Jerusalem': 120,
        'Haifa': 150,
        'Eilat': 180,
        'Ashdod': 90,
        'Ashkelon': 90,
        'Beersheba': 90,
        'Hadera': 90,
        'Herzliya': 90,
        'Netanya': 90,
        'Rishon LeZion': 90,
        'Kfar Saba': 90,
        'Holon': 90,
        'Bat Yam': 90,
        'Ramat Gan': 90,
        'Bnei Brak': 90,
        'Petah Tikva': 90,
        'Rehovot': 90,
        'Modiin-Maccabim-Reut': 90,
        'Kiryat Ono': 90,
        'Yavne': 90,
        'Nazareth': 120,
        'Afula': 120,
        'Karmiel': 120,
        'Tiberias': 120,
        'Sderot': 60,
        'Nahariya': 120,
        'Qiryat Shemona': 120,
        'Rosh HaAyin': 90,
        'Givat Shmuel': 90,
        'Bet Shemesh': 90,
        'Dimona': 90,
    }

    return warning_times.get(city, 'City not found, please enter a valid city in Israel.')

if __name__ == "__main__":
    city = input("Enter a city in Israel: ")
    print(warning_time(city))
