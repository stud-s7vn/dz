from colorama import init, Fore, Back, Style

init(autoreset=True)

def introspect_colorama(module):
    attributes = [attr for attr in dir(module) if not attr.startswith('_')]
    return attributes

print("=== КОЛЬОРИ ТЕКСТУ (Fore) ===")
fore_colors = introspect_colorama(Fore)
for color in fore_colors:
    color_code = getattr(Fore, color)
    print(f"{color_code}{color}")

print("\n=== КОЛЬОРИ ФОНУ (Back) ===")
back_colors = introspect_colorama(Back)
for color in back_colors:
    color_code = getattr(Back, color)

    print(f"{color_code}{Fore.WHITE}{color}")

print("\n=== СТИЛІ (Style) ===")
styles = introspect_colorama(Style)
for style in styles:
    style_code = getattr(Style, style)
    print(f"{style_code}{style}")

#i was lazy ok?
