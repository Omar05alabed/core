# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 22:36:18 by oalabed           #+#    #+#              #
#    Updated: 2026/04/27 22:36:34 by oalabed          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    watering = int(input("Days since last watering:"))
    if(watering > 2):
        print("Water the plants")
    else:
        print("Plants are fine")
