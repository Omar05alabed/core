#include "push_swap.h"

t_stack* stack_new(int value)
{
    t_stack* node;

    node = malloc(sizeof(t_stack));
    if (!node)
        return (NULL);
    node->value = value;
    node->next = NULL;
    return (node);
}

t_stack* stack_last(t_stack* stack)
{
    if (!stack)
        return (NULL);
    while (stack->next)
        stack = stack->next;
    return (stack);
}

void    stack_add_back(t_stack** stack, t_stack* new)
{
    t_stack* last;

    if (!stack || !new)
        return;
    if (!*stack)
    {
        *stack = new;
        return;
    }
    last = stack_last(*stack);
    last->next = new;
}

t_stack* init_stack(int argc, char** argv)
{
    t_stack* stack;
    int     i;
    int     value;

    stack = NULL;
    i = 1;
    while (i < argc)
    {
        value = ft_atoi(argv[i]); // make sure you validate before this
        stack_add_back(&stack, stack_new(value));
        i++;
    }
    return (stack);
}