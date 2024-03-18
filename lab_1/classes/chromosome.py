import numpy as np

rng = np.random.default_rng(2)


class Chromosome:
    def __init__(self, value: int | str, length: int):
        if isinstance(value, str):
            value = int(''.join(value), base=2)

        self._encoded = value
        self._bin_encoded = list(bin(value))[2:]
        if self.length < length:
            difference = int(length - self.length)
            additional_zeros = ['0' for _ in range(0, difference)]
            self._bin_encoded = [*additional_zeros, *self.bin_encoded]

        # self._bin_encoded = ''.join(self._bin_encoded)

    @property
    def encoded(self):
        return self._encoded

    @property
    def bin_encoded(self):
        return self._bin_encoded

    @property
    def length(self):
        return len(self.bin_encoded)

    def cross(self, chromosome, k):
        binary = [self.bin_encoded[i] if i < k else chromosome.bin_encoded[i] for i in range(0, self.length)]
        return Chromosome(''.join(binary), self.length)

    def rcross(self, chromosome, k):
        binary = [self.bin_encoded[i] if i > k else chromosome.bin_encoded[i] for i in range(0, self.length)]
        return Chromosome(''.join(binary), self.length)

    def full_cross(self, chromosome):
        k = rng.integers(1, self.length)

        chr1 = self.cross(chromosome, k)
        chr2 = self.rcross(chromosome, k)
        return chr1, chr2

    def mutate(self):
        for i in range(0, self.length):
            if rng.random() <= 0.01:
                self._bin_encoded[i] = '0' if self._bin_encoded == '1' else '1'

        self._encoded = int(''.join(self._bin_encoded), base=2)

    @staticmethod
    def create_chromosome(number: float | int, left_border: float | int, h: float, length: int):
        encoded = Chromosome.encode_number(number, left_border, h)
        return Chromosome(encoded, length)

    @staticmethod
    def encode_number(num: int | float, left_border: int | float, h: float) -> int:
        return round((num - left_border) / h)

    @staticmethod
    def decode_number(encoded: int, left_border: int, h: float) -> float:
        return left_border + encoded * h

    def __repr__(self):
        return f'Encoded: {self.encoded}, binary: {self.bin_encoded}'


if __name__ == '__main__':
    pass
