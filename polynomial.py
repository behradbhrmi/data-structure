
# ===================================================================================================
# Behrad Bahrami
#
# form of polynomial should be like -->> your_list = [ [coe0, exp0], [coe1, exp1], [coe2, exp2], ...]
# the first value is coefficent [coe] and the second is exponent [exp]
# [coe, epx]
# ===================================================================================================

from string import ascii_letters



class Polynomial:
    def __init__(self, input_list:list[list[int, int]]):
        self.poly = self.refiner(input_list)
        

    def __add__(self, other) :
        in_list = self.poly + other
        return self.calc(in_list, 'sum')


    def __sub__(self, other):
        in_list = self.poly + other
        return self.calc(in_list, 'sub')


    def __mul__(self, other):
        if type(other) == int :
            return [[x[0]*other,x[1]] for x in self.poly]
        elif type(other) == Polynomial :
            temp_list = []
            for item1 in self.poly:
                for item2 in other.poly:
                    temp_list.append([item1[0]*item2[0], item1[1]+item2[1]])
        return self.calc(temp_list, 'sum')


    def __str__(self):
        result, sign, e_sign, var = '', '', '^', 'x'
        for index, item in enumerate(self.poly):
            coe = item[0]
            exp = item[1]

            if exp == 1:
                exp = ''
                e_sign = ''
            if exp == 0 :
                var = ''
                e_sign = ''
                exp = ''
            if coe > 0 :
                if index != 0 :  
                    sign = '+'
            else:
                if coe == -1: 
                    coe = ''
                coe = -item[0]
                sign = '-'
            if coe == 1 :
                coe = ''
            result += f"{sign} {coe}{var}{e_sign}{exp} "
        return result


    def calc(self, input_list, operation):
        final_list = []
        ignore_list = []
        for index1, item1 in enumerate(input_list) :
            for index2, item2 in enumerate(input_list[index1+1:], start=index1+1):
                if (index1 in ignore_list) or (index2 in ignore_list):continue
                if item1[1] == item2[1] :
                    ignore_list.append(index1)
                    ignore_list.append(index2)
                    if operation == 'sum':
                        final_list.append([item1[0]+item2[0], item1[1]])
                    elif operation == 'sub':
                        final_list.append([item1[0]-item2[0], item1[1]])
            if index1 not in ignore_list :
                final_list.append(item1)
        for item in final_list :
            if item[0] == 0 :
                final_list.remove(item)
        return final_list


    def refiner(self, input_list):
        if type(input_list) == list :
            return input_list
        final_result = []
        input_list = input_list.split(' ')
        for item in input_list:
            var_index = ''
            for i in item:
                if i in ascii_letters :
                    var_index = item.index(i)
                    break
            coe = int(item[0:var_index])
            if '^' in item:
                exp = int(item[var_index+2:])
            else: 
                exp = 1
            final_result.append([coe, exp])
        return final_result
