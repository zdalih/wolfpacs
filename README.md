# wolfpacs
DICOM PACS query and storage

Run on Debian 9.

```
sudo apt-get install -y dcmtk
sudo apt-get install -y python3-pip python3-dev
sudo apt-get install --upgrade pip
```

Must have Python 3.5+ 

# Setup Virtual Environment

Pipenv handles dependencies in the python project, first install it. 

```
pip install pipenv 
pipenv install
```

To add packages in dependencies use the pipenv command instead of pip.

```
pipenv install <package_name>
```

Finally, to  run the virtual environment 

```
pipenv shell
```

