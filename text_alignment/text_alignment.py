def main():

    thickness = int(input())  # User input for the thickness of the
    # pattern (must be an odd number)
    c = "H"  # Character used to form the shape

    # Top Cone
    # This loop prints the top cone-like structure
    if 0 < thickness < 50:
        for i in range(thickness):
            # rjust and ljust are used to align the character `H` in the
            # shape of a cone
            print(
                (c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)
            )

        # Top Pillars
        # This loop prints two vertical pillars on either side
        for i in range(thickness + 1):
            # center is used to align the pillars in the center of the
            # defined width
            print(
                (c * thickness).center(thickness * 2)
                + (c * thickness).center(thickness * 6)
            )

        # Middle Belt
        # This loop prints the middle belt connecting the two pillars
        for i in range((thickness + 1) // 2):
            # center is used to align the long horizontal belt in the
            # center
            print((c * thickness * 5).center(thickness * 6))

        # Bottom Pillars
        # This loop prints the bottom pillars (similar to the top
        # pillars)
        for i in range(thickness + 1):
            # Same logic as Top Pillars to print the bottom pillars
            print(
                (c * thickness).center(thickness * 2)
                + (c * thickness).center(thickness * 6)
            )

        # Bottom Cone
        # This loop prints an inverted cone at the bottom
        for i in range(thickness):
            # The cone is printed using rjust and ljust, aligned to the
            # right side
            print(
                (
                    (c * (thickness - i - 1)).rjust(thickness)
                    + c
                    + (c * (thickness - i - 1)).ljust(thickness)
                ).rjust(thickness * 6)
            )


if __name__ == "__main__":
    main()
