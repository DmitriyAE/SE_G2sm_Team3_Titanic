import streamlit as st
import matplotlib.pyplot as plt


def count_passengers(lines, embarked='None'):
    a_1 = sum(1 for line in lines if line.split(',')[1] ==
              '0' and line.split(',')[12].strip() == embarked)
    a_0 = sum(1 for line in lines if line.split(',')[1] ==
              '1' and line.split(',')[12].strip() == embarked)
    return a_1, a_0


def var2_main():
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    st.subheader('Подсчитать число спасенных и погибших '
                 'для указанного пункта посадки.')

    selected_port = st.selectbox('Пункт посадки:', ['выбрать', 'Шербур',
                                 'Квинстаун', 'Саутгемптон'])

    if selected_port != 'выбрать':
        port_codes = {'Шербур': 'C', 'Квинстаун': 'Q', 'Саутгемптон': 'S'}
        a_0, a_1 = count_passengers(lines, port_codes.get(selected_port, ''))
        values = [a_0, a_1]
        labels = ["Погибшие", "Спасенные"]

        st.write(f"Количество пассажиров, спасенных "
                 f"и погибших для порта {selected_port}:")
        st.table({'Пассажиры': labels, 'Количество': values})

        fig, ax = plt.subplots()
        ax.pie(values, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.legend(labels, loc='center left', title='Статистика по портам в %',
                  bbox_to_anchor=(1, 0.5))
        st.pyplot(fig)
