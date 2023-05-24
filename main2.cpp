#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Student {
    int id;
    float grade;
};

void input(vector<Student>& students);
void printAll(vector<Student>& students);
Student findHighestGrade(vector<Student>& students);
Student findLowestGrade(vector<Student>& students);
void printHighestGrade(Student highest);
void printLowestGrade(Student lowest);

int main() {
    vector<Student> students;
    int option = 0;
    do {
        cout << "......Point Management System...." << endl;
        cout << "\t1. Input" << endl;
        cout << "\t2. Print all" << endl;
        cout << "\t3. Print Highest grades" << endl;
        cout << "\t4. Print Lowest grades" << endl;
        cout << "\t5. Exit" << endl;
        cout << "Choose an option: ";
        cin >> option;
        switch (option) {
            case 1:
                input(students);
                break;
            case 2:
                printAll(students);
                break;
            case 3:
                printHighestGrade(findHighestGrade(students));
                break;
            case 4:
                printLowestGrade(findLowestGrade(students));
                break;
            case 5:
                break;
            default:
                cout << "Invalid! Please try again!" << endl;
                break;
        }
    } while (option != 5);
    return 0;
}

void input(vector<Student>& students) {
    Student s;
    cout << "Enter student ID: ";
    cin >> s.id;
    cout << "Enter student grade: ";
    cin >> s.grade;
    students.push_back(s);
}

void printAll(vector<Student>& students) {
    for (int i = 0; i < students.size(); i++) {
        cout << "Student #" << i+1 << endl;
        cout << "\tID: " << students[i].id << endl;
        cout << "\tGrade: " << students[i].grade << endl;
    }
}

Student findHighestGrade(vector<Student>& students) {
    Student highest = students[0];
    for (int i = 1; i < students.size(); i++) {
        if (students[i].grade > highest.grade) {
            highest = students[i];
        }
    }
    return highest;
}

Student findLowestGrade(vector<Student>& students) {
    Student lowest = students[0];
    for (int i = 1; i < students.size(); i++) {
        if (students[i].grade < lowest.grade) {
            lowest = students[i];
        }
    }
    return lowest;
}

void printHighestGrade(Student highest) {
    cout << "The student with the highest grade is: " << endl;
    cout << "\tID: " << highest.id << endl;
    cout << "\tGrade: " << highest.grade << endl;
}

void printLowestGrade(Student lowest) {
    cout << "The student with the lowest grade is: " << endl;
    cout << "\tID: " << lowest.id << endl;
    cout << "\tGrade: " << lowest.grade << endl;
}