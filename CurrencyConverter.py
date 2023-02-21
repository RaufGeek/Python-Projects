def main():
    print("This program convert US dollars to AZE manat")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    manat = convert_to_manat(dollars)

    print("That is", manat, "AZE manat.")


convert_to_manat = lambda dollars: dollars * 1.70


main()
