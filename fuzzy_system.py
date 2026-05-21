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


def output_label_from_score(rule_score):
    if rule_score < 38:
        return "Düşük"
    elif rule_score < 63:
        return "Orta"
    elif rule_score < 82:
        return "Yüksek"
    else:
        return "Çok Yüksek"


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

    study_scores = {
        "Düşük": 15,
        "Orta": 58,
        "Yüksek": 92,
    }

    phone_scores = {
        "Az": 95,
        "Orta": 55,
        "Fazla": 15,
    }

    sleep_scores = {
        "Kötü": 15,
        "Orta": 58,
        "İyi": 92,
    }

    break_scores = {
        "Yetersiz": 35,
        "Dengeli": 90,
        "Aşırı": 30,
    }

    aggregated = np.zeros_like(efficiency_x)
    active_rules = []

    for study_label, study_degree in memberships["study"].items():
        for phone_label, phone_degree in memberships["phone"].items():
            for sleep_label, sleep_degree in memberships["sleep"].items():
                for break_label, break_degree in memberships["break"].items():

                    activation = min(
                        study_degree,
                        phone_degree,
                        sleep_degree,
                        break_degree
                    )

                    if activation <= 0:
                        continue

                    rule_score = (
                        study_scores[study_label] * 0.35 +
                        phone_scores[phone_label] * 0.25 +
                        sleep_scores[sleep_label] * 0.25 +
                        break_scores[break_label] * 0.15
                    )

                    output_label = output_label_from_score(rule_score)
                    output_mf = mfs["efficiency"][output_label]

                    clipped = np.fmin(activation, output_mf)
                    aggregated = np.fmax(aggregated, clipped)

                    active_rules.append({
                        "rule": (
                            f"Çalışma {study_label.lower()}, "
                            f"telefon {phone_label.lower()}, "
                            f"uyku {sleep_label.lower()}, "
                            f"mola {break_label.lower()}"
                        ),
                        "activation": round(float(activation), 3),
                        "output": output_label,
                        "rule_score": round(float(rule_score), 2)
                    })

    if np.sum(aggregated) == 0:
        score = 0
    else:
        score = fuzz.defuzz(efficiency_x, aggregated, "centroid")

    active_rules = sorted(
        active_rules,
        key=lambda x: x["activation"],
        reverse=True
    )[:12]

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