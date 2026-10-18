import os
import kagglehub


os.makedirs("Data", exist_ok=True)


path = kagglehub.dataset_download(
    "nasa/kepler-exoplanet-search-results",
    output_dir="Data",
    force_download=True
)

print("Dataset saved to: ", path)