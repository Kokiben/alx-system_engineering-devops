#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creats infinite loop
 * Return: 0
 */
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 * zom - Creats zombie
 * Return: 0
 */
int zom(void)
{
int j;
pil_t zob;

for (j = 0; j < 5; j++)
{
zob = fork();
if (!zob)
return (0);
printf("Zombie process created, PID: %d\n", zob);
}

infinite_while();
return (0);
}
