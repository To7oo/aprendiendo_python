import sys, webbrowser

args = sys.argv[1:]

if len(args) < 1:
    print('No se ha proporcionado una ubicación')
    exit()


adress = ' '.join(args)

url = 'https://www.google.com/maps/place/'

webbrowser.open_new(url + adress)

print('fin del programa')
print('Holi')