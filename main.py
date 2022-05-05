import re

def cleaner(requests):
    try:
        x_str = request.form.get('text')
    except:
        x_str = requests['text']
    clean_str = re.sub('[^a-zA-Z0-9]', '_', x_str)
    print(clean_str)
    return clean_str

if __name__ == "__main__":
    cleaner()
