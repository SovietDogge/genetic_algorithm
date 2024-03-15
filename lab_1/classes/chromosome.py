class Chromosome:
    def __init__(self, value: int | str):
        if isinstance(value, str):
            value = int(str(value), base=2)

        self._encoded = value
        self._bin_encoded = str(bin(value))[2:]

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
        binary = str([self.bin_encoded[i] if i < k else chromosome.bin_encoded[i] for i in range(0, self.length)])
        return Chromosome(binary)

    def rcross(self, chromosome, k):
        binary = str([self.bin_encoded[i] if i > k else chromosome.bin_encoded[i] for i in range(0, self.length)])
        return Chromosome(binary)

    def full_cross(self, chromosome, k):
        chr1 = self.cross(chromosome, k)
        chr2 = self.rcross(chromosome, k)
        return chr1, chr2

    @staticmethod
    def create_chromosome(number: float | int, left_border: float | int, h: float):
        encoded = Chromosome.encode_number(number, left_border, h)
        return Chromosome(encoded)

    @staticmethod
    def encode_number(num: int | float, left_border: int | float, h: float):
        return round((num - left_border) / h)

    def __repr__(self):
        return f'Encoded: {self.encoded}, binary: {self.bin_encoded}'


if __name__ == '__main__':
    pass
