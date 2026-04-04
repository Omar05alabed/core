#include "push_swap.h"

int stack_size(t_stack* stack)
{
    int i;

    i = 0;
    while (stack)
    {
        i++;
        stack = stack->next;
    }
    return (i);
}

int stack_min(t_stack* stack)
{
    int min;

    if (!stack)
        return (0);
    min = stack->value;
    while (stack)
    {
        if (stack->value < min)
            min = stack->value;
        stack = stack->next;
    }
    return (min);
}

int stack_max(t_stack* stack)
{
    int max;

    if (!stack)
        return (0);
    max = stack->value;
    while (stack)
    {
        if (stack->value > max)
            max = stack->value;
        stack = stack->next;
    }
    return (max);
}

int stack_position(t_stack* stack, int value)
{
    int i;

    i = 0;
    while (stack)
    {
        if (stack->value == value)
            return (i);
        stack = stack->next;
        i++;
    }
    return (-1);
}

int stack_sorted(t_stack* stack)
{
    if (!stack)
        return (1);
    while (stack->next)
    {
        if (stack->value > stack->next->value)
            return (0);
        stack = stack->next;
    }
    return (1);
}