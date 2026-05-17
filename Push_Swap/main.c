/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/12 15:00:54 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/15 01:47:30 by domansou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

static int	is_bench_only(int ac, char **av, t_bench *bn)
{
	if (ac == 2 && ft_strcomp(av[1], "--bench") == 0)
	{
		bn->disorder = 0;
		ft_strcpy(bn->strategy, "Adaptive");
		ft_strcpy(bn->complexity, "O(1)");
		bench(0, bn);
		return (1);
	}
	return (0);
}

static int	get_start(int argc, char **argv)
{
	int	i;

	i = 1;
	while (i < argc && argv[i][0] == '-' && argv[i][1] == '-')
		i++;
	return (i);
}

static void	run_sort(t_stack **a, t_stack **b, t_bench *bench)
{
	if (ft_strcomp(bench->strategy, "simple") == 0)
		simple_sort(a, b, bench);
	else if (ft_strcomp(bench->strategy, "medium") == 0)
		sort_medium_chunk(a, b, bench);
	else if (ft_strcomp(bench->strategy, "complex") == 0)
		radix_sort(a, b, bench);
	else if (ft_strcomp(bench->strategy, "adaptive") == 0)
		adaptive_sort(a, b, bench, bench->disorder);
}

int	main(int argc, char **argv)
{
	t_stack	*a;
	t_stack	*b;
	t_bench	benchb;
	int		bench_flag;

	a = NULL;
	b = NULL;
	bench_flag = 0;
	if (argc < 2)
		return (0);
	bench_init(&benchb);
	if (is_bench_only(argc, argv, &benchb))
		return (0);
	handle_flags(argc, argv, &benchb, &bench_flag);
	init_stack(argc, argv, get_start(argc, argv), &a);
	if (!a || check_sorted(is_sorted(a), &bench_flag, &benchb))
		return (0);
	benchb.disorder = compute_disorder(a);
	run_sort(&a, &b, &benchb);
	if (bench_flag)
		bench(benchb.disorder, &benchb);
	free_stack(&a);
	free_stack(&b);
	return (0);
}
