import streamlit as st
from matplotlib import pyplot as plt
import numpy as np


def info_ticket(x_lines, sex='None'):
    ticket_cost = {'1': 0, '2': 0, '3': 0}

    for line in x_lines:
        data = line.strip().split(',')
        try:
            cost = float(data[10])
        except (ValueError, IndexError):
            continue

        ticket_class = data[2]
        passenger_sex = data[5]

        if sex != 'None' and passenger_sex == sex:
            ticket_cost[ticket_class] += cost
        elif sex == 'None':
            ticket_cost[ticket_class] += cost

    return ticket_cost['1'], ticket_cost['2'], ticket_cost['3']


with open('data.csv') as file:
    lines = file.readlines()


def graf(vip, standard, economy):
    x = ['VIP', 'Стандарт', 'Эконом']
    arr_x = [vip, standard, economy]
    x_axis = np.arange(len(x))
    plt.figure(figsize=(10, 3))
    plt.bar(x_axis - 0.0, arr_x, 0.6)
    plt.xticks(x_axis, x)
    plt.xlabel("Билет")
    plt.ylabel("Выручка")
    plt.title("Суммарная стоимость билетов по каждому классу")
    plt.show()
    return st.pyplot(plt)


def var9_main():
    st.write("**Найти суммарную стоимость билетов пассажиров указанного пола по каждому классу обслуживания.**")
    choice = st.selectbox('Суммарная стоимость билетов по каждому классу',
                          ['Всех проданных билетов', 'Проданных для мужчин', 'Проданных для женщин'])

    if choice == 'Всех проданных билетов':
        vip, standard, economy = info_ticket(lines)
        st.dataframe({'Сумма полученная от продажи билетов': ['\"высшего(VIP)\" класса',
                                                              '\"среднего(стандартного)\" класса',
                                                              '\"низший(эконом)\" класса'],
                      'Кол-во': [round(vip, 2), round(standard, 2), round(economy, 2)]})
        graf(vip, standard, economy)

    elif choice == 'Проданных для мужчин':
        vip, standard, economy = info_ticket(lines, 'male')
        st.dataframe({'Сумма полученная от продажи билетов': ['\"высшего(VIP)\" класса',
                                                              '\"среднего(стандартного)\" класса',
                                                              '\"низший(эконом)\" класса'],
                      'Кол-во': [round(vip, 2), round(standard, 2), round(economy, 2)]})
        graf(vip, standard, economy)

    elif choice == 'Проданных для женщин':
        vip, standard, economy = info_ticket(lines, 'female')
        st.dataframe({'Сумма полученная от продажи билетов': ['\"высшего(VIP)\" класса',
                                                              '\"среднего(стандартного)\" класса',
                                                              '\"низший(эконом)\" класса'],
                      'Кол-во': [round(vip, 2), round(standard, 2), round(economy, 2)]})
        graf(vip, standard, economy)
