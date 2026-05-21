import matplotlib.pyplot as plt
import numpy as np


def plot_memberships(result):
    mfs = result["mfs"]
    universes = result["universes"]
    memberships = result["memberships"]

    input_values = {
        "study": result.get("input_values", {}).get("study", None),
        "phone": result.get("input_values", {}).get("phone", None),
        "sleep": result.get("input_values", {}).get("sleep", None),
        "break": result.get("input_values", {}).get("break", None),
    }

    fig, axes = plt.subplots(2, 2, figsize=(7.0, 4.0), dpi=130)

    variables = [
        ("study", "Çalışma Süresi", "Saat"),
        ("phone", "Telefon Kullanımı", "Saat"),
        ("sleep", "Uyku Kalitesi", "Puan"),
        ("break", "Mola Düzeni", "Puan"),
    ]

    for ax, (var, title, unit) in zip(axes.flatten(), variables):
        x = universes[var]

        for label, mf in mfs[var].items():
            ax.plot(x, mf, label=label, linewidth=1.2)

            activation = memberships[var][label]
            if activation > 0:
                clipped = np.fmin(activation, mf)
                ax.fill_between(x, 0, clipped, alpha=0.28)

        value = input_values[var]
        if value is not None:
            ax.axvline(value, linestyle="--", linewidth=1.2)
            ax.text(
                value,
                1.03,
                f"{value:.1f}",
                fontsize=6,
                ha="center",
                va="bottom"
            )

        ax.set_title(title, fontsize=8)
        ax.set_xlabel(unit, fontsize=6)
        ax.set_ylabel("Üyelik", fontsize=6)
        ax.tick_params(labelsize=6)
        ax.legend(fontsize=5, loc="best")
        ax.grid(True, alpha=0.25)
        ax.set_ylim(0, 1.12)

    plt.subplots_adjust(
        left=0.07,
        right=0.98,
        top=0.91,
        bottom=0.12,
        wspace=0.28,
        hspace=0.55
    )

    return fig


def plot_defuzzification(result):
    x = result["universes"]["efficiency"]
    aggregated = result["aggregated"]
    mfs = result["mfs"]["efficiency"]
    score = result["score"]

    fig, ax = plt.subplots(figsize=(7.0, 3.0), dpi=130)

    for label, mf in mfs.items():
        ax.plot(x, mf, label=label, linewidth=1.2)

    ax.fill_between(x, 0, aggregated, alpha=0.35)

    ax.axvline(
        score,
        linestyle="--",
        linewidth=1.8,
        label=f"Centroid = {score}"
    )

    ax.text(
        score,
        1.04,
        f"{score}",
        fontsize=7,
        ha="center",
        va="bottom"
    )

    ax.set_title("Durulaştırma Grafiği", fontsize=9)
    ax.set_xlabel("Verimlilik Skoru", fontsize=7)
    ax.set_ylabel("Üyelik Derecesi", fontsize=7)
    ax.tick_params(labelsize=6)
    ax.legend(fontsize=6, loc="upper left")
    ax.grid(True, alpha=0.25)
    ax.set_ylim(0, 1.12)

    plt.tight_layout()
    return fig