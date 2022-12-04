import csv
import database

MAIN_MENU = "MAIN MENU\n0 Exit\n1 CRUD operations\n2 Show top ten companies by criteria"
CRUD_MENU = "CRUD MENU\n0 Back\n1 Create a company\n2 Read a company\n3 Update a company\n4 Delete a company\n5 List " \
            "all companies"
TOP_TEN_MENU = "TOP TEN MENU\n0 Back\n1 List by ND/EBITDA\n2 List by ROE\n3 List by ROA"
NICE_DAY = "Have a nice day!"


class InvestCalc:
    pass


def main():
    while True:
        menu_input = input(f'{MAIN_MENU}\nEnter an option: ')
        match menu_input:
            case '1':
                crud_input = input(f'{CRUD_MENU}\nEnter an option: ')
                match crud_input:
                    case '0':
                        print(NICE_DAY)
                        exit()
                    case _:
                        print('Not implemented!')
            case '2':
                ten_menu = input(f'{TOP_TEN_MENU}\nEnter an option: ')
                match ten_menu:
                    case '0':
                        print(NICE_DAY)
                        exit()
                    case _:
                        print('Not implemented!')
            case '0':
                print(NICE_DAY)
                exit()
            case _:
                print('Invalid option!')


if __name__ == '__main__':
    # main()
    database.main()
