class Chromosome:
    def __init__(self, value: int | str, length: int):
        if isinstance(value, str):
            value = int(''.join(value), base=2)

        self._encoded = value
        self._bin_encoded = str(bin(value))[2:]
        if self.length < length:
            difference = int(length - self.length)
            additional_zeros = ['0' for _ in range(0, difference)]
            self._bin_encoded += ''.join(additional_zeros)

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

    def full_cross(self, chromosome, k):
        chr1 = self.cross(chromosome, k)
        chr2 = self.rcross(chromosome, k)
        return chr1, chr2

    @staticmethod
    def create_chromosome(number: float | int, left_border: float | int, h: float, length: int):
        encoded = Chromosome.encode_number(number, left_border, h)
        return Chromosome(encoded, length)

    @staticmethod
    def encode_number(num: int | float, left_border: int | float, h: float):
        return round((num - left_border) / h)

    def __repr__(self):
        return f'Encoded: {self.encoded}, binary: {self.bin_encoded}'


if __name__ == '__main__':
    pass
