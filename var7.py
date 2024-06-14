# 7. Найти средний возраст пассажиров по каждому классу обслуживания (поле
# Pclass, указав количество братьев, сестер... (столбец SibSp): [0, ..., 8])
import matplotlib.pyplot as plt
import streamlit as st


# Функция, которая вычисляет средний возраст пассажиров
# каждого класса на основе данных из файла
def calculate_average_age(lines, consider_family_size=False, family_size=None):
    ages = {1: [], 2: [], 3: []}

    for line in lines:
        data = line.strip().split(',')
        try:
            age = float(data[6])
            pclass = int(data[2])
            sibsp = int(data[7])
        except (ValueError, IndexError):
            continue

        if not consider_family_size or sibsp == family_size:
            ages[pclass].append(age)

    averages = {
        pclass: (sum(age_list) / len(age_list)) if age_list else 0
        for pclass, age_list in ages.items()
    }

    return averages[1], averages[2], averages[3]


def var7_main():
    with open('data.csv') as file:
        lines = file.readlines()

    # Визуализируем решение
    st.write(
        '**Средний возраст пассажиров парохода «Титаник» '
        'по каждому классу обслуживания в зависимости '
        'от количества родственников (братьев, сестер, '
        'сводных братьев, сводных сестер, супругов на борту).**'
    )
    class_service = ['1 класс', '2 класс', '3 класс']
    selected_family_size = st.number_input(
        'Для просмотра данных выберите значение поля SibSp:', 0, 8
    )
    family_size_options = st.checkbox('Без учета родственников')

    # Заполняем таблицу и строим график
    # в зависимости от выбора family_size_options
    if family_size_options:
        class1_avg, class2_avg, class3_avg = calculate_average_age(lines)
        st.dataframe({'Класс обслуживания': class_service,
                      'Средний возраст': [class1_avg, class2_avg, class3_avg]})
        plt.figure(figsize=(10, 3))
        plt.bar(class_service, [class1_avg, class2_avg, class3_avg])
        plt.ylabel('Средний возраст')
        plt.title('Средний возраст пассажиров по классам обслуживания',
                  fontsize=12)
        st.pyplot(plt)
    else:
        if selected_family_size == 'Без учета родственников':
            class1_avg, class2_avg, class3_avg = calculate_average_age(lines)
            st.dataframe({'Класс обслуживания': class_service,
                          'Средний возраст': [class1_avg,
                                              class2_avg,
                                              class3_avg]})
        else:
            family_size = int(selected_family_size)
            class1_avg, class2_avg, class3_avg = calculate_average_age(
                lines, consider_family_size=True, family_size=family_size
                )
            st.dataframe({'Класс обслуживания': class_service,
                          'Средний возраст': [class1_avg,
                                              class2_avg,
                                              class3_avg]})

        plt.figure(figsize=(10, 3))
        plt.bar(class_service, [class1_avg, class2_avg, class3_avg])
        plt.ylabel('Средний возраст')
        if selected_family_size == '1':
            plt.title(
                f'Средний возраст пассажиров по классам обслуживания для '
                f'{selected_family_size} родственника'
            )
        else:
            plt.title(
                f'Средний возраст пассажиров по классам обслуживания для '
                f'{selected_family_size} родственников'
            )
        st.pyplot(plt)
