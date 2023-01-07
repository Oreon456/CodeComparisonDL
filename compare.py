import ast


class FileReader():  # this class is responsible for reading and processing python code into abstract syntax trees

    def read_file(self, filename):
        self.filename = filename
        with open(self.filename) as f:
            code = f.read()
        node = ast.parse(code)
        return ast.dump(node, indent=2)


class Difference():  # returns levenstein distance between two given strings
    def levenstein(self, str_1, str_2):
        n, m = len(str_1), len(str_2)
        if n > m:
            str_1, str_2 = str_2, str_1
            n, m = m, n

        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                if str_1[j - 1] != str_2[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)

        return current_row[n]

    def amount_of_constructions(self, str1, str2):  # counting prints for`s while`s etc.
        mass = []  # creating a lists that consists rates of amount of different language constructions
        checklist = ['While', 'IF', 'For', 'print', 'list',
                     'Constant']  # constructions of the language that are checked
        for i in checklist:  # filling the list with values
            try:
                mass.append(min(str1.count(i), str2.count(i)) / max(str1.count(i), str2.count(i)))
            except:
                mass.append(0)
                pass
        return sum(mass) / len(mass)


name1 = input('Path to first file: ')
name2 = input('Path to second file: ')

if __name__ == '__main__':
    file = FileReader()
    diff = Difference()

    tree1 = file.read_file(name1)
    tree2 = file.read_file(name2)

    levenstein_distance = diff.levenstein(tree1, tree2)

    result1 = levenstein_distance / ((len(tree1) + len(tree2)) * 2)
    result2 = diff.amount_of_constructions(tree1, tree2)
    result = (result1 + result2) / 2
    print(str(result))
