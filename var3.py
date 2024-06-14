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


def convert_to_percentages(info):
    total_passengers = sum(info.values())
    if total_passengers > 0:
        percentages = (
            {key: round(value / total_passengers  *  100, 2)
             for key, value in info.items()}
        )
        return percentages
    else:
        return None


def main():
    with open('data.csv') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]

    st.write(
        'Подсчитать количество мужчин и количество женщин, '
        'указав спасен/погиб и число или %.'
    )
    selected_value = st.selectbox('Значение поля выжившие:',
                                  ['Всего',
                                   'Выживших (1)',
                                   'Погибших (0)'])
    selected_percent = st.checkbox('Процент от общего количества пассажиров')

    info = passenger(lines, selected_value)
    converted_info = convert_to_percentages(info)

    fig = plt.figure(figsize=(10, 3))
    if selected_percent and converted_info is not None:
        plt.bar(['мужчин', 'женщин'],[converted_info['мужчин'], converted_info['женщин']])
        plt.ylabel('процент')
        st.dataframe(converted_info)
    elif not selected_percent:
        plt.bar(['мужчин', 'женщин'], [info['мужчин'], info['женщин']])
        plt.ylabel('количество')
        st.dataframe(info)
    plt.xlabel('Пассажиры')
    plt.title('Количество мужчин и женщин')
    st.pyplot(fig)
