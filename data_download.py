"""Отвечает за загрузку данных об акциях."""
import yfinance as yf
# pip install yfinance --upgrade --no-cache-dir


def fetch_stock_data(ticker, period='1mo'):
    """
    Получает исторические данные об акциях для указанного тикера и временного периода.
    :param ticker:
    :param period:
    :return: Возвращает DataFrame с данными.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
    Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
    :param data:
    :param window_size:
    :return:
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    """
    Вычисляет и выводит среднюю цену закрытия акций за заданный период.
    Функция будет принимать DataFrame и вычислять среднее значение колонки 'Close'.
    Результат будет выводиться в консоль.
    :param data:
    :return:
    """
    average = data['Close'].mean()
    print(average)
