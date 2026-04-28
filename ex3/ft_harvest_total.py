# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 22:34:25 by oalabed           #+#    #+#              #
#    Updated: 2026/04/27 22:34:47 by oalabed          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
   day1 = int(input("Day 1 harvest:"))
   day2 = int(input("Day 2 harvest:"))
   day3 = int(input("Day 3 harvest:"))
   total = day1 + day2 + day3
   print("Total harvest:",total)
