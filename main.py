import streamlit as st
from var2 import var2_main
from var3 import var3_main
from var7 import var7_main
from var9 import var9_main
# from var12 import var12_main
from var16 import var16_main

st.image('titaniс.jpg')
st.subheader('Анализ данных пассажиров парахода «Титаник»')

task_options = {
    'Вариант №2': var2_main,
    'Вариант №3': var3_main,
    'Вариант №7': var7_main,
    'Вариант №9': var9_main,
    # 'Вариант №12': var12_main,
    'Вариант №16': var16_main
}

task_list = [''] + list(task_options.keys())
choice_task_option = st.selectbox(
    'Выберите вариант задания команды №3:', task_list
)

if choice_task_option == '':
    st.warning('Вы не выбрали вариант из списка!')
elif choice_task_option in task_options:
    task_options[choice_task_option]()
