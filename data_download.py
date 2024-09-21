"""Отвечает за загрузку данных об акциях."""
import pandas as pd
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
    Результат (возвращается и затем) будет выводиться в консоль.
    :param data:
    :return: Float
    """
    # print(data)
    return data['Close'].mean()


def notify_if_strong_fluctuations(data, threshold=5):
    """
    Функция, которая анализирует данные и уведомляет пользователя,
        если цена акций колебалась более чем на заданный процент за период.
    Функция вычисляет максимальное и минимальное значения цены закрытия и сравнивать разницу с заданным порогом.
        Если разница превышает порог, пользователь получает уведомление.
    :param data: DataFrame
    :param threshold: пороговый процент за период
    :return:
    """
    # Получаем из dataframe максимальную и минимальную цены (по заданию цена закрытия).
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    # Альтернативный вариант по High и Low
    # max_price = data['High'].max()
    # min_price = data['Low'].min()
    # Вычисляем процентное изменение цены (за 100% возьмем среднее из def calculate_and_display_average_price(data):)
    percentage_price_change = (max_price - min_price) / calculate_and_display_average_price(data) * 100
    # Проверяем, если процентное изменение цены больше заданного порога.
    if percentage_price_change > threshold:
        print(f'Произошли сильные колебания по цене: {percentage_price_change:.2f} %.\n'
              f'\tМинимальная цена: {min_price:.2f} USD. Максимальная цена: {max_price:.2f} USD.')
    # print((max_price + min_price) / 2)
    # print(data['Close'].mean())


def export_data_to_csv(data, filename):
    """
    Сохранить загруженные данные об акциях в CSV файл.
    :param data: DataFrame
    :param filename: имя файла
    :return:
    """
    try:
        data.to_csv(filename, index=False)
    except Exception as e:
        print(f'Не удалось экспортировать данные в CSV. Ошибка: {e}')


# В модуль data_download.py добавлена функция (15) calculate_rsi(data):
def calculate_rsi(data, period=12):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


if __name__ == "__main__":
    # Пример использования
    # Загрузите данные в DataFrame
    # df = pd.read_csv('your_data.csv')  # Замените на ваш файл

    # Пример данных (замените на свои)
    data = {
        'Close': [46, 47, 45, 48, 49, 50, 52, 51, 53, 54, 53, 52, 50, 51, 52]
    }
    df = pd.DataFrame(data)

    # Рассчитайте RSI
    df['RSI'] = calculate_rsi(df)

    print(df)
