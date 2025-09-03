class encoder():
    
    def coords_to_colors(self, data, pix):
        colors = []
        for x in data:
            plus=next(pix)
            colors.append((x[0]+plus[0]-3, x[1]+plus[1]-3, x[2]+plus[2]-3))
        return colors

    def encode(self, data, height, width, pix):
        colors = self.coords_to_colors(data, pix)
        len_colors = len(colors)
        res = []
        for i in range(height):
            for j in range(width):
                basik = next(pix)
                res.append((basik[0],basik[1],basik[2]))
                for _ in range(3):
                    if len_colors > 0:
                        res.append(next(colors))
                        len_colors -= 1
                    else:
                        res.append((basik[0],basik[1],basik[2]))
        return res

        
class decoder():
    pass