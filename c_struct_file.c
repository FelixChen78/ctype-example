#include <stdio.h>
#include "c_struct_file.h"

double c_function(struct c_struct * s) 
{
    printf("int is %d, char is %c, string is %s \n", s->i, s->c, s->s);
    s->s = "goodbye";
    return 42;

}