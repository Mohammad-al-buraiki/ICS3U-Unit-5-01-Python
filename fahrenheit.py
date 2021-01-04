# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is a loop a while loop


def fehrenheit():
    # this function calculates the temperature in degrees celsius
    # and convert temperature is degrees Fahrenheit

    celsius = input("Enter the degree in celsius: ")

    # process
    fehrenheit = (9/5)*celsius+32
    # output
    print("the degree celsius {0} in fehrenheit is {1}."
          .format(celsius, fehrenheit))


def main():
    # this function just calls other functions

    fehrenheit()


if __name__ == "__main__":
    main()
