#include <stdint.h>
#include <stdio.h>

#include "generated.c"

#define IN_INT int32_t
#define OUT_INT int32_t

void print_nums(OUT_INT *nums)
{
	printf("[ ");
	for (int i = 0; i < 14; i++)
	{
		if (i)
			printf(" ");
		printf("%d", nums[i]);
	}
	printf(" ]\n");
}

int main()
{

	OUT_INT nums[14] = {9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9};
	// OUT_INT nums[14] = {9, 4, 2, 3, 3, 5, 6, 5, 7, 9, 8, 7, 8, 7};
	OUT_INT largest[14] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	OUT_INT regs[4];
	int running = 1;
	int li = 0;

	while (running)
	{

		if (++li > 10000000)
		{
			printf("AT ");
			print_nums(nums);
			li = 0;
		}

		code(nums, regs);
		if (regs[3] == 0)
		{
			printf("FOUND ");
			print_nums(nums);
			for (int i = 0; i < 14; ++i)
			{
				largest[i] = nums[i];
			}
		}

		for (int i = 13; i >= 0; --i)
		{
			if (nums[i] > 1)
			{
				--nums[i];
				break;
			}
			nums[i] = 9;
			if (i == 0)
			{
				running = 0;
			}
		}
	}

	printf("LARGEST ");
	print_nums(largest);
}
