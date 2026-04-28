# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 22:37:18 by oalabed           #+#    #+#              #
#    Updated: 2026/04/27 22:37:45 by oalabed          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_count_harvest_iterative():
     days = int(input("Days until harvest:"))
     i = 1

     while i <= days:  
            print("Day",i)
            i += 1
     print("Harvest time!")     

ft_count_harvest_iterative()

def ft_count_harvest_iterative():
     days = int(input("Days until harvest:"))

     for i in range (1 , days + 1):
                     print("Day",i)

    print("Harvest time!")
