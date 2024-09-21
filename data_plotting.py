"""Отвечает за визуализацию данных."""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None):
    """
    Создаёт график, отображающий цены закрытия и скользящие средние.
    + 4 задание добавлен график RSI.
    Предоставляет возможность сохранения графика в файл.
    Параметр filename опционален; если он не указан, имя файла генерируется автоматически.
    :param data:
    :param ticker:
    :param period:
    :param filename:
    :return:
    """
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['RSI'].values, label='Индикатор относительной силы (RSI)')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['RSI'], label='Индикатор относительной силы (RSI)')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def create_and_save_plot_003(data, ticker, period, filename=None):
    """
    Вариант с более красивым (или более понятным) графиком.
    :param data:
    :param ticker:
    :param period:
    :param filename:
    :return:
    """
    plt.figure(figsize=(16, 9))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.title(f"{ticker} Цена акций с течением времени")

            plt.subplot(2,1,1)
            plt.plot(dates, data['Close'].values, label='Close Price', color='red')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.xlabel("Дата")
            plt.ylabel("Цена")
            plt.legend()
            plt.subplot(2,1,2)
            plt.plot(dates, data['RSI'].values, label='RSI', color='orange')
            plt.ylabel("Процент")
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['RSI'], label='Индикатор относительной силы (RSI)')

    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
    plt.grid()
    plt.show()


def probe():
    """Вариант из: https://www.codecamp.ru/blog/matplotlib-two-y-axes/ для примера"""
    # create DataFrames
    df1 = pd.DataFrame({'year': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'sales': [14, 16, 19, 22, 24, 25, 24, 24, 27, 30]})
    df2 = pd.DataFrame({'year': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'leads': [4, 4, 4, 5, 4, 5, 7, 8, 5, 3]})
    # define colors to use
    col1 = 'steelblue'
    col2 = 'red'

    # define subplots
    fig, ax = plt.subplots()

    # add first line to plot
    ax.plot(df1.year, df1.sales, color=col1)

    # add x-axis label
    ax.set_xlabel('Year', fontsize=14)

    # add y-axis label
    ax.set_ylabel('Sales', color=col1, fontsize=16)

    # define second y-axis that shares x-axis with current plot
    ax2 = ax.twinx()

    # add second line to plot
    ax2.plot(df2.year, df2.leads, color=col2)

    # add second y-axis label
    ax2.set_ylabel('Leads', color=col2, fontsize=16)

    plt.savefig("stock_price_chart.png")


# В модуле data_plotting.py добавлен код отрисовки графика показателя rsi
def rsi(stock_data):
    pass


# В модуль data_plotting (37) добавлена функция select_styles, которая отображает доступные стили графиков и
# предлагает пользователю выбрать один из них.
def select_styles():
    pass


if __name__ == "__main__":
    # main()
    probe()
