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


def graf(v, s, e):
    x = ['VIP', 'Стандарт', 'Эконом']
    arr_x = [v, s, e]
    x_axis = np.arange(len(x))
    plt.bar(x_axis - 0.0, arr_x, 0.6)
    plt.xticks(x_axis, x)
    plt.xlabel("Билет")
    plt.ylabel("Выручка")
    plt.title("Суммарная стоимость билетов по каждому классу")
    plt.show()
    return st.pyplot(plt)


def var9_main():
    st.subheader("Найти суммарную стоимость билетов пассажиров указанного пола по каждому классу обслуживания.")
    choice = st.selectbox('Суммарная стоимость билетов по каждому классу',
                          ['Всех проданных билетов', 'Проданных для мужчин', 'Проданных для женщин'])

    if choice == 'Всех проданных билетов':
        v, s, e = info_ticket(lines)
        st.table({'Сумма полученная от продажи билетов': ['\"высшего(VIP)\" класса',
                                                          '\"среднего(стандартного)\" класса',
                                                          '\"низший(эконом)\" класса'],
                  'Кол-во': [round(v, 2), round(s, 2), round(e, 2)]})
        graf(v, s, e)

    elif choice == 'Проданных для мужчин':
        v, s, e = info_ticket(lines, 'male')
        st.table({'Сумма полученная от продажи билетов': ['\"высшего(VIP)\" класса',
                                                          '\"среднего(стандартного)\" класса',
                                                          '\"низший(эконом)\" класса'],
                  'Кол-во': [round(v, 2), round(s, 2), round(e, 2)]})
        graf(v, s, e)

    elif choice == 'Проданных для женщин':
        v, s, e = info_ticket(lines, 'female')
        st.table({'Сумма полученная от продажи билетов': ['\"высшего(VIP)\" класса',
                                                          '\"среднего(стандартного)\" класса',
                                                          '\"низший(эконом)\" класса'],
                  'Кол-во': [round(v, 2), round(s, 2), round(e, 2)]})
        graf(v, s, e)
