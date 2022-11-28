#include <iostream>
using namespace std;

void perm(string s, const int first, const int last)
{   
    if (first == last) 
        cout<< s << endl;
    
    else
    {
        for (int i = first; i <= last; i++) {
        
            swap(s[first], s[i]);
            perm(s, first+1, last);
            swap(s[first], s[i]);
        }
    }
}

int main()
{
    string str;
    int first = 0;
    int last;

    cout << "=======(( Start ))=======" << endl;
    cout << "> Enter your Array : ";
    cin >> str;

    last = str.length() -1;
    
    perm(str, first, last);

    cout << "=======(( Done )=======";
    return 0;
}
