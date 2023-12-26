#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    double A[N];

    for (int i = 0 ; i < N ; i++)
    {
        cin >> A[i];
    }

    double max_sum_with_last = A[0];
    double max_sum = A[0];

    for (int idx = 1 ; idx < N ; idx++)
    {
        max_sum_with_last = max((double)0, max_sum_with_last) + A[idx];
        max_sum = max(max_sum, max_sum_with_last);
    }

    cout << max_sum;
}