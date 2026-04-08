#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdlib.h>
# include <unistd.h>
# include <limits.h>

/*
** If your project already defines these structs elsewhere,
** remove these typedefs to avoid redefinition errors.
*/
typedef struct s_stack
{
	int				value;
	int				index;
	struct s_stack* next;
}	 s_stack;

/* stack utils */
void	assign_index(s_stack** a);
void	free_stack(s_stack** a);
s_stack* new_node(int value);
s_stack* stack_init(int* arr, int size);
int		stack_size(t_stack* a);
int		ft_push(s_stack** a, int value);

/* parsing */
long	ft_atoi(char* str);
int* ft_parsing(int argc, char** argv);
int		is_number(char* str);
int		ft_duplicate(int* arr, int size);
void	print_error(void);

/* operations */
void	ft_pa(s_stack** a, s_stack** b);
void	ft_pb(s_stack** a, s_stack** b);

void	ft_ra(t_stack** a);
void	ft_rb(t_stack** b);
void	ft_rr(s_stack** a, s_stack** b);

void	ft_rra(s_stack** a);
void	ft_rrb(s_stack** b);
void	ft_rrr(s_stack** a, s_stack** b);

void	ft_sa(s_stack** a);
void	ft_sb(s_stack** b);
void	ft_ss(s_stack** a, s_stack** b);

/* sorting */
void	simple_sort(s_stack** a, s_stack** b);

#endif