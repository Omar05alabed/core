/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   adaptive.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/08 15:19:28 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/08 15:32:01 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	adaptive_sort(t_stack **a, t_stack **b, t_bench bench, double disorder)
{
	if (is_sorted(*a))
		return ;
	if (disorder < 0.2)
		simple_sort(a, b, bench);
	else if (disorder < 0.5 && disorder >= 0.2)
		chunk_sort(a, b, bench);
	else if (disorder >= 0.5)
		radix_sort(a, b, bench);
}
