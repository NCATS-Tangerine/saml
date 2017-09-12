# saml

## Install

Requires: Python3

```
python3.6 -m venv <env>
source <env>/bin/activate
pip install -r requirements.txt
jupyter notebook
```
This should open a jupyter notebook window. Open the SAML_Authentication notebook and runn the cells.

In a terminal window, run:

```
python client.py localhost saml.xml
```

Currently, this produces an error saying that the XML is not properly formed.

