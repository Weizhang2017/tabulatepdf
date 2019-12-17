### A CLI for [tabula-py](https://github.com/chezou/tabula-py)

#### Installation

Install using pip:
```shell
pip install tabulatepdf
```
Install from Github
```shell
git clone https://github.com/Weizhang2017/tabulatepdf
cd tabulatepdf 
python setup.py install
```

#### CLI

```shell
usage: tabulatepdf [-h] --pdf pdf [--output output] [--page page]

extract tables from pdf

optional arguments:
  -h, --help       show this help message and exit
  --pdf pdf        pdf file to extract tables from
  --output output  output filename, default: output.csv
  --page page      page number of pdf to extract from, default: 1
```

###### Simple Example:

```shell
tabulatepdf --pdf sample.pdf --output output.csv --page 10
table saved to output.csv
```
