import psycopg2

conn = psycopg2.connect(
    dbname="mydb",
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS apartments (
        id SERIAL PRIMARY KEY,
        city VARCHAR(100),
        district VARCHAR(100),
        address VARCHAR(255),
        area NUMERIC,
        rooms INT,
        floor INT,
        year_built INT,
        price NUMERIC,
        type VARCHAR(50)
    )
""")

apartments_data = [
    ("Москва", "Центральный", "ул. Арбат, 10", 55.5, 2, 5, 2000, 4500000, "Вторичка"),
    ("Санкт-Петербург", "Адмиралтейский", "Невский проспект, 50", 60.0, 3, 7, 2015, 6000000, "Новостройка"),
    ("Казань", "Советский", "ул. Баумана, 12", 48.0, 2, 4, 2010, 3500000, "Вторичка"),
    ("Екатеринбург", "Ленинский", "пр. Ленина, 25", 70.0, 3, 9, 2018, 7000000, "Новостройка"),
    ("Новосибирск", "Железнодорожный", "ул. Кирова, 3", 52.0, 2, 2, 2005, 4000000, "Вторичка"),
    ("Ростов-на-Дону", "Кировский", "ул. Садовая, 15", 58.0, 3, 6, 2012, 5000000, "Новостройка"),
    ("Сочи", "Хостинский", "ул. Курортная, 8", 90.0, 4, 10, 2020, 12000000, "Новостройка"),
    ("Краснодар", "Фестивальный", "ул. Красная, 101", 40.0, 1, 3, 2013, 3200000, "Вторичка"),
    ("Омск", "Центральный", "ул. Ленина, 5", 45.0, 2, 1, 2008, 2800000, "Вторичка"),
    ("Уфа", "Советский", "ул. Октябрьская, 22", 65.0, 3, 8, 2016, 5400000, "Новостройка")
]

cursor.executemany("""
    INSERT INTO apartments (city, district, address, area, rooms, floor, year_built, price, type)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""", apartments_data)

conn.commit()
cursor.close()
conn.close()

print("Таблица создана и данные добавлены!")
