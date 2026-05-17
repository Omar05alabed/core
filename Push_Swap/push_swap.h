/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/08 14:54:56 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/14 20:41:29 by domansou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <limits.h>
# include <stdarg.h>
# include <stdlib.h>
# include <unistd.h>

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

	char			complexity[10];
	char			strategy[10];

	int				total_obs;
	double			disorder;
}					t_bench;

/* stack utils */
void				assign_index(t_stack **a);
void				free_stack(t_stack **a);
t_stack				*new_node(int value);
int					stack_size(t_stack *a);
void				ft_push(t_stack **a, int value);

/* parsing */
long				ft_atoi(char *str);
int					*to_int_array(char **tokens, int *size);
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
void				sort_medium_chunk(t_stack **a, t_stack **b, t_bench *bench);
void				adaptive_sort(t_stack **a, t_stack **b, t_bench *bench,
						double disorder);

double				compute_disorder(t_stack *a);
int					is_sorted(t_stack *a);

void				bench_init(t_bench *bench);
void				bench(double disorder, t_bench *benchb);
// printf
int					ft_print_char(char c, int fd);
int					ft_print_str(char *s, int fd);
int					ft_print_dec(int n, int fd);
int					ft_printf(int fd, const char *format, ...);
int					ft_print_float(double n, int fd);
int					ft_strcomp(char *s1, char *s2);
char				*ft_strcpy(char *dest, char *src);
void				set_strategy(t_bench *bench, char *flag);
int					check_sorted(int sort, int *flag, t_bench *benchb);
void				handle_flags(int ac, char **av, t_bench *b, int *f);
void				init_stack(int argc, char **argv, int start, t_stack **a);
void				free_split(char **arr);
char				**collect_tokens(int argc, char **argv, int start);
char				**split_whitespace(const char *s);
int					is_space(char c);
#endif
