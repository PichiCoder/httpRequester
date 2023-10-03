# Este script sera para lo principal del programa, por no decir todo jajaja, es muy basico.

import urllib.request

def main():
    target = input("Ingrese la URL: ");
    try:
        response = urllib.request.urlopen(target);
        print(response.read());
    except: 
        print("Error al abrir la URL");