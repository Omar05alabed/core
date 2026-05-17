/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   adaptive.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/08 15:19:28 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/14 05:28:55 by domansou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	adaptive_sort(t_stack **a, t_stack **b, t_bench *bench, double disorder)
{
	if (is_sorted(*a))
		return ;
	if (disorder < 0.2)
	{
		simple_sort(a, b, bench);
		ft_strcpy(bench->complexity, "O(n2)");
	}
	else if (disorder >= 0.2 && disorder < 0.5)
	{
		sort_medium_chunk(a, b, bench);
		ft_strcpy(bench->complexity, "O(n√n)");
	}
	else if (disorder >= 0.5)
	{
		radix_sort(a, b, bench);
		ft_strcpy(bench->complexity, "O(nlogn)");
	}
}
