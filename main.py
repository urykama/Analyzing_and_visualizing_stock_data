import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)


def main_02():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        """Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть:
        AAPL (Apple Inc),                   GOOGL (Alphabet Inc),
        MSFT (Microsoft Corporation),       AMZN (Amazon.com Inc),
        TSLA (Tesla Inc).""")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = 'AAPL'
    period = '1mo'

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Вычислить среднее значение колонки 'Close'. Результат будет выводиться в консоль.
    print('Средняя цена закрытия акций за заданный период: ', dd.calculate_and_display_average_price(stock_data))
    # Уведомление о сильных колебаниях

    # threshold = float(input("Уведомление о сильных колебаниях. Введите порог колебания цен в процентах: "))
    # dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # filename = 'stock_data'
    filename = 'stock_data.csv'
    dd.export_data_to_csv(stock_data, filename)

    # В дата-фрейм добавляем данные технического индикатора RSI
    # Add Relative Strength Index to the data
    stock_data['RSI'] = dd.calculate_rsi(stock_data)
    # print(stock_data)
    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)


def main_05():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        """Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть:
        AAPL (Apple Inc),                   GOOGL (Alphabet Inc),
        MSFT (Microsoft Corporation),       AMZN (Amazon.com Inc),
        TSLA (Tesla Inc),                   ^GSPC (S&P 500)""")
    print(
        "Периоды времени для данных: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max")

    # Модифицировать main.py для приёма дат начала и окончания,
    # а также обеспечить передачу этих параметров в fetch_stock_data.
    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    start_date = input("Введите дату начала периода в формате YYYY-MM-DD: ")
    end_date = input("Введите дату окончания периода в формате YYYY-MM-DD: ")
    # Fetch stock data
    stock_data = dd.fetch_stock_data_not_using_period(ticker, start_date, end_date)

    # Вычислить среднее значение колонки 'Close'. Результат будет выводиться в консоль.
    print('Средняя цена закрытия акций за заданный период: ', dd.calculate_and_display_average_price(stock_data))
    # Уведомление о сильных колебаниях

    # threshold = float(input("Уведомление о сильных колебаниях. Введите порог колебания цен в процентах: "))
    # dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # filename = 'stock_data'
    filename = 'stock_data.csv'
    dd.export_data_to_csv(stock_data, filename)

    # В дата-фрейм добавляем данные технического индикатора RSI
    # Add Relative Strength Index to the data
    stock_data['RSI'] = dd.calculate_rsi(stock_data)
    # print(stock_data)
    # Plot the data
    dplt.create_and_save_plot_004(stock_data, ticker)


if __name__ == "__main__":
    # main()
    main_05()
