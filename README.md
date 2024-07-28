# Python Authenticator

## Dependencias:

Librería pyotp.

Instalarla vía:
```
pip install pyotp
```
https://pypi.org/project/pyotp/

## Modo de uso

`otp.py [-h] [-q,--quiet] [-k,--keys] [key]`

Si se ejecuta el programa sin pasarle ningún argumento, mostrará los valores una sola vez en el momento en que se ejecute. Si se le pasa tanto una clave de la sección DEFAULT como de la sección ALIASES (más adelante se un archivo de configuración de ejemplo) mostrará por pantalla el valor de esa clave en ese momento. Si la utilidad está disponible en su sistema operativo, se copiará la clave directamente en el portapapeles. Si se pasa el argumento -q o --quiet, no se mostrará información por consola solo si la herramienta para copiar el valor directamente en el portapapeles está disponible. Si no lo está, se mostrará el valor de la clave por consola.

Si se pasa la flag -k o --keys, se mostrará por consola todas las claves que se leyeron correctamente del archivo de configuración.

Idealmente, la sección DEFAULT es para guardar todos los códigos que se usarán asociados a una clave autodescriptiva. La sección ALIASES es para acceder a esas claves, las cuales por ser autodescriptivas pueden ser largas, con un alias.

## Parámetros:

- key : Clave para acceder al valor.

- -k, --keys : Imprimir por consola todas las claves que se han leído del archivo de configuración.

- -q, --quiet : Modo silencioso.

## Ejemplo de archivo de Configuración
```
[DEFAULT]
google_account = nbsw y3dp gezd gmjs gmyt emzr gizt cmrt
google_account2 = jbcuytcpgizdgmrsgmzdemzsgiztemrt
X_account = mfrggzdfmztwq2lknnwg23tpobyxe5dv
strange_account = nnwg23tpobyxe5dv

[ALIASES]
google = %(google_account)s
1 = %(google)s
x = mfrggzdfmztwq2lknnwg23tpobyxe5dv
2 = %(X_account)s
```