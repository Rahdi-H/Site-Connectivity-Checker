import urllib.request as ur

def main(url):
    print("Checking site connectivity")
    response = ur.urlopen(url)
    print('The response was ', response.getcode())

print('Site connectivity checker')
input = input('enter url')
main(input)