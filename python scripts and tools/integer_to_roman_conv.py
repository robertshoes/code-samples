#Integer to roman converter tool

#1-10...50...100...500...1000
roman_numbers = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "L", "C", "D", "M"]


class ConvertTool(object):

    def __init__(self, num):
        self.num = num
        self.roman_num_str = ""

    
    def integer_to_roman(self):
        integer_num = str(self.num)
        counter = 1
        rom_units = ""
        rom_decenes = ""
        rom_hundreds = ""
        rom_thousands = ""
        for each_num in range(len(integer_num)-1, -1, -1):
            roman_number =  int(integer_num[each_num])
            if counter == 1: #units
                if roman_number >= 1 and roman_number <= 3:
                    rom_units += roman_number * "I"
                elif roman_number > 3:
                    rom_units += roman_numbers[roman_number-1]
                else:
                    pass                
            else:
                if counter == 2: #decenes
                    rom_dec = roman_number * 10
                    if rom_dec >= 10 and rom_dec <= 30:
                        rom_decenes += (roman_number) * "X"
                    elif rom_dec == 40:
                        rom_decenes += "XL"
                    elif rom_dec >= 50 and rom_dec <= 80:
                        rom_decenes += ("L" + ((roman_number-5) * "X"))
                    elif rom_dec == 90:
                        rom_decenes += "XC"                                
                if counter == 3: #unit of hundreds
                    rom_h = roman_number * 100
                    if rom_h == 100:
                        rom_hundreds += "C"
                    if rom_h == 500:
                        rom_hundreds += "D"
                if counter == 4: #unit of thousands
                    rom_th = roman_number * 1000
                    if rom_th == 1000:
                        rom_thousands += "M"
                    
            counter += 1        
        self.roman_num_str = rom_thousands + rom_hundreds + rom_decenes + rom_units
        return self.roman_num_str
        
        


if __name__ == "__main__":
    obj = ConvertTool(10)
    print obj.integer_to_roman()
