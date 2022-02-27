'''int main()
{
  string name, surname;
  int n, x, y, z;
  cin >> n;
  vector<pair<pair<int,int>, string>> students;

  for (int i = 0; i < n; i++)
  {
    cin >> name >> surname >> x >> y >> z;
    students.push_back({{-(x + y + z),i}, name + " " + surname});
  }
  sort(students.begin(), students.end());

  for (auto a : students)
    cout << a.second << endl;

  return 0;
}'''

a = [1, 3, 5, 7, 9, 16]
b =[2, 4, 8, 1, 6, 15]


for i in b:
    L = -1
    R = len(a)
    while R - L > 1:
        M = (R + L) // 2
        if a[M] <= i:
            L = M
        else:
            R = M

    if abs(a[L] - i) <= abs(a[R] - i):
        print(a[L])
    else:
        print(a[R])

