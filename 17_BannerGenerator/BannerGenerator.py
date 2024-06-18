import sys
import pyfiglet


def ascii_maker():
    print('-' * 70)
    ascii_banner = pyfiglet.figlet_format("ASCII Banner").upper()
    print(ascii_banner)
    print('-' * 70)

    text = input("\nEnter your text: ")
    banner = pyfiglet.figlet_format(f"{text}").upper()
    print(banner)


def end_message():
    print("\n\nThanks for using app <3 \n")
    answer = input("Do you want to run the program again? (y for yes) (any key for no): ")
    if answer.lower() == "y":
        return True
    else:
        sys.exit()


def main():
    while True:
        ascii_maker()
        if not end_message():
            break


main()
