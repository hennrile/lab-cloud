#include <stdio.h>
#include <stdlib.h>
#define MAX 50

void input(int *n, int IDs[MAX], float grades[MAX]);
void printAll(int n, int IDs[MAX], float grades[MAX]);
float findHighestGrade(int n, int IDs[MAX], float grades[MAX]);
float findLowestGrade(int n, int IDs[MAX], float grades[MAX]);
void printHighestGrade(int n, int IDs[MAX], float grades[MAX]);
void printLowestGrade(int n, int IDs[MAX], float grades[MAX]);
void printMenu();
int main()
{
    int n = 0;
    int IDs[MAX];
    float grades[MAX];
    int option = 0;
    do
    {
        printMenu();
        scanf("%d", &option);
        switch (option)
        {
            case 1:
                input(&n, IDs, grades);
            case 2:
                printAll(n, IDs, grades);
            case 3:
                printHighestGrade(n, IDs, grades);
            case 4:
                printLowestGrade(n, IDs, grades);
            case 5:
                break;
            default:
                printf("\nInvalid! Please try again!\n");
                break;
        }
    } while (option != 5);
}
void printMenu()
{
    system("cls");
    printf("......Point Management System....\n");
    printf("\t1. Input\n");
    printf("\t2. Print all\n");
    printf("\t3. Print Highest grades\n");
    printf("\t4. Print Lowest grades\n");
    printf("\t5. Exit\n");
    printf("Choose an option: ");
}

void input(int *n, int IDs[MAX], float grades[MAX])
{
    printf("\nInput student ID: ");
    scanf("%d", &IDs[*n]);
    printf("\nInput student grade: ");
    scanf("%f", &grades[*n]);
    (*n)++;
}

void printAll(int n, int IDs[MAX], float grades[MAX])
{
    system("cls");
    for (int i = 0; i < n; i++)
    {
        printf("\nThe student's informations #%d: \n", i+1);
        printf("\t + ID: %d\n", IDs[i]);
        printf("\t + Grade: %.2f\n", grades[i]);
    }
    printf("\nPress any key to back menu: ");
    getchar(); getchar();
}

float findHighestGrade(int n, int IDs[MAX], float grades[MAX])
{
    float maxGrade = grades[0];
    for (int i = 0; i < n; i++)
    {
        if (maxGrade < grades[i]) maxGrade = grades[i];
    }
    return maxGrade;
}

float findLowestGrade(int n, int IDs[MAX], float grades[MAX])
{
    float minGrade = grades[0];
    for (int i = 0; i < n; i++)
    {
        if (minGrade > grades[i]) minGrade = grades[i];
    }
    return minGrade;
}

void printHighestGrade(int n, int IDs[MAX], float grades[MAX])
{
    float highest = findHighestGrade(n, IDs, grades);
    float grade;
    system("cls");
    printf("    Student have highest grade is:    \n");
    for (int i = 0; i < n; i++)
    {
        grade = grades[i];
        if (grades[i] == highest)
        {
            printf("\t + ID: %d\n", IDs[i]);
            printf("\t + Grade: %.2f\n", grades[i]);
        }
    }
    printf("\nPress any key to back menu: ");
    getchar(); getchar();
}

void printLowestGrade(int n, int IDs[MAX], float grades[MAX])
{
    float lowest = findLowestGrade(n, IDs, grades);
    float grade;
    system("cls");
    printf("    Student have lowest grade is:    \n");
    for (int i = 0; i < n; i++)
    {
        grade = grades[i];
        if (grades[i] == lowest)
        {
            printf("\t + ID: %d\n", IDs[i]);
            printf("\t + Grade: %.2f\n", grades[i]);
        }
    }
    printf("\nPress any key to back menu: ");
    getchar(); getchar();
}

void menu()
{
    printf("1. Input: \n");
    printf("2. Print All: \n");
    printf("3. Print Highest Grade: \n");
    printf("4. Print Lowest Grade: \n");
    printf("5. Exit: \n");
}

