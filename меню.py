from Bachelor import (
    Bachelor,
)


class Menu:
    """Класс для работы пользовательского меню."""

    def print_main_menu(self) -> None:
        """Вывод пунктов главного пользовательского меню."""

        print(
            '\n1: Печать информации о бакалавре.\n'
            '2: Изменить фамилию.\n'
            '3: Изменить специальность.\n'
            '4: Изменить курс.\n'
            '5: Получить информацию о фамилии.\n'
            '6: Получить информацию о специальности.\n'
            '7: Получить информацию о курсе.\n'
            '8: Получить статус обучения.\n'
            '9: Перевести на следующий курс.\n'
            '10: Добавить оценку по предмету.\n'
            '11: Показать все оценки.\n'
            '12: Показать средний балл.\n'
            '13: Установить посещаемость.\n'
            '14: Проверить, является ли отличником.\n'
            '15: Получить оценку успеваемости.\n'
            '0: ВЫХОД ИЗ ПРОГРАММЫ!\n'
        )

    def main_menu(self, choice: int, bachelor: Bachelor) -> bool:
        """Главное пользовательское меню.

        Args:
            choice: Выбор пользователя.
            bachelor: Объект бакалавра для работы.

        Returns:
            is_running: Продолжается ли работа программы.
        """

        is_running = True

        match choice:
            case 0:
                is_running = False
            case 1:
                bachelor.print_info()
            case 2:
                last_name = input('Введите фамилию бакалавра: ')
                bachelor.set_last_name(last_name)
            case 3:
                specialty = input('Введите специальность: ')
                bachelor.set_specialty(specialty)
            case 4:
                course = int(input('Введите курс (от 1 до 4): '))
                bachelor.set_course(course)
            case 5:
                print(bachelor.get_last_name())
            case 6:
                print(bachelor.get_specialty())
            case 7:
                print(bachelor.get_course())
            case 8:
                print(f'Статус обучения: {bachelor.get_study_status()}')
            case 9:
                bachelor.transfer_to_next_course()
            case 10:
                subject = input('Введите название предмета: ')
                grade = int(input('Введите оценку (2-5): '))
                bachelor.add_grade(subject, grade)
            case 11:
                grades = bachelor.get_grades()
                if grades:
                    print("Оценки студента:")
                    for subject, grade in grades.items():
                        print(f"  {subject}: {grade}")
                else:
                    print("Оценок пока нет.")
            case 12:
                print(f"Средний балл: {bachelor.calculate_average_grade():.2f}")
            case 13:
                attendance = int(input('Введите процент посещаемости (0-100): '))
                bachelor.set_attendance(attendance)
            case 14:
                if bachelor.is_excellent_student():
                    print("Студент является отличником!")
                else:
                    print("Студент не является отличником.")
            case 15:
                print(f"Успеваемость: {bachelor.get_academic_performance()}")

        return is_running