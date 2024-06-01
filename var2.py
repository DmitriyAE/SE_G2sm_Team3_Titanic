import streamlit as st
import matplotlib.pyplot as plt


def count_passengers(lines,Embarked='None'):
    a_1 = 0
    a_0 = 0
    for line in lines:
        data = line.split(',')
        if data[1] == '0' and data[12].strip() == Embarked:
            a_1 += 1
        elif data[1] == '1' and data[12].strip() == Embarked:
            a_0 += 1
    return a_1, a_0


def var2_main():
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    a_0, a_1 = count_passengers(lines)

    st.subheader('Подсчитать число спасенных и погибших для указанного пункта посадки.')

    selected_port = st.selectbox('Пункт посадки:', ['выбрать', 'Шербур', 'Квинстаун', 'Саутгемптон'])

    if selected_port == 'Шербур':
        a_0, a_1, = count_passengers(lines,'C')
        values = [a_0, a_1]
        labels = ["", ""]
    elif selected_port == 'Квинстаун':
        a_0, a_1, = count_passengers(lines,'Q')
        values = [a_0, a_1]
        labels = ["", ""]
    elif selected_port == 'Саутгемптон':
        a_0, a_1, = count_passengers(lines,'S')
        values = [a_0, a_1]
        labels = ["", ""]
    else:
        values = []
        labels = []

    if selected_port != 'выбрать':
        st.write(f"Количество пассажиров, спасенных и погибших для порта {selected_port}:")
        st.table({
            "Пассажиры": ["Погибшие", "Спасенные"],
            "Количество": values
        })

    if values:
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.legend(['Погибшие', 'Спасенные'], loc='center left', title='Статистика по портам в %', bbox_to_anchor=(1, 0.5))
        st.pyplot(fig)
