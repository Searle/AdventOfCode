#include <stdbool.h>
#include <stdio.h>

#include "code_2.txt.h"

#define TASK 2

#define MAX_CMDS 256
#define MAX_NODES 256 // Assuming a maximum number of nodes

int cmd_srcs[MAX_CMDS];
long long cmd_pulses[MAX_CMDS];
long long states[MAX_NODES];

#if TASK == 1
int pulse_stats[2] = {0, 0};
#endif

#define node(inx) (nodes + (inx) * NODE_WIDTH)

bool push_button()
{
#if TASK == 1
    pulse_stats[0] += 1;
#endif

    cmd_srcs[0] = BROADCAST_INX;
    cmd_pulses[0] = 0;

    unsigned int cmd_start = 0;
    unsigned int cmd_end = 1;

    while (cmd_start != cmd_end)
    {
        int src = cmd_srcs[cmd_start];
        long long pulse = cmd_pulses[cmd_start];
        cmd_start = (cmd_start + 1) % MAX_CMDS;
        // printf("SRC %d PULSE %lld\n", src, pulse);

        for (int *ninx_p = node(src) + 1; *ninx_p >= 0; ninx_p++)
        {
            int ninx = *ninx_p;

#if TASK == 1
            pulse_stats[pulse != 0] += 1;
#else
            if (ninx == RX_INX && pulse == 0)
            {
                return false;
            }
#endif

            if (node(ninx)[0])
            {
                if (!pulse)
                {
                    states[ninx] = ~states[ninx];
                    cmd_srcs[cmd_end] = ninx;
                    cmd_pulses[cmd_end] = states[ninx];
                    cmd_end = (cmd_end + 1) % MAX_CMDS;
                }
            }
            else
            {
                if (pulse)
                {
                    states[ninx] |= 1 << src;
                }
                else
                {
                    states[ninx] &= ~(1 << src);
                }
                cmd_srcs[cmd_end] = ninx;
                cmd_pulses[cmd_end] = states[ninx] ^ node_masks[ninx];
                cmd_end = (cmd_end + 1) & 255;
            }
        }
    }
    return true;
}

void main()
{
#if TASK == 1

    for (int i = 0; i < 1000; i++)
    {
        push_button();
    }
    printf("RESULT: %lld\n", (long long)pulse_stats[0] * pulse_stats[1]);

#else
    long result = 0;
    while (push_button())
    {
        result++;

        if ((result & 0xfffff) == 0)
        {
            printf("loop %ld\n", result);
        }
    }

    printf("RESULT: %ld\n", result);

#endif
}
