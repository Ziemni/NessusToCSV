# NessusToCSV
A simple python script which converts .nessus file into CSV format.



## Introduction
I use Nessus a lot at my work and I love it, but when it comes to exporting scan results it sucks. Export option is limited to only a few formats and its .csv one is pain in the a** to import into Excel.  I wrote this script a while ago, it took me about 10 mins, but I used it ever since.
It's not perfect, but it is very easy to add more features and attributes to it. I hapo you like it :)



## Requirements
- Python 2.7 (But it is easily convertable to 3)
- Python libraries:
  - sys (Should be installed with Python by default)
  - xml.etree.ElementTree (Might require to be insta;;ed manually)



## Usage
```
python <nessus_file> <output_file>
```
Example:
```
python results.nessus out.csv
```



### Thanks!
