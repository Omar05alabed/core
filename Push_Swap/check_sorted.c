/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_sorted.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/13 15:00:56 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/13 15:16:02 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	check_sorted(int sort, int *flag, t_bench *benchb)
{
	if (sort == 1)
	{
		ft_strcpy(benchb->complexity, "O(0)");
		if (*flag == 1)
			bench(benchb->disorder, benchb);
		return (1);
	}
	return (0);
}
