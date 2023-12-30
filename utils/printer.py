from colorama import init, Fore, Style

init(autoreset=True)

class Printer:
    @staticmethod
    def print_colored_text(text, color=Fore.WHITE, indent=0):
        indentation = " " * indent
        print(f"{indentation}{color}{text}{Style.RESET_ALL}")

    @staticmethod
    def print_success(text, indent=0):
        Printer.print_colored_text(f":) {text}", color=Fore.GREEN, indent=indent)

    @staticmethod
    def print_error(text, indent=0):
        Printer.print_colored_text(f"!!! {text}", color=Fore.RED, indent=indent)

    @staticmethod
    def print_info(text, indent=0):
        Printer.print_colored_text(f"# {text}", color=Fore.BLUE, indent=indent)

    @staticmethod
    def print_text(text, indent=0):
        Printer.print_colored_text(f"{text}", color=Fore.WHITE, indent=indent)
