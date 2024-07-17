from MGMService import get_data
import csv

dataset = get_data("sondurumlar/ilmerkezleri")

with open("veriler.csv", mode="w", newline="", encoding="utf-8") as csvfile:
    fieldnames = dataset[0].keys()  # Sözlükteki anahtarlar CSV başlıkları olacak
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Başlık satırını yaz
    for veri in dataset:
        writer.writerow(veri)  # Her sözlüğü bir satır olarak yaz
