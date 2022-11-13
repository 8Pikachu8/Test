import numpy as np
import matplotlib.pyplot as plt
import Config


class Population:
    def __init__(self, alpha: float, N: int, id: int):
        self.array_N = []
        self.alpha = alpha
        self.N = N
        self.id = id

    def multiplication(self):
        return self.alpha * self.N

    def __str__(self):
        return f"id: {self.id} alpha: {self.alpha}  N: {self.N}"

    def interaction(self, populations):
        self.array_N.append(self.N)
        f = 0
        for population in populations:
            if self == population:
                continue
            f += Config.coefficients[self.id][population.id] * population.N * self.N
        self.N += Config.delta * (self.multiplication() + f)
        print("----------------")

    def interaction_2(self, populations):
        f = 0
        for population in populations:
            if self == population:
                continue
            f += Config.coefficients[self.id][population.id] * population.N * self.N
        f = self.multiplication() + f
        return f

    def method_runge_kutta(self, populations):
        self.array_N.append(self.N)
        a = self.N
        k1 = self.interaction_2(populations)
        self.N = a + 0.5 * Config.delta * k1
        k2 = self.interaction_2(populations)
        self.N = a + 0.5 * Config.delta * k2
        k3 = self.interaction_2(populations)
        self.N = a + Config.delta * k3
        k4 = self.interaction_2(populations)
        self.N = a + (k1 + 2 * k2 + 2 * k3 + k4) * Config.delta / 6
