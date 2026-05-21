import numpy as np
import skfuzzy as fuzz


study_x = np.arange(0, 8.1, 0.1)
phone_x = np.arange(0, 6.1, 0.1)
sleep_x = np.arange(0, 10.1, 0.1)
break_x = np.arange(0, 10.1, 0.1)
efficiency_x = np.arange(0, 100.1, 0.1)


def trimf(x, points):
    return fuzz.trimf(x, points)


def trapmf(x, points):
    return fuzz.trapmf(x, points)


def get_membership_functions():
    return {
        "study": {
            "Düşük": trapmf(study_x, [0, 0, 1.5, 3.2]),
            "Orta": trimf(study_x, [2.0, 4.0, 6.0]),
            "Yüksek": trapmf(study_x, [5.0, 6.5, 8.0, 8.0]),
        },
        "phone": {
            "Az": trapmf(phone_x, [0, 0, 0.8, 2.0]),
            "Orta": trimf(phone_x, [1.2, 3.0, 4.5]),
            "Fazla": trapmf(phone_x, [3.8, 5.0, 6.0, 6.0]),
        },
        "sleep": {
            "Kötü": trapmf(sleep_x, [0, 0, 3.0, 5.2]),
            "Orta": trimf(sleep_x, [4.0, 6.0, 8.0]),
            "İyi": trapmf(sleep_x, [6.8, 8.5, 10.0, 10.0]),
        },
        "break": {
            "Yetersiz": trapmf(break_x, [0, 0, 2.5, 4.5]),
            "Dengeli": trimf(break_x, [3.0, 6.0, 8.0]),
            "Aşırı": trapmf(break_x, [7.0, 8.5, 10.0, 10.0]),
        },
        "efficiency": {
            "Düşük": trapmf(efficiency_x, [0, 0, 18, 40]),
            "Orta": trimf(efficiency_x, [30, 50, 68]),
            "Yüksek": trimf(efficiency_x, [58, 75, 90]),
            "Çok Yüksek": trapmf(efficiency_x, [82, 92, 100, 100]),
        },
    }


def get_efficiency_level(score):
    if score < 40:
        return "Düşük Verimlilik"
    elif score < 65:
        return "Orta Verimlilik"
    elif score < 82:
        return "Yüksek Verimlilik"
    else:
        return "Çok Yüksek Verimlilik"


