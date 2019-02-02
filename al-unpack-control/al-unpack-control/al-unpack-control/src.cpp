#include <iostream>
#include <windows.h>
#include <direct.h> 
using namespace std;

int main(int argc, char * argv[])
{	
	string cwd = _getcwd(NULL, 0);
	string cmd = "\\Python37-32\\python.exe main";
	cmd = cwd + cmd;
	for (int i = 1; i < argc; i++)
	{
		cmd += " ";
		cmd += argv[i];
	}
	const char *cmd_c_str = cmd.c_str();
	cout << cmd_c_str<<endl;
	system(cmd_c_str);
	//system("pause");
	return 0;
}