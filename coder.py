class Encoder:
    def coords_to_colors(self, data, pix):
        colors = []
        for x in data:
            plus = next(pix)
            colors.append((
                x[0] + plus[0] - 3,
                x[1] + plus[1] - 3,
                x[2] + plus[2] - 3
            ))
        return colors

    def encode(self, data, height, width, pix):
        colors = iter(self.coords_to_colors(data, pix))
        res = []
        for i in range(height):
            for j in range(width):
                basik = next(pix)
                res.append((basik[0], basik[1], basik[2]))
                for _ in range(3):
                    try:
                        res.append(next(colors))
                    except StopIteration:
                        res.append((basik[0], basik[1], basik[2]))
        return iter(res)