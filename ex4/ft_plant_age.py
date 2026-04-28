# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 22:35:15 by oalabed           #+#    #+#              #
#    Updated: 2026/04/27 22:35:33 by oalabed          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    age = int(input("Enter plant age in days:"))
    if(age <= 60):
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
