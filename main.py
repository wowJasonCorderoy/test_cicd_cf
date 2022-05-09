import re
import os
import json

def cleaner(requests):
    """
    cleans strings replaces nums chars with underscores.
    """
    try:
        x_str = requests.form.get('text')
    except:
        x_str = requests['text']
    clean_str = re.sub('[^a-zA-Z0-9]', '_', x_str)
    print(clean_str)
    return clean_str

def secret_length(requests):
    """
    print length of a secrets value.
    """
    env_var_ibm_creds = 'ibm-creds'
    ibm_creds = json.loads(os.environ[env_var_ibm_creds])
    url = ibm_creds['url']
    print(len(url))

if __name__ == "__main__":
    #cleaner()
    secret_length()
