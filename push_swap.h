/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/08 14:54:56 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/08 15:37:35 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <limits.h>
# include <stdlib.h>
# include <unistd.h>

/*
** If your project already defines these structs elsewhere,
** remove these typedefs to avoid redefinition errors.
*/
typedef struct s_stack
{
	int				value;
	int				index;
	struct s_stack	*next;
}					t_stack;

typedef struct s_bench
{
	int				pa;
	int				pb;

	int				ra;
	int				rb;
	int				rr;

	int				sa;
	int				sb;
	int				ss;

	int				rra;
	int				rrb;
	int				rrr;

	int				total_obs;
}					t_bench;

/* stack utils */
void				assign_index(s_stack **a);
void				free_stack(s_stack **a);
s_stack				*new_node(int value);
s_stack				*stack_init(int *arr, int size);
int					stack_size(t_stack *a);
int					ft_push(s_stack **a, int value);

/* parsing */
long				ft_atoi(char *str);
int					*ft_parsing(int argc, char **argv);
int					is_number(char *str);
int					ft_duplicate(int *arr, int size);
void				print_error(void);

/* operations */
void				ft_pa(t_stack **a, t_stack **b, t_bench *bench);
void				ft_pb(t_stack **a, t_stack **b, t_bench *bench);

void				ft_ra(t_stack **a, t_bench *bench);
void				ft_rb(t_stack **b, t_bench *bench);
void				ft_rr(t_stack **a, t_stack **b, t_bench *bench);

void				ft_rra(t_stack **a, t_bench *bench);
void				ft_rrb(t_stack **b, t_bench *bench);
void				ft_rrr(t_stack **a, t_stack **b, t_bench *bench);

void				ft_sa(t_stack **a, t_bench *bench);
void				ft_sb(t_stack **b, t_bench *bench);
void				ft_ss(t_stack **a, t_stack **b, t_bench *bench);

/* sorting */
void				simple_sort(t_stack **a, t_stack **b, t_bench *bench);
void				radix_sort(t_stack **a, t_stack **b, t_bench *bench);

double				compute_disorder(t_stack *a, t_bench *bench);
int					is_sorted(t_stack *a);

#endif
