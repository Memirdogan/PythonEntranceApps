
def addressVal(mail):
    dot = mail.find(".")
    at = mail.find("@")

    if dot == -1:
        print("Geçersiz mail adresi")
    elif at == -1:
        print("Geçersiz mail adresi")
    else:
        print("Geçerli mail adresi")

def main():
    print("Bu program girdiğiniz bilginin geçerli bir e-posta adresi olup olmadığına karar verecektir")
    print()
    while True:
        print("Geçerli bir e-posta adresinde '@' sembolü ve '.' işareti bulunmalıdır.")
        print()
        mail = input("Mail adresinizi giriniz: ")
        addressVal(mail)


if __name__ == '__main__':
    main()