def calculate_efficiency(study_hours, phone_hours, sleep_quality, break_quality):
    mfs = get_membership_functions()

    memberships = {
        "study": {
            name: fuzz.interp_membership(study_x, mf, study_hours)
            for name, mf in mfs["study"].items()
        },
        "phone": {
            name: fuzz.interp_membership(phone_x, mf, phone_hours)
            for name, mf in mfs["phone"].items()
        },
        "sleep": {
            name: fuzz.interp_membership(sleep_x, mf, sleep_quality)
            for name, mf in mfs["sleep"].items()
        },
        "break": {
            name: fuzz.interp_membership(break_x, mf, break_quality)
            for name, mf in mfs["break"].items()
        },
    }

    aggregated = np.zeros_like(efficiency_x)
    active_rules = []

    rules = [
        (
            "IF çalışma yüksek AND telefon az AND uyku iyi THEN verimlilik çok yüksek",
            min(memberships["study"]["Yüksek"], memberships["phone"]["Az"], memberships["sleep"]["İyi"]),
            "Çok Yüksek"
        ),
        (
            "IF çalışma yüksek AND telefon orta AND uyku iyi THEN verimlilik yüksek",
            min(memberships["study"]["Yüksek"], memberships["phone"]["Orta"], memberships["sleep"]["İyi"]),
            "Yüksek"
        ),
        (
            "IF çalışma yüksek AND mola dengeli THEN verimlilik yüksek",
            min(memberships["study"]["Yüksek"], memberships["break"]["Dengeli"]),
            "Yüksek"
        ),
        (
            "IF çalışma yüksek AND telefon fazla THEN verimlilik orta",
            min(memberships["study"]["Yüksek"], memberships["phone"]["Fazla"]),
            "Orta"
        ),
        (
            "IF çalışma orta AND telefon az AND uyku iyi THEN verimlilik yüksek",
            min(memberships["study"]["Orta"], memberships["phone"]["Az"], memberships["sleep"]["İyi"]),
            "Yüksek"
        ),
        (
            "IF çalışma orta AND telefon orta AND uyku orta THEN verimlilik orta",
            min(memberships["study"]["Orta"], memberships["phone"]["Orta"], memberships["sleep"]["Orta"]),
            "Orta"
        ),
        (
            "IF çalışma orta AND mola dengeli THEN verimlilik orta",
            min(memberships["study"]["Orta"], memberships["break"]["Dengeli"]),
            "Orta"
        ),
        (
            "IF çalışma orta AND telefon fazla THEN verimlilik düşük",
            min(memberships["study"]["Orta"], memberships["phone"]["Fazla"]),
            "Düşük"
        ),
        (
            "IF çalışma düşük AND telefon az AND uyku iyi THEN verimlilik orta",
            min(memberships["study"]["Düşük"], memberships["phone"]["Az"], memberships["sleep"]["İyi"]),
            "Orta"
        ),
        (
            "IF çalışma düşük AND telefon orta THEN verimlilik düşük",
            min(memberships["study"]["Düşük"], memberships["phone"]["Orta"]),
            "Düşük"
        ),
        (
            "IF çalışma düşük AND telefon fazla THEN verimlilik düşük",
            min(memberships["study"]["Düşük"], memberships["phone"]["Fazla"]),
            "Düşük"
        ),
        (
            "IF uyku kötü AND telefon fazla THEN verimlilik düşük",
            min(memberships["sleep"]["Kötü"], memberships["phone"]["Fazla"]),
            "Düşük"
        ),
        (
            "IF uyku kötü AND çalışma düşük THEN verimlilik düşük",
            min(memberships["sleep"]["Kötü"], memberships["study"]["Düşük"]),
            "Düşük"
        ),
        (
            "IF uyku iyi AND mola dengeli AND çalışma orta THEN verimlilik yüksek",
            min(memberships["sleep"]["İyi"], memberships["break"]["Dengeli"], memberships["study"]["Orta"]),
            "Yüksek"
        ),
        (
            "IF mola aşırı AND çalışma düşük THEN verimlilik düşük",
            min(memberships["break"]["Aşırı"], memberships["study"]["Düşük"]),
            "Düşük"
        ),
        (
            "IF mola aşırı AND telefon fazla THEN verimlilik düşük",
            min(memberships["break"]["Aşırı"], memberships["phone"]["Fazla"]),
            "Düşük"
        ),
        (
            "IF mola yetersiz AND çalışma yüksek THEN verimlilik yüksek",
            min(memberships["break"]["Yetersiz"], memberships["study"]["Yüksek"]),
            "Yüksek"
        ),
        (
            "IF telefon az AND uyku iyi AND mola dengeli THEN verimlilik çok yüksek",
            min(memberships["phone"]["Az"], memberships["sleep"]["İyi"], memberships["break"]["Dengeli"]),
            "Çok Yüksek"
        ),
    ]

    for rule_text, activation, output_label in rules:
        if activation <= 0:
            continue

        output_mf = mfs["efficiency"][output_label]
        clipped = np.fmin(activation, output_mf)
        aggregated = np.fmax(aggregated, clipped)

        active_rules.append({
            "rule": rule_text,
            "activation": round(float(activation), 3),
            "output": output_label
        })

    if np.sum(aggregated) == 0:
        score = 0
    else:
        score = fuzz.defuzz(efficiency_x, aggregated, "centroid")

    active_rules = sorted(
        active_rules,
        key=lambda x: x["activation"],
        reverse=True
    )

    return {
        "score": round(float(score), 2),
        "level": get_efficiency_level(score),
        "memberships": memberships,
        "active_rules": active_rules,
        "aggregated": aggregated,
        "mfs": mfs,
        "universes": {
            "study": study_x,
            "phone": phone_x,
            "sleep": sleep_x,
            "break": break_x,
            "efficiency": efficiency_x,
        },
        "input_values": {
            "study": study_hours,
            "phone": phone_hours,
            "sleep": sleep_quality,
            "break": break_quality,
        }
    }