#include <iostream>
#include <climits>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cstdio>
#include <windows.h>
#include <locale.h>

using namespace std;

// Задание 1
void task1() {
    const int size = 10;
    int* arr = new int[size] { 5, 2, 8, 1, 9, 3, 7, 4, 6, 0 };

    int min_val = INT_MAX;
    int max_val = INT_MIN;

    for (int i = 0; i < size; i++) {
        if (arr[i] < min_val) min_val = arr[i];
        if (arr[i] > max_val) max_val = arr[i];
    }

    cout << "minimum things: " << min_val << endl;
    cout << "maksimum things: " << max_val << endl;
    cout << "differents: " << max_val - min_val << endl;

    delete[] arr;
}

// Задание 2
void task2() {
    srand(time(NULL));

    const int size = 10;
    int* arr = new int[size];

    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 100 - 50;
    }

    cout << "massiv: ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    delete[] arr;
}

// Задание 3
void task3() {
    int size;

    cout << "size of: ";
    cin >> size;

    int* arr = new int[size];

    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    delete[] arr;
}

// Задание 4
void task4() {
    const int rows = 4;
    const int cols = 4;

    int** matrix = new int* [rows];
    for (int i = 0; i < rows; i++) {
        matrix[i] = new int[cols];
    }

    int value = 1;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = value++;
        }
    }

    cout << "Matrix:" << endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }

    cout << "\nSumma po stolbcam:" << endl;
    for (int j = 0; j < cols; j++) {
        int col_sum = 0;
        for (int i = 0; i < rows; i++) {
            col_sum += matrix[i][j];
        }
        cout << "Stolbec " << j + 1 << ": " << col_sum << endl;
    }

    for (int i = 0; i < rows; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
}

// Задание 5
struct Student {
    char famil[20];
    char name[20];
    char facult[20];
    int Nomzach;
};

void printStudents(Student* students, int num) {
    cout << "\nList of students:" << endl;
    cout << "==============================================" << endl;
    cout << "№  Surname      Name          facultet    Zachetka" << endl;
    cout << "--------------------------------------------------------------" << endl;
    for (int i = 0; i < num; i++) {
        printf("%-2d %-12s %-12s %-12s %-10d\n",
            i + 1, students[i].famil, students[i].name,
            students[i].facult, students[i].Nomzach);
    }
    cout << "==============================================" << endl;
}

void swapStudents(Student* s1, Student* s2) {
    Student temp = *s1;
    *s1 = *s2;
    *s2 = temp;
}

void reorderStudents(Student* students, int num) {
    int index1, index2;

    cout << "\nPoyadok studentov:" << endl;
    printStudents(students, num);

    cout << "Enter numbers of students (to 1 to " << num << "):" << endl;
    cout << "First student: ";
    cin >> index1;
    cout << "Second student: ";
    cin >> index2;

    if (index1 < 1 || index1 > num || index2 < 1 || index2 > num) {
        cout << "False numbers of students!" << endl;
        return;
    }

    if (index1 == index2) {
        cout << "It's a same student!" << endl;
        return;
    }

    swapStudents(&students[index1 - 1], &students[index2 - 1]);

    cout << "\nStudent pomenalis mestami!" << endl;
    cout << "New List:" << endl;
    printStudents(students, num);
}

void searchStudent(Student* students, int num) {
    char search[20];
    int searchType;

    cout << "\nChoice pole for search:" << endl;
    cout << "1 - Po fami" << endl;
    cout << "2 - Po imeni" << endl;
    cout << "3 - Po facultetu" << endl;
    cout << "4 - Po omeru zachetki" << endl;
    cout << "Ваш выбор: ";
    cin >> searchType;

    cout << "Enter znachenie poiska: ";
    cin >> search;

    bool found = false;

    cout << "\nPeruslt of search:" << endl;
    cout << "==============================================" << endl;

    for (int i = 0; i < num; i++) {
        bool match = false;

        switch (searchType) {
        case 1:
            if (strcmp(students[i].famil, search) == 0) {
                match = true;
            }
            break;
        case 2:
            if (strcmp(students[i].name, search) == 0) {
                match = true;
            }
            break;
        case 3:
            if (strcmp(students[i].facult, search) == 0) {
                match = true;
            }
            break;
        case 4:
            if (students[i].Nomzach == atoi(search)) {
                match = true;
            }
            break;
        default:
            cout << "False choice!" << endl;
            return;
        }

        if (match) {
            cout << "Student №" << i + 1 << ":" << endl;
            cout << "Surname: " << students[i].famil << endl;
            cout << "Name: " << students[i].name << endl;
            cout << "Facult: " << students[i].facult << endl;
            cout << "Zachetka: " << students[i].Nomzach << endl;
            cout << "-----------------" << endl;
            found = true;
        }
    }

    if (!found) {
        cout << "Student not found" << endl;
    }
}

void studentManagementMenu(Student* students, int num) {
    int choice;

    do {
        cout << "\n=== Menu ===" << endl;
        cout << "1 - Show all students" << endl;
        cout << "2 - Search students" << endl;
        cout << "3 - Pomenyat mestami" << endl;
        cout << "0 - exit" << endl;
        cout << "Your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            printStudents(students, num);
            break;
        case 2:
            searchStudent(students, num);
            break;
        case 3:
            reorderStudents(students, num);
            break;
        case 0:
            cout << "Exit from menu..." << endl;
            break;
        default:
            cout << "Nevernyi vibor!" << endl;
        }
    } while (choice != 0);
}

void task5() {
    const int num_students = 5;
    setlocale(LC_ALL, "Russian");

    Student* students = new Student[num_students];

    strcpy_s(students[0].famil, "Ivanov");
    strcpy_s(students[0].name, "Ivan");
    strcpy_s(students[0].facult, "FVT");
    students[0].Nomzach = 12345;

    strcpy_s(students[1].famil, "Petrov");
    strcpy_s(students[1].name, "Petr");
    strcpy_s(students[1].facult, "Math");
    students[1].Nomzach = 12346;

    strcpy_s(students[2].famil, "Sidorov");
    strcpy_s(students[2].name, "Alex");
    strcpy_s(students[2].facult, "Fizika");
    students[2].Nomzach = 12347;

    strcpy_s(students[3].famil, "Kuznetsova");
    strcpy_s(students[3].name, "Mari");
    strcpy_s(students[3].facult, "FVT");
    students[3].Nomzach = 12348;

    strcpy_s(students[4].famil, "Smirnov");
    strcpy_s(students[4].name, "Dmitriy");
    strcpy_s(students[4].facult, "Math");
    students[4].Nomzach = 12349;

    studentManagementMenu(students, num_students);

    delete[] students;
}

int main() {
    cout << "=== Task 1 ===" << endl;
    task1();

    cout << "\n=== Task 2 ===" << endl;
    task2();

    cout << "\n=== Task 3 ===" << endl;
    task3();

    cout << "\n=== Task 4 ===" << endl;
    task4();

    cout << "\n=== Task 5 ===" << endl;
    task5();

    return 0;
}