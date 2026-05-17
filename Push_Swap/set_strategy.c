/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   set_strategy.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: domansou <domansou@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/13 02:07:10 by domansou          #+#    #+#             */
/*   Updated: 2026/04/13 13:13:18 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	set_strategy(t_bench *bench, char *flag)
{
	if (ft_strcomp(flag, "--simple") == 0)
	{
		ft_strcpy(bench->strategy, "simple");
		ft_strcpy(bench->complexity, "O(n2)");
	}
	else if (ft_strcomp(flag, "--medium") == 0)
	{
		ft_strcpy(bench->strategy, "medium");
		ft_strcpy(bench->complexity, "O(n√n)");
	}
	else if (ft_strcomp(flag, "--complex") == 0)
	{
		ft_strcpy(bench->strategy, "complex");
		ft_strcpy(bench->complexity, "O(nlogn)");
	}
	else
	{
		ft_strcpy(bench->strategy, "adaptive");
	}
}
