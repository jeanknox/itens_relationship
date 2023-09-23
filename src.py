from io import StringIO
import pandas as pd
from bs4 import BeautifulSoup
import os
from tqdm import tqdm

file_path = os.path.join(
    os.path.expanduser("~"),
    "Área de Trabalho",
    "Programacao",
    "python",
    "itens_relationship",
    "xml",
)
xml_file_names = [item for item in os.listdir(file_path) if item.endswith(".XML")]
for item in tqdm(xml_file_names):
    with open(os.path.join(file_path, item)) as file:
        file_data = file.read()

    soup = BeautifulSoup(StringIO(file_data), "lxml")
    itens = soup.find_all("det")
    for i in range(0, len(itens)):
        pass
        # print(itens[i].prod.cean.text)
