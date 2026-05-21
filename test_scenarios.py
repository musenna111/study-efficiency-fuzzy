from fuzzy_system import calculate_efficiency


scenarios = [
    {
        "name": "Sağlıklı ve Verimli Çalışma",
        "study_hours": 7,
        "phone_hours": 1,
        "sleep_quality": 9,
        "break_quality": 7
    },
    {
        "name": "Ortalama Çalışma Düzeni",
        "study_hours": 4,
        "phone_hours": 2,
        "sleep_quality": 5,
        "break_quality": 5
    },
    {
        "name": "Düşük Verimli Çalışma",
        "study_hours": 1,
        "phone_hours": 5,
        "sleep_quality": 3,
        "break_quality": 9
    },
    {
        "name": "Çok Çalışma Ama Dengesiz Kullanım",
        "study_hours": 7,
        "phone_hours": 5,
        "sleep_quality": 4,
        "break_quality": 2
    },
    {
        "name": "Dengeli Fakat Orta Seviye",
        "study_hours": 5,
        "phone_hours": 2,
        "sleep_quality": 6,
        "break_quality": 6
    }
]


for scenario in scenarios:
    result = calculate_efficiency(
        scenario["study_hours"],
        scenario["phone_hours"],
        scenario["sleep_quality"],
        scenario["break_quality"]
    )

    print("-" * 50)
    print("Senaryo:", scenario["name"])
    print("Çalışma Süresi:", scenario["study_hours"])
    print("Telefon Kullanımı:", scenario["phone_hours"])
    print("Uyku Kalitesi:", scenario["sleep_quality"])
    print("Mola Düzeni:", scenario["break_quality"])
    print("Verimlilik Skoru:", result["score"])
    print("Verimlilik Seviyesi:", result["level"])
    print("Aktif Kural Sayısı:", len(result["active_rules"]))