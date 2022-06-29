class Cell:

    def __init__(self, status):
        self.status = status

    def kill(self):
        """
        Set a cell's status to 0
        """
        self.status = 0

    def resurrect(self):
        """
        Set a cell's status to 1
        """
        self.status = 1

    def is_alive(self):
        """
        Checks if a cell's status is 1
        :return: True / False
        """
        return self.status == 1

    def get_symbol(self):
        """
        :return: "o" is status is 1, "." else
        """
        if self.status == 0:
            return "."
        else:
            return "o"
