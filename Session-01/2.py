

class ClaculateNumber:
    """ this class will calculate numbers
    """

    def __init__(self):
        super(ClaculateNumber, self).__init__() # why ??? 

    def add_numbers(self, num1: float = 0, num2: float = 0) -> float:
        """ will add to numbers from given argumants
        :param num1: number 1 is <float>
        :param num2: number 2 is <float>
        :return: num1 + num2 that will be <float> 
        """
        return num1 + num2

    def add_peridically(self, num1: float = 1) -> float:
        for i in range(1, 10): # [1, ..., 10]
            num1 += i
        return num1

def main():
    cn = ClaculateNumber()
    print(cn.add_numbers(
        num1=1.123, 
        num2=12.412
    ))
    print(cn.add_peridically(num1=10))


if __name__ == "__main__":
    main()
