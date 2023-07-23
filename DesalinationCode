import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def word_counts(texts):
    """Calculates the word counts for multiple texts and returns a list of Counter objects."""
    word_counts_list = []
    for text in texts:
        words = text.split(" ")
        word_counts_list.append(Counter(words))
    return word_counts_list

def plot_word_counts(word_counts_list):
    """Plots word counts for multiple texts in separate bar plots."""
    num_texts = len(word_counts_list)
    fig, axes = plt.subplots(1, num_texts, figsize=(5 * num_texts, 4))
    for i, counts in enumerate(word_counts_list):
        words = list(counts.keys())
        counts = list(counts.values())
        axes[i].bar(range(len(words)), counts, alpha=0.7, label=f"Text {i+1}")
        axes[i].set_xticks(range(len(words)))
        axes[i].set_xticklabels(words, rotation=45, ha="right")
        axes[i].set_xlabel("Word")
        axes[i].set_ylabel("Count")
        axes[i].set_title(f"Word Counts for Text {i+1}")
        axes[i].legend()

    plt.tight_layout()
    plt.show()

def plot_elevations(elevations):
    """Plots the elevations of each run."""
    plt.plot(elevations, marker='o', linestyle='-', color='b', label='Elevations')
    plt.xlabel("Run")
    plt.ylabel("Elevation")
    plt.legend()
    plt.title("Elevations of Each Run")
    plt.show()

def plot_salt_buildup(salt_buildup):
    """Plots the salt buildup after a year of running the desalination plant."""
    plt.plot(salt_buildup, marker='s', linestyle='--', color='g', label='Salt Buildup')
    plt.axhline(salt_buildup[0], color="red", label="Year 1", linewidth=2)
    plt.xlabel("Month")
    plt.ylabel("Salt Buildup (mg/L)")
    plt.legend()
    plt.title("Salt Buildup Over Time")
    plt.show()

def plot_anion_status(anion_concentrations):
    """Plots the status of anion concentrations over time."""
    months = range(len(anion_concentrations))

    plt.plot(months, anion_concentrations, marker='o', linestyle='-', color='b', label='Anion Concentration')
    plt.xlabel("Month")
    plt.ylabel("Concentration (mg/L)")
    plt.legend()
    plt.title("Anion Concentration Over Time")
    plt.tight_layout()
    plt.show()

def plot_cation_status(cation_concentrations):
    """Plots the status of cation concentrations over time."""
    months = range(len(cation_concentrations))

    plt.plot(months, cation_concentrations, marker='s', linestyle='--', color='r', label='Cation Concentration')
    plt.xlabel("Month")
    plt.ylabel("Concentration (mg/L)")
    plt.legend()
    plt.title("Cation Concentration Over Time")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    texts = [
        "Desalination is the process of removing salt from seawater to produce freshwater.",
        "Freshwater is essential for all life on Earth."
    ]
    plot_word_counts(word_counts(texts))

    elevations = [100, 200, 300, 400, 500]
    plot_elevations(elevations)

    salt_buildup = [10, 20, 30, 40, 50]
    plot_salt_buildup(salt_buildup)

    # Generating random data for anion and cation concentrations at different months
    np.random.seed(42)
    anion_concentrations = np.random.randint(5, 15, 5)
    cation_concentrations = np.random.randint(10, 20, 5)

    plot_anion_status(anion_concentrations)
    plot_cation_status(cation_concentrations)
