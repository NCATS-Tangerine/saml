import json, sys, requests;

print ("-------- {}".format (sys.argv))

flag, host, file = sys.argv;
data=open(file).read() #.replace ('\n', ' ');

j=requests.post (
    url='http://{0}:8000/saml/sso/unc'.format (host),
    data=json.dumps ({
        "SAMLResponse" : data,
        "RelayState"   : "http://relay.state/x"
        }, indent=2),
    headers={ 'Content-Type' : 'application/json' }).json ();

print(json.dumps(j, indent=2))
      
      
