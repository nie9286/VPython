#include <stdio.h>

struct SomeStructure {
	int i;
	char c;
	char* s;
};

double __declspec(dllexport) someFunction(struct SomeStructure* s)
{
	printf("int si %d, char is %c, string is %s\n", s->i, s->c, s->s);
	s->s = (char*)"goodbye";
	return 42;
}