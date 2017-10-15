#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// functions used to comunicate with the interactor (the other program)
// use this to get the position of the other player.
// after using it you must do your own move
// TL;DR GetEdge() GetEdge() is invalid
pair<int, int> GetEdge() {
    int a, b; 
    cin >> a >> b;
    return {a, b};
}

// use this to set your answer
void SetAnswer(int s) {
    cout << s << endl;
    if (s == 0) {
        exit(0);
    }
}

int main() {
    // use this to pass the first example
    int n; 
    cin >> n;
    GetEdge();
    SetAnswer(1);
    GetEdge();
    SetAnswer(1);
    GetEdge();
    SetAnswer(1);
    GetEdge();
    SetAnswer(0);
    return 0;
}
