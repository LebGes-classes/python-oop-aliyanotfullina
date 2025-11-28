class Bachelor:
    """Класс для описания бакалавра."""

    def __init__(self, last_name: str = "NA", specialty: str = "NA", course: int = None) -> None:
        """Инициализация/конструктор класса.

        Args:
            last_name: Фамилия бакалавра.
            specialty: Специальность.
            course: Курс (от 1 до 4).
        """

        self.__last_name = last_name
        self.__specialty = specialty
        self.__course = course
        self.__grades = {}  # Словарь для хранения оценок по предметам
        self.__attendance = 0  # Процент посещаемости

    def set_last_name(self, last_name: str) -> None:
        """Сеттер для фамилии бакалавра.

        Args:
            last_name: Фамилия бакалавра.
        """

        self.__last_name = last_name

    def get_last_name(self) -> str:
        """Геттер для фамилии бакалавра.

        Returns:
            last_name: Фамилия бакалавра
        """

        return self.__last_name

    def set_specialty(self, specialty: str) -> None:
        """Сеттер для специальности.

        Args:
            specialty: Специальность.
        """

        self.__specialty = specialty

    def get_specialty(self) -> str:
        """Геттер для специальности.

        Returns:
            specialty: Специальность.
        """

        return self.__specialty

    def set_course(self, course: int) -> None:
        """Сеттер для курса.

        Args:
            course: Курс бакалавра.
        """

        while course < 1 or course > 4:
            course = int(input('Введите корректный курс (от 1 до 4): '))

        self.__course = course

    def get_course(self) -> int:
        """Геттер для курса.

        Returns:
            course: Курс бакалавра.
        """

        return self.__course

    def print_info(self) -> None:
        """Вывод информации о бакалавре."""

        print(
            f'\nФамилия бакалавра: {self.get_last_name()}\n'
            f'Специальность: {self.get_specialty()}\n'
            f'Курс: {self.get_course()}\n'
            f'Статус: {self.get_study_status()}\n'
            f'Средний балл: {self.calculate_average_grade():.2f}\n'
            f'Посещаемость: {self.get_attendance()}%\n'
        )

    def get_study_status(self) -> str:
        """Метод для получения статуса обучения.

        Returns:
            Статус обучения в зависимости от курса.
        """

        course = self.get_course()
        if course == 1:
            return "Первокурсник"
        elif course == 2:
            return "Второкурсник"
        elif course == 3:
            return "Третьекурсник"
        elif course == 4:
            return "Выпускник"
        else:
            return "Неопределенный статус"

    def transfer_to_next_course(self) -> int:
        """Метод для перевода на следующий курс.

        Returns:
            Новый курс или текущий, если уже 4 курс.
        """

        if self.__course < 4:
            self.__course += 1
            print(f"Студент переведен на {self.__course} курс")
        else:
            print("Студент уже на выпускном курсе!")

        return self.__course

    # ДОПОЛНИТЕЛЬНЫЕ МЕТОДЫ:

    def add_grade(self, subject: str, grade: int) -> None:
        """Метод для добавления оценки по предмету.

        Args:
            subject: Название предмета.
            grade: Оценка (от 2 до 5).
        """

        if 2 <= grade <= 5:
            self.__grades[subject] = grade
            print(f"Оценка {grade} по предмету '{subject}' добавлена.")
        else:
            print("Оценка должна быть в диапазоне от 2 до 5.")

    def get_grades(self) -> dict:
        """Метод для получения всех оценок.

        Returns:
            Словарь с оценками по предметам.
        """

        return self.__grades

    def calculate_average_grade(self) -> float:
        """Метод для расчета среднего балла.

        Returns:
            Средний балл студента.
        """

        if not self.__grades:
            return 0.0

        total = sum(self.__grades.values())
        return total / len(self.__grades)

    def set_attendance(self, attendance: int) -> None:
        """Метод для установки посещаемости.

        Args:
            attendance: Процент посещаемости (0-100).
        """

        if 0 <= attendance <= 100:
            self.__attendance = attendance
        else:
            print("Посещаемость должна быть в диапазоне от 0 до 100%.")

    def get_attendance(self) -> int:
        """Метод для получения посещаемости.

        Returns:
            Процент посещаемости.
        """

        return self.__attendance

    def is_excellent_student(self) -> bool:
        """Метод для проверки, является ли студент отличником.

        Returns:
            True если средний балл >= 4.5 и посещаемость >= 80%.
        """

        return self.calculate_average_grade() >= 4.5 and self.__attendance >= 80

    def get_academic_performance(self) -> str:
        """Метод для получения академической успеваемости.

        Returns:
            Строка с оценкой успеваемости.
        """

        avg_grade = self.calculate_average_grade()
        if avg_grade >= 4.5:
            return "Отличная"
        elif avg_grade >= 3.5:
            return "Хорошая"
        elif avg_grade >= 3.0:
            return "Удовлетворительная"
        else:
            return "Неудовлетворительная"