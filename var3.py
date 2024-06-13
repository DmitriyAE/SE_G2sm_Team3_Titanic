import streamlit as st
import matplotlib.pyplot as plt
import csv


def passenger(lines, selected_value):
    info = {"мужчин": 0, "женщин": 0}
    reader = csv.reader(lines)
    next(reader)
    for data in reader:
        sex = data[4]
        sur = data[1]
        if selected_value == "Всего" or (selected_value == "Выживших (1)" and sur == '1') or (
                (selected_value == "Погибших (0)" and sur == '0')
        ):
            if sex == 'female':
                info['женщин'] += 1
            elif sex == 'male':
                info['мужчин'] += 1
    return info


def var3_main():
    with open('data.csv') as file:
        lines = file.readlines()

    st.subheader(
        'Подсчитать количество мужчин и количество женщин, '
        'указав спасен/погиб и число или %.'
    )
    selected_value = st.selectbox('Значение поля выжившие:',
                                  ['Всего',
                                   'Выживших (1)',
                                   'Погибших (0)'])
    selected_percent = st.checkbox('Процент от общего количества пассажиров')

    info = passenger(lines, selected_value)

    fig = plt.figure(figsize=(7, 4))
    if selected_percent:
        total_passengers = info["мужчин"] + info["женщин"]
        if total_passengers > 0:
            info = {"мужчин":
                    round(info["мужчин"] / total_passengers * 100, 2),
                    "женщин":
                    round(info["женщин"] / total_passengers * 100, 2)}
        plt.bar(['мужчин', 'женщин'], [info["мужчин"], info["женщин"]])
        plt.ylabel('процент')
        st.dataframe(info)
    else:
        plt.bar(['мужчин', 'женщин'], [info["мужчин"], info["женщин"]])
        plt.ylabel('количество')
        st.dataframe(info)
    plt.xlabel('Пассажиры')
    plt.title('Количество мужчин и женщин')
    st.pyplot(fig)
