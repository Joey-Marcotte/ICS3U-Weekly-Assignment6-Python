#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: November 2019
# This program calculates the volume of a frustem

import math


def volume(outer_radius, inner_radius, height):
    # calculates volume

    volume = math.pi*height/3*(outer_radius**2 + outer_radius*inner_radius +
                               inner_radius**2)

    return volume


def main():
    # this function gets inputs and calls other function
    while True:
        # input
        outer_radius = input("Enter Outer Radius of Frustem(R) in cm: ")
        inner_radius = input("Enter Inner Radius of Frustem(r) in cm: ")
        height = input("Enter height of Frustem in cm: ")

        try:
            outer_radius_number = int(outer_radius)
            inner_radius_number = int(inner_radius)
            height_number = int(height)

            calculate_volume = volume(outer_radius_number, inner_radius_number,
                                      height_number)

        # output
            print("")
            print("Volume of Frustem is {:,.2f}cm".format(calculate_volume))
            break

        except(ValueError):
            print("Invalid input")
            print("")


if __name__ == "__main__":
    main()
