import streamlit as st
import matplotlib.pyplot as plt
import csv


def count_survivors(lines, price):
    first_class_survived = 0
    second_class_survived = 0
    third_class_survived = 0

    reader = csv.reader(lines)
    next(reader)

    for parts in reader:
        try:
            fare = float(parts[9])
        except ValueError:
            continue
        if not price[0] <= fare <= price[1]:
            continue
        if parts[4] == 'female' and parts[1] == '1':
            if parts[2] == '1':
                first_class_survived += 1
            elif parts[2] == '2':
                second_class_survived += 1
            elif parts[2] == '3':
                third_class_survived += 1

    return [first_class_survived, second_class_survived, third_class_survived]


def var16_main():
    st.subheader(
        'Просмотр данных количества выживших женщин '
        'по каждому классу обслуживания, с диапазоном платы за проезд'
    )
    price = st.slider('Диапазон платы за проезд в $ 600', 0, 600, (0, 600))
    classes = ['Первый класс', 'Второй класс', 'Третий класс']

    with open("data.csv") as file:
        lines = file.readlines()

    survivors = count_survivors(lines, price)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(classes, survivors)
    ax.set_xlabel('Класс')
    ax.set_ylabel('Количество выживших женщин')
    ax.set_title('Количество выживших женщин по классам')

    st.pyplot(fig)
