import streamlit as st
from var2 import var2_main
from var3 import var3_main
from var7 import var7_main
from var9 import var9_main
# from var12 import var12_main
from var16 import var16_main

st.image('titaniс.jpg')
st.title('Анализ данных пассажиров парахода «Титаник»')
task_option = ['Вариант №2',
               'Вариант №3',
               'Вариант №7',
               'Вариант №9',
               'Вариант №12',
               'Вариант №16']
choice_task_option = st.selectbox('**Выберите вариант задания команды №3:**',
                                  [''] + task_option)

if choice_task_option == '':
    st.warning('Вы не выбрали вариант из списка!')
elif choice_task_option == 'Вариант №2':
    var2_main()
elif choice_task_option == 'Вариант №3':
    var3_main()
elif choice_task_option == 'Вариант №7':
    var7_main()
elif choice_task_option == 'Вариант №9':
    var9_main()
# elif choice_task_option == 'Вариант №12':
#     var12_main()
elif choice_task_option == 'Вариант №16':
    var16_main()
else:
    st.error(f'"{choice_task_option}" не реализован, пожалуйста, '
             f'выберите другой вариант из списка.')
