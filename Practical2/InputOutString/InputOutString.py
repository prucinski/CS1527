class InputOutString:
    def get_string(self):
        self._string = input("Give an input string: ")
    def print_string(self):
        print((self._string).upper())

firstString = InputOutString()
firstString.get_string()
firstString.print_string()