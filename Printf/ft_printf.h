/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 19:58:15 by oalabed           #+#    #+#             */
/*   Updated: 2026/03/01 01:05:48 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

int	ft_print_char(char c);
int	ft_print_str(char *s);
int	ft_print_percent(void);
int	ft_print_dec(int n);
int	ft_print_unsigned(unsigned int n);
int	ft_print_hex(unsigned long int n, char format);
int	ft_print_ptr(void *ptr);
int	ft_printf(const char *format, ...);

#endif
