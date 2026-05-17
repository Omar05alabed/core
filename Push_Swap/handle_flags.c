/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   handle_flags.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: domansou <domansou@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/14 01:39:00 by domansou          #+#    #+#             */
/*   Updated: 2026/04/14 21:19:37 by domansou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	handle_flags(int ac, char **av, t_bench *b, int *f)
{
	int	i;

	i = 1;
	while (i < ac && av[i][0] == '-' && av[i][1] == '-')
	{
		if (ft_strcomp(av[i], "--bench") == 0)
		{
			*f = 1;
		}
		else
			set_strategy(b, av[i]);
		i++;
	}
}
