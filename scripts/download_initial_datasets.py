import os
import urllib.request
from zipfile import ZipFile

# Directory to store raw datasets
data_dir = "data/raw/"

# Ensure the data directory exists
os.makedirs(data_dir, exist_ok=True)


def download_kaggle_dataset(api_url, dataset_name, destination):
    if not os.path.exists(destination):
        print(f"Downloading {dataset_name} dataset from Kaggle...")
        os.system(f'kaggle datasets download -d {api_url} -p {data_dir}')
        # Wait for the download to complete
        print("Download complete. Extracting files...")
        with ZipFile(f"{destination}.zip", 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        os.remove(f"{destination}.zip")
        print(f"{dataset_name} dataset downloaded and extracted.")
    else:
        print(f"{dataset_name} dataset already exists. Skipping download.")


def download_with_headers(url, destination, headers):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response, open(destination, 'wb') as out_file:
        out_file.write(response.read())

def download_phishtank(destination):
    phishtank_api_key = os.getenv('PHISHTANK_API_KEY')
    if phishtank_api_key:
        phishtank_url = f"http://data.phishtank.com/data/{phishtank_api_key}/online-valid.csv"
        print("Downloading PhishTank dataset using API key...")
    else:
        phishtank_url = "http://data.phishtank.com/data/online-valid.csv"
        print("Downloading PhishTank dataset using generic URL...")

    if not os.path.exists(destination):
        # Add descriptive User-Agent to the request
        headers = {'User-Agent': 'phistank/cqc_frostbyte07'}
        download_with_headers(phishtank_url, destination, headers)
        print("PhishTank dataset downloaded.")
    else:
        print("PhishTank dataset already exists. Skipping download.")


def download_generic_dataset(url, destination, dataset_name):
    if not os.path.exists(destination):
        print(f"Downloading {dataset_name} dataset...")
        urllib.request.urlretrieve(url, destination)
        print(f"{dataset_name} dataset downloaded.")
    else:
        print(f"{dataset_name} dataset already exists. Skipping download.")


# Phishing Detection
download_kaggle_dataset("danielfernandon/web-page-phishing-dataset", "Phishing Websites",
                        os.path.join(data_dir, "web-page-phishing-dataset"))

# PhishTank Database
download_phishtank(os.path.join(data_dir, "phishtank.csv"))

# Malware Classification
download_kaggle_dataset("c/microsoft-malware-classification", "Microsoft Malware Classification",
                        os.path.join(data_dir, "microsoft_malware"))

# Malicia Project Dataset
malicia_url = "http://malicia-project.com/download.php"  # Example URL; adjust if necessary
download_generic_dataset(malicia_url, os.path.join(data_dir, "malicia_project.zip"), "Malicia Project")

# Unauthorized Access Detection
download_generic_dataset("https://research.unsw.edu.au/sites/default/files/documents/UNSW-NB15.tar.gz",
                         os.path.join(data_dir, "unsw_nb15.tar.gz"), "UNSW-NB15")

download_generic_dataset("http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz",
                         os.path.join(data_dir, "kddcup99.gz"), "KDD CUP 99")

print("All datasets have been processed.")
