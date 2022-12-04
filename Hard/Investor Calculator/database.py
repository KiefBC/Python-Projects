import csv

from sqlalchemy import create_engine, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///investor.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class CompanyDatabase(Base):
    __tablename__ = 'companies'

    ticker = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)


class FinancialDatabase(Base):
    __tablename__ = 'financial'

    ticker = Column(String, primary_key=True)
    ebitda = Column(Float)
    sales = Column(Float)
    net_profit = Column(Float)
    market_price = Column(Float)
    net_debt = Column(Float)
    assets = Column(Float)
    equity = Column(Float)
    cash_equivalents = Column(Float)
    liabilities = Column(Float)


def main():
    Base.metadata.create_all(engine)

    with open("companies.csv", newline='') as companies:
        file_reader = csv.reader(companies, delimiter=",")  # Create a reader object
        next(file_reader)
        for line in file_reader:  # Read each line
            ticker = line[0]
            name = line[1]
            sector = line[2]
            add_company = CompanyDatabase(ticker=ticker, name=name, sector=sector)
            session.add(add_company)
            session.commit()

        with open("financial.csv", newline='') as financials:
            file_reader = csv.DictReader(financials, delimiter=",")
            for line in file_reader:
                for v in line.items():
                    if v[1] == '':
                        line[v[0]] = None
                ticker = line['ticker']
                ebitda = line['ebitda']
                sales = line['sales']
                net_profit = line['net_profit']
                market_price = line['market_price']
                net_debt = line['net_debt']
                assets = line['assets']
                equity = line['equity']
                cash_equivalents = line['cash_equivalents']
                liabilities = line['liabilities']
                add_financial = FinancialDatabase(ticker=ticker, ebitda=ebitda, sales=sales, net_profit=net_profit,
                                                  market_price=market_price, net_debt=net_debt, assets=assets,
                                                  equity=equity, cash_equivalents=cash_equivalents,
                                                  liabilities=liabilities)
                session.add(add_financial)
                session.commit()

    session.commit()
    print('Database created successfully!')


if __name__ == '__main__':
    main()
