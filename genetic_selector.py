import drawer


class GeneticSelector:
    def __init__(self, children_size, survival_group_size):
        self.drawer = drawer.Drawer(500, 500)
        self.children_size = children_size
        self.survival_group_size = survival_group_size
        self.population = []
        initial_img = drawer.init_img()
        for _i in survival_group_size:
            self.population = self.population.append(initial_img)

    def generate_children(self, img):
        return [self.drawer.draw_ellipse(img) for _i in range(self.children_size)]
