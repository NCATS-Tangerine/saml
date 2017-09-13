# saml

This is an experiment towards a Jupyter notebook authenticating to a SAML IdP.

## Install

Requires: Python3

```
git clone git@github.com:NCATS-Tangerine/saml.git
cd saml
python3.6 -m venv <env>
source <env>/bin/activate
pip install -r requirements.txt
jupyter notebook SAML_Authentication.ipynb 
```
This should open a jupyter notebook window. Run the cells. 
Then, in a terminal window, run:

```
python client.py localhost saml.xml
```

The client reads a SAML response from a file, packages that as a field in a posted JSON object and sends it to our server.

Currently, this produces an error in the notebook saying that the XML is not properly formed. So there's probably an easier way to do the post. If you see the problem, don't hesitate to point it out.

