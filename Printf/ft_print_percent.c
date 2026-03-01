/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_percent.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 00:40:42 by oalabed           #+#    #+#             */
/*   Updated: 2026/02/28 01:20:03 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <unistd.h>

int	ft_print_percent(void)
{
	char	percent;

	percent = '%';
	return (write(1, &percent, 1));
}
