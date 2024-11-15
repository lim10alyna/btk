#include <iostream>
#include <string>

using namespace std;

// Person sınıfı tanımlanıyor
class Person {
protected:
    string name;
    int age;

public:
    Person(string name, int age) {
        this->name = name;
        this->age = age;
    }

    virtual void displayInfo() {
        cout << "Ad: " << name << ", Yaş: " << age << endl;
    }
};

// Student sınıfı tanımlanıyor (Person'dan miras alıyor)
class Student : public Person {
private:
    string studentID;

public:
    Student(string name, int age, string studentID) : Person(name, age) {
        this->studentID = studentID;
    }

    void displayInfo() override {
        cout << "Ad: " << name << ", Yaş: " << age << ", Öğrenci Numarası: " << studentID << endl;
    }
};

// Teacher sınıfı tanımlanıyor (Person'dan miras alıyor)
class Teacher : public Person {
private:
    string subject;

public:
    Teacher(string name, int age, string subject) : Person(name, age) {
        this->subject = subject;
    }

    void displayInfo() override {
        cout << "Ad: " << name << ", Yaş: " << age << ", Öğretilen Ders: " << subject << endl;
    }
};

int main() {
    // Öğrenci ve öğretmen nesneleri oluşturuluyor
    Student student("Ali", 20, "S12345");
    Teacher teacher("Ayşe", 35, "Matematik");

    // Bilgiler ekrana yazdırılıyor
    student.displayInfo();
    teacher.displayInfo();

    return 0;
}
