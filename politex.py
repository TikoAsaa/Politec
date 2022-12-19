"""
class Naive:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hcfnaive(self):
        while self.b:
            self.a, self.b = self.b, self.a % self.b
        print(abs(self.a))


x1 = Naive(50, 60)
x1.hcfnaive()


class Compute:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute_lcm(self):
        if self.x > self.y:
            greater = self.x
        else:
            greater = self.y

        while True:
            if (greater % self.x == 0) and (greater % self.y == 0):
                lcm = greater
                break
            greater += 1

        print("The L.C.M. is", lcm)


num1 = 54
num2 = 24

x1 = Compute(num1, num2)
x1.compute_lcm()



class Encode:
    def __init__(self, message):
        self.message = message

    def encode_message(self):
        encode_string = ""
        i = 0
        while i <= len(self.message) - 1:
            count = 1
            ch = self.message[i]
            j = i
            while j < len(self.message) - 1:
                if self.message[j] == self.message[j + 1]:
                    count = count + 1
                    j = j + 1
                else:
                    break

            encode_string = encode_string + str(count) + ch
            i = j + 1
        print(encode_string)


x1 = Encode("AAACCCAA")
x1.encode_message()

"""

class Decode:
    def __init__(self, message):
        self.message = message

    def decode_message(self):
        decoded_string = ""
        i = 0
        j = 0
        while i <= len(self.message) - 1:
            run_count = int(self.message[i])
            run_word = self.message[i + 1]
            for j in range(run_count):
                decoded_string = decoded_string + run_word
                j = j + 1
            i = i + 2
        print(decoded_string)


x1 = Decode("3A3C2A")
x1.decode_message()