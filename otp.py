from configparser import ConfigParser, NoOptionError
from argparse import ArgumentParser
try:
    from pyotp import TOTP
except ModuleNotFoundError:
    print('Run: \'pip install pyotp\' first!')
    exit()
try:
    from pyperclip import copy, is_available
    pyperclip_available = is_available()
except ModuleNotFoundError:
    pyperclip_available = False

def get_otp(value:str, config:ConfigParser) -> tuple:
    try:
        result = config.get('ALIASES' if config.has_section('ALIASES') else 'DEFAULT', value)
    except NoOptionError:
        print('No existe la opción {}.'.format(value))
        exit(1)
    secret_code = TOTP(result)
    return result, secret_code.now()

def get_max_length(iterable) -> int:
    max_length = 0
    [max_length := (len(key) if len(key) > max_length else max_length) for key in iterable]
    return max_length

def show_keys(config:ConfigParser) -> None:
    if config.has_section('ALIASES'):
        print('\033[31m[ALIASES]\033[0m')
        keys_in_aliases = [key for key in config.options('ALIASES') if key not in config.defaults().keys()]
        max_length = get_max_length(keys_in_aliases)
        for key in keys_in_aliases:
            points_to = {value:key for key, value in c_parser.defaults().items()}[config.get('ALIASES', key)]
            print(key.ljust(max_length) + ' -> ' + points_to)
    print('\033[34m[DEFAULTS]\033[0m')
    max_length = get_max_length(config.defaults().keys())
    for key, value in config.defaults().items():
        print(key.ljust(max_length) + ' : ' + value)

def main(config:ConfigParser) -> None:
    max_length = get_max_length(config.defaults().keys())
    for key, value in config.defaults().items():
        print(key.ljust(max_length) + ' : ' + TOTP(value).now())

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('key', nargs='?',
                        help='la clave cuyo valor quiere conocer')
    parser.add_argument('-q', action='store_true', dest='quiet',
                        help='modo silencioso')
    parser.add_argument('-k', '--keys', action='store_true', dest='show_keys',
                        help='muestra todas las clave leídas desde el archivo de configuración')
    args = parser.parse_args()
    sep = '/' if '/' in __file__ else '\\'
    script_route = sep.join(__file__.split('\\')[:-1]) + sep
    c_parser = ConfigParser()
    if len(c_parser.read(script_route + 'otp_config.ini', 'utf-8')) == 0:
        print('El archivo otp_config.ini no existe. Lea el archivo README.md para saber como crear uno.')
        exit(1)
    if args.show_keys:
        show_keys(c_parser)
        exit(0)
    if args.key == None:
        main(c_parser)
    else:
        secret, value = get_otp(args.key, c_parser)
        key = args.key if not args.key.isdigit() else {value:key for key, value in c_parser.defaults().items()}[secret]
        if pyperclip_available:
            copy(value)
        if not args.quiet or pyperclip_available == False:
            print('{key}: {value}{extra}'.format(key=key, value=value, extra='\nCopied to clipboard!' if pyperclip_available else ''))