#include <iostream>
using namespace std;

int addTwoNumbers(int A, int B) {
    return A + B;
}

int main() {
    int A = 15, B = 5;
    cout << "Sum = " << addTwoNumbers(A, B);
    return 0;
}
