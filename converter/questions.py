questions = {
    'Имя ученика': {
        'options': [''],
        'answers': {
            '': ['']
        },
        'follow_up': {
            '': 'Имя родителя'
        }
    },
    'Имя родителя': {
        'options': [''],
        'answers': {
            '': ['']
        },
        'follow_up': {
            '': 'Количество посещенных занятий'
        }
    },
    'Количество посещенных занятий': {
        'options': ['Два', 'Три'],
        'answers': {
            'Два': ['имя_ученика посетил 2 занятия, '],
            'Три': ['имя_ученика посетил все три занятия наших мини-курсов. \n']
        },
        'follow_up': {
            'Два': 'Какое занятие он пропустил?',
            'Три': 'Принимал активное участие?'
        }
    },
    'Принимал активное участие?': {
        'options': ['Да', 'Нет'],
        'answers': {
            'Да': ['Он принимал активное участие на каждом уроке. \n'],
            'Нет': ['']
        },
        'follow_up': {
            'Да': 'Самый сильный в группе?',
            'Нет': 'Пользовался микрофоном?'
        }
    },
    'Какое занятие он пропустил?': {
        'options': ['Второе', 'Третье'],
        'answers': {
            'Второе': ['к сожалению, пропустив второе. '
                       'Однако, это вовсе не помешало ему довольно '
                       'быстро сориентироваться, понять материал '
                       'и начать решать задания по третьему уроку. '
                       'Это очень здорово.\n'
                       '* Я поинтересовался у него '
                       'насчет второго занятия, и он мне сообщил, что '
                       'обязательно вернется к пропущенному '
                       'уроку и выполнит его. На мой взгляд, это '
                       'говорит о том, что мини-курс ему был, '
                       'как минимум, не безразличен, но я и вовсе '
                       'надеюсь, что ему было интересно. *\n'],
            'Третье': ['к сожалению, пропустив третье, финальное. \n']
        },
        'follow_up': {
            'Второе': 'Принимал активное участие?',
            'Третье': 'Принимал активное участие?'
        }
    },
    'Самый сильный в группе?': {
        'options': ['Да', 'Нет'],
        'answers': {
            'Да': ['имя_ученика - один из самых, если не самый сильный ученик в '
                   'группе. * Я говорю такое не часто, поэтому прошу мне поверить. \n'
                   'Сама по себе группа была собрана из довольно смышленых ребят, а '
                   'имя_ученика на их фоне ещё и выделялся - молодец. * \n'],
            'Нет': ['* имя_ученика демонстрирует хороший уровень понимания основ '
                    'Python. *\n']
        },
        'follow_up': {
            'Да': 'Задавал вопросы?',
            'Нет': 'Самый активный в группе?'
        }
    },
    'Самый активный в группе?': {
        'options': ['Да', 'Нет'],
        'answers': {
            'Да': ['имя_ученика - один из самых, если не самый активный ученик '
                   'в группе. \n'
                   'Он задавал довольно большое количество вопросов и это просто '
                   'замечательно, потому что это очень важный навык - уметь '
                   'задавать правильные вопросы. \n'],
            'Нет': ['']
        },
        'follow_up': {
            'Да': 'Задавал вопросы?',
            'Нет': 'Пользовался микрофоном?'
        }
    },
    'Пользовался микрофоном?': {
        'options': ['Да', 'Нет'],
        'answers': {
            'Да': [''],
            'Нет': ['имя_ученика, к сожалению, почти не пользовался микрофоном. \n'
                    'Мы с ним нашли договоренность о том, что я буду периодически '
                    'интересоваться, как ему удаётся справляться с заданиями, '
                    'а имя_ученика будет отвечать мне письменно в чате. \n'
                    'После этого он начал сообщать мне, с какими заданиями у него '
                    'возникают трудности, мы совместно их разбирали и судя по '
                    'результатам выполнения упражнений, он с ними успешно '
                    'справлялся. \n',
                    'К сожалению, имя_ученика не пользовался микрофоном на занятиях, '
                    'но это вовсе не помешало нам продуктивно общаться '
                    'и работать. Он регулярно отправлял сообщения в чат, '
                    'задавал уточняющие вопросы и отправлял свои'
                    'предположения и правильные ответы. \n']
        },
        'follow_up': {
            'Да': 'Задавал вопросы?',
            'Нет': 'Задавал вопросы?'
        }
    },
    'Задавал вопросы?': {
        'options': ['Да', 'Нет'],
        'answers': {
            'Да': [''],
            'Нет': ['Не всегда активно задает вопросы, что может означать '
                    'недостаток понимания материала. \n']
        },
        'follow_up': {
            'Да': 'Есть, что ещё добавить о ребенке по факту?',
            'Нет': 'Упражнения'
        }
    },
    'Есть, что ещё добавить о ребенке по факту?': {
        'options': ['Да', 'Нет'],
        'answers': {
            'Да': ['имя_ученика активно отвечал на заданные мной вопросы и принимал '
                   'участие в обсуждении наших проектов. \n Непонятные для '
                   'него моменты он уточнял у меня, и впоследствии ему '
                   'удавалось справляться со всеми трудностями. \n'],
            'Нет': ['имя_ученика в течении занятия никогда не стеснялся задавать '
                    'вопросы. Задавать правильные вопросы - это '
                    'очень важный навык, вы сами прекрасно понимаете. '
                    'Особенно в рамках мини-курса, когда имеется ограниченное '
                    'количество времени. \n'
                    'В результате, мы совместно находили правильные и эффективные '
                    'решения проблемы. \n']
        },
        'follow_up': {
            'Да': 'Упражнения',
            'Нет': 'Упражнения'
        }
    },
    'Упражнения': {
        'options': ['Решил всё', 'Брал доп.', 'Брал звёздочки', 'Основные', 'Тяжело'],
        'answers': {
            'Решил всё': ['Если говорить более конкретно, оперируя показателями '
                          'выполнения упражнений, которые у преподавателей имеются, '
                          'то я могу с уверенностью сообщить, что имя_ученика очень '
                          'старался: \n'
                          'он уделил очень много внимания выполнению упражнений и '
                          'справился не только с основным курсом, но брал также '
                          'и дополнительные задания, и задания с повышенной '
                          'сложностью. Он буквально выполнил практически все '
                          'доступные упражнения. \n'],
            'Брал доп.': ['Если говорить более конкретно, оперируя показателями '
                          'выполнения упражнений, которые у преподавателей имеются, '
                          'то я могу с уверенностью сообщить, что имя_ученика очень '
                          'старался: \n'
                          'он уделил очень много внимания выполнению упражнений и '
                          'справился не только с основным курсом, но брал также '
                          'и дополнительные задания, которые он также '
                          'успешно выполнял. \n'],
            'Брал звёздочки': ['Если говорить более конкретно, оперируя показателями '
                               'выполнения упражнений, которые у преподавателей '
                               'имеются, то я могу с уверенностью сообщить, '
                               'что имя_ученика очень старался: \n'
                               'он довольно много времени уделил выполнению заданий и '
                               'это, разумеется, дало свои плоды. Он успешно выполнил '
                               'не только основную программу, но брался и за '
                               'дополнительные задания и упражнения с повышенной '
                               'сложностью. \n'],

            'Основные': ['Если говорить более конкретно, оперируя показателями '
                         'выполнения упражнений, которые у преподавателей имеются, '
                         'то я могу с уверенностью сообщить, что имя_ученика очень '
                         'старался: \n'
                         'Он провел довольно продолжительное время за решением '
                         'упражнений и всю основную программу выполнил '
                         'практически без ошибок. Некоторые задачи он решил '
                         'нестандартным образом, что подчёркивает то, '
                         'что у него был интерес к курсу и '
                         'материал он понял на довольно хорошем уровне. \n'],
            'Тяжело': ['']
        },
        'follow_up': {
            'Решил всё': 'Давал обратную связь?',
            'Брал доп.': 'Давал обратную связь?',
            'Брал звёздочки': 'Давал обратную связь?',
            'Основные': 'Прочел документацию?',
            'Тяжело': 'Ребенок старался или всё плохо?'
        }
    },
    'Давал обратную связь?': {
        'options': ['Да', 'Нет'],
        'answers': {
            'Да': [''],
            'Нет': ['']
        },
        'follow_up': {
            'Да': 'Идеально решает или ещё больше мотивирую?',
            'Нет': 'Выводы'
        }
    },
    'Идеально решает или ещё больше мотивирую?': {
        'options': ['Идеально', 'Мотивирую'],
        'answers': {
            'Идеально': ['Я регулярно, после каждого занятия, просматривал его решения'
                         ' и наблюдал одну и ту же картину - он решает и пишет'
                         'код именно так, как это задумывалось. Отличные решения. \n'],
            'Мотивирую': ['Я регулярно наблюдал за прогрессом в его решениях, после '
                          'каждого занятия давал ему чуть больше материала, '
                          'чтобы мотивировать его решать ещё более эффективно и '
                          'писать более качественный код. \n',
                          'Я регулярно, после каждого нашего занятия, просматривал'
                          ' то, как он справляется с упражнениями и давал '
                          'советы, как это задание выполнить ещё лучше и эффективнее, '
                          'чтобы он не останавливался на достигнутом. \n'],
        },
        'follow_up': {
            'Идеально': 'Выводы',
            'Мотивирую': 'Выводы'
        }
    },
    'Прочел документацию?': {
        'options': ['Да', 'Нет'],
        'answers': {
            'Да': ['Он также прочел документации, которые прилагаются к урокам, где '
                   'хранится вся “выжимка”, всё основное, что мы с ребятами '
                   'разбирали на уроках, что подчеркивает его интерес '
                   'к изучаемой теме. \n'],
            'Нет': ['']
        },
        'follow_up': {
            'Да': 'Выводы',
            'Нет': 'Выводы'
        }
    },
    'Ребенок старался или всё плохо?': {
        'options': ['Старался', 'Всё плохо'],
        'answers': {
            'Старался': ['имя_ученика было тяжеловато разбираться в дисциплине. '
                         'Считаю, что ему нужно чуть больше времени для того, '
                         'чтобы разобраться в материале. В рамках мини-курса '
                         'времени, к сожалению, было очень немного, '
                         'темы изучаются очень интенсивно. \n'
                         'На полноценном курсе времени будет достаточно, '
                         'преподаватель сможет найти необходимый для ребенка'
                         'ритм и темп обучения. \n'
                         'Мне понравилось работать с имя_ученика, учитывая то, '
                         'что он не сложил руки и усердно пытался понять новый '
                         'материал, я могу сделать вывод, что ему было '
                         'интересно. А если есть интерес, значит у него всё '
                         'обязательно получится. \n'],
            'Всё плохо': ['У имя_ученика не очень получалось и это абсолютно '
                          'нормально, так как программирование - это тяжело. \n'
                          'Возможно, ему нужно просто повысить уровень '
                          'общей компьютерной грамотности. У нас в алгоритмике даже '
                          'есть курс на эту тему, если будет интересно, '
                          'вы можете уточнить у наших менеджеров, '
                          'они вас сориентируют. \n']
        },
        'follow_up': {
            'Старался': None,
            'Всё плохо': None
        },
        'result': True
    },
    'Выводы': {
        'options': ['Интересно', 'Усвоил + интересно', 'Рекомендую'],
        'answers': {
            'Интересно': ['Если я не ошибаюсь в своих выводах и имя_ученика '
                          'было по-настоящему интересно, '
                          'то я бы однозначно рекомендовал ему продолжать '
                          'изучать программирование '
                          'на языке Python. \n'],
            'Усвоил + интересно': ['У меня нет никаких сомнений в том, что имя_ученика'
                                   ' замечательно усвоил материал '
                                   'и мне бы очень хотелось верить, что ему было '
                                   'по-настоящему интересно изучать Python '
                                   'и он продолжит обучение. \n'],
            'Рекомендую': ['Я однозначно рекомендую продолжать заниматься '
                           'программированием на Python. \n']
        },
        'follow_up': {
            'Интересно': None,
            'Усвоил + интересно': None,
            'Рекомендую': None
        },
        'result': True
    }
    # Добавляем вопросы сюда
}
