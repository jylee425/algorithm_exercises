if __name__ == "__main__":
    N = int(input())

    # recursive function to draw the star
    def draw_star(size):
        if size == 3:
            return ["  *  ", " * * ", "*****"]

        unit = draw_star(size // 2)

        star = []
        # top
        for u in unit:
            star.append(" " * (size // 2) + u + " " * (size // 2))
        # left & right
        for u in unit:
            star.append(u + " " + u)

        return star

    print("\n".join(draw_star(N)))
