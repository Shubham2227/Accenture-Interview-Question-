Write a program to calculate the length of a string without
using the strlen() function.



#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	int i;
	string str = "Shubham";
	for (i = 0; str[i]; i++);
	cout << i << endl;
	return 0;
}
