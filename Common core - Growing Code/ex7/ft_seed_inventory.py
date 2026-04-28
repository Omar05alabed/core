# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 22:38:48 by oalabed           #+#    #+#              #
#    Updated: 2026/04/27 22:39:10 by oalabed          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    if unit == "packets":
        print( seed,"seeds:",quantity,unit,"available")
    elif unit == "grams":
        print(seed,"seeds:",quantity,unit,"total")
    elif unit == "area":
        print(seed,"seeds:","covers",quantity,"square meters")
