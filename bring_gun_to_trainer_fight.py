"""
Bringing a Gun to a Trainer Fight
=================================

Uh-oh -- you've been cornered by one of Commander Lambdas elite bunny trainers! Fortunately, you grabbed a beam weapon from an abandoned storeroom while you were running through the station, so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the bunny trainers: its beams reflect off walls, meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam hits either you or the bunny trainer, it will stop immediately (albeit painfully). 

Write a function solution(dimensions, your_position, trainer_position, distance) that gives an array of 2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 integers of the trainer's x and y coordinates in the room, and returns an integer of the number of distinct directions that you can fire to hit the elite trainer, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite trainer are both positioned on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite trainer were positioned in a room with dimensions [3, 2], your_position [1, 1], trainer_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite trainer (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite trainer with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite trainer with a total shot distance of sqrt(5).

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
Solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9

-- Python cases --
Input:
solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9
"""
from math import sqrt, atan2, ceil
from copy import deepcopy


class Room:
    def __init__(self, dim, pos, guard_pos, distance):
        self.room_x = dim[0]
        self.room_y = dim[1]
        self.player_x = pos[0]
        self.player_y = pos[1]
        self.guard_x = guard_pos[0]
        self.guard_y = guard_pos[1]
        self.max_distance = distance
        self.max_x = self.player_x + distance + 1
        self.max_y = self.player_y + distance + 1

    def get_dist(self, point_x, point_y):
        """Gets distance between player and a point"""
        dist = sqrt((point_x - self.player_x) ** 2 + (point_y -
                                                      self.player_y) ** 2)
        return dist

    def get_angle(self, point_x, point_y):
        """Gets angle between player and a point in RAD"""
        angle = atan2(point_y - self.player_y, point_x - self.player_x)
        return angle

    def get_first_quadrant(self):
        """gets the number of copies that need to be done along the axis
        and gets all the guard and player coords"""
        num_copies_x = ceil(self.max_x / self.room_x)
        num_copies_x = int(num_copies_x)
        num_copies_y = ceil(self.max_y / self.room_y)
        num_copies_y = int(num_copies_y)

        player_exp_x = []
        player_exp_y = []
        guard_exp_x = []
        guard_exp_y = []
        # Loop expands along the x axis
        for i in range(0, num_copies_x + 1, 1):
            temp_player_y_list = []
            temp_guard_y_list = []
            r_x = self.room_x * i

            if len(player_exp_x) == 0:
                n_p_p_x = self.player_x
            else:
                n_p_p_x = (r_x - player_exp_x[-1][0]) + r_x
            player_exp_x.append([n_p_p_x, self.player_y, 1])

            if len(guard_exp_x) == 0:
                n_g_p_x = self.guard_x
            else:
                n_g_p_x = (r_x - guard_exp_x[-1][0]) + r_x
            guard_exp_x.append([n_g_p_x, self.guard_y, 7])

            # Loop expands along the x axis
            for j in range(1, num_copies_y + 1, 1):
                r_y = self.room_y * j
                if len(temp_guard_y_list) == 0:
                    n_g_p_y = (r_y - self.guard_y) + r_y
                    temp_guard_y_list.append(n_g_p_y)
                else:
                    n_g_p_y = (r_y - temp_guard_y_list[-1]) + r_y
                    temp_guard_y_list.append(n_g_p_y)
                guard_exp_y.append([n_g_p_x, n_g_p_y, 7])

                if len(temp_player_y_list) == 0:
                    n_p_p_y = (r_y - self.player_y) + r_y
                    temp_player_y_list.append(n_p_p_y)
                else:
                    n_p_p_y = (r_y - temp_player_y_list[-1]) + r_y
                    temp_player_y_list.append(n_p_p_y)
                player_exp_y.append([n_p_p_x, n_p_p_y, 1])

        return player_exp_x + guard_exp_x + player_exp_y + guard_exp_y

    def other_quadrants(self, matrix):
        """Uses the list from the first quadrant and flips its to the other
        3 quadrants"""
        q2 = deepcopy(matrix)
        q2t = [-1, 1]
        q2f = []
        for j in range(len(q2)):
            list = [q2[j][i] * q2t[i] for i in range(2)]
            dist = self.get_dist(list[0], list[1])

            if dist <= self.max_distance:
                list.append(matrix[j][2])
                q2f.append(list)

        q3 = deepcopy(matrix)
        q3t = [-1, -1]
        q3f = []
        for j in range(len(q3)):
            list = [q3[j][i] * q3t[i] for i in range(2)]
            dist = self.get_dist(list[0], list[1])

            if dist <= self.max_distance:
                list.append(matrix[j][2])
                q3f.append(list)

        q4 = deepcopy(matrix)
        q4t = [1, -1]
        q4f = []
        for j in range(len(q3)):
            list = [q4[j][i] * q4t[i] for i in range(2)]
            dist = self.get_dist(list[0], list[1])

            if dist <= self.max_distance:
                list.append(matrix[j][2])
                q4f.append(list)

        return q2f, q3f, q4f

    def filter_target_hit(self, matrix):
        """Uses a dict with angles as key
        Filters by range and by distance of the same angle (closer always
        wins)"""
        target = {}
        for i in range(len(matrix)):
            dist = self.get_dist(matrix[i][0], matrix[i][1])
            angle = self.get_angle(matrix[i][0], matrix[i][1])
            test_a = self.max_distance >= dist > 0
            test_b = angle not in target
            test_c = angle in target and dist < target[angle][1]
            if test_a and (test_b or test_c):
                target[angle] = [matrix[i], dist]

        return target


def return_count(dict):
    count = 0
    for key in dict:
        if dict[key][0][2] == 7:
            count += 1
    return count


def solution(dimensions, your_position, guard_position, distance):
    # Makes a room instance with all the parameters given
    p = Room(dimensions, your_position, guard_position, distance)

    # Generates all possible points in the first quadrant
    first_quadrant = p.get_first_quadrant()

    # Get all position in all  other quadrants
    q2, q3, q4 = p.other_quadrants(first_quadrant)
    final_list = first_quadrant + q2 + q3 + q4

    # Filters the Original player, and all unattainable guards
    final_dict = p.filter_target_hit(final_list)

    # Returns count
    count = return_count(final_dict)
    return count


# Test cases found online

#
dimensions = [10, 10]
captain_position = [4, 4]
badguy_position = [3, 3]
distance = 5000
# REAL answer = 739323



# dimensions = [2, 5]
# captain_position = [1, 2]
# badguy_position = [1, 4]
# distance = 11
# 0.0001 secs and result 27

# dimensions = [23, 10]
# captain_position = [6, 4]
# badguy_position = [3, 2]
# distance = 23
# 0.002 secs and result 8

# dimensions = [300, 275]
# captain_position = [150, 150]
# badguy_position = [180, 100]
# distance = 500
# 0.65 secs and result 9


# dimensions = [3, 2]
# captain_position = [1, 1]
# badguy_position = [2, 1]
# distance = 4
# 0 secs and result 7


# dimensions = [1250, 1250]
# captain_position = [1000, 1000]
# badguy_position = [500, 400]
# distance = 10000
# 204 sec and result of 196
# v0.2 183 secs and result of 196

import time

print( solution(dimensions, captain_position, badguy_position, distance) )