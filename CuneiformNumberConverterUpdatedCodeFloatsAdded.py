# 
# numberic Script with characters borrow from cunieform. "gal"/1 and "nu"/0 chosen base on their orginal meanings. Gal being "great", being the great value single character before 60
# "nu" being the Sumerian suffix for "not" or "opposite" being as zero. The rest are mainly pick out for having rememberable shapes 
def convertNumbersToCuneiform(number: int, separator: str= " : ") -> str:
    cunie_map = [ "𒉡", #0
                 "𒀀", #1
             
                 "𒀊", #2
                 "𒀖", #3
                 "𒀜", #4
                 "𒀝", #5
                 "𒀠", #6
                 "𒀪", #7
                 "𒀫", #8 
                  "𒀳", #9

                  "𒀴", #10

                 "𒀷", #11

                 "𒁀", #12

                 "𒁉", #13

                "𒁍", #14

                "𒁕", #15

                "𒁲", #16

                "𒁺", #17

               "𒂊", #18

               "𒂔", #19

              "𒂍", #20

                 "𒂕", #21

              "𒂖", #22
              "𒂞", #23

              "𒂟", #24

             "𒃮", #25

             "𒃯", #26

              "𒃰", #27

              "𒃱", #28

              "𒃳", #29

                "𒄩", #30
               "𒁂", #31

               "𒄨", #32

              "𒄧", #33

             "𒋞", #34

              "𒎙", #35

               "𒎘", #36

             "𒎗", #37

             "𒎖", #38

              "𒎕", #39

             " 𒎔  ", #40

            "𒎓", #41

              "𒎒", #42

              "𒎐", #43

            "𒎎", #44

              "𒀾", #45

            "𒎌", #46

            "𒎋", #47

           "𒎉", #48

            "𒎈", #49

            "𒀽", #50

            "𒍽", #51

            "𒍼", #52

             "𒍻", #53

            "𒍺", #54

            "𒁁", #55

            "𒍴", #56

           "𒍳", #57

            "𒍮", # 58



            "𒃲", #59 
    ]

    
    
    if number == 0:
        return cunie_map[0]
    
    
    is_negative = number < 0
    number = abs(number)
    raw_digits = []
    position = 0 
    highest_monumental_pos = -1
    
        
  

    monumental_Values = {
        6: "  𒈤",    # MAH for 60^6
        36: "  𒂗",   # EN for 60^36
        216: "  𒈹", # MUS for 60^216
        1296: "  𒀭",  # AN for 60^1296
        7776: "  𒀮",  # AN.AN for 60^7776
        46656: "  𒀯", # MUL for 60^46656 
    }

    
    # Mathematical Base-60 division loop
    while number > 0: 
        remainder = number % 60
        
        if position in monumental_Values and remainder > 0:
            highest_monumental_pos = position
            if remainder > 1: 
                raw_digits.append((position, f"{cunie_map[remainder]}{monumental_Values[position]}"))
            else: 
                raw_digits.append((position, monumental_Values[position])) 
        else: 
            raw_digits.append((position, cunie_map[remainder]))
        number //= 60 
        position += 1  # Increment the column counter
        
    cunie_digits = []
    for pos, char in raw_digits:
          if char == "𒉡" and pos < highest_monumental_pos:
              continue
          cunie_digits.append(char)
        
        

    

    # CRITICAL: Reversing and joining must happen OUTSIDE the while loop
    cunie_digits.reverse()
    result = separator.join(cunie_digits)

    return f"𒇲{result}" if is_negative else result
    
from decimal import Decimal, getcontext

def convertFloatToCuneiform(value, separator=" : ", radix_point=".", precision=6): # for floats 
    getcontext().prec = 50

    value = Decimal(str(value))

    is_negative = value < 0
    value = abs(value)

    integer_part = int(value)
    fractional_part = value - integer_part

    integer_cunie = convertNumbersToCuneiform(integer_part, separator=separator)

    fractional_digits = []

    for _ in range(precision):
        if fractional_part == 0:
            break

        fractional_part *= 60
        digit = int(fractional_part)
        fractional_part -= digit

        fractional_digits.append(convertNumbersToCuneiform(digit, separator=separator))

    if fractional_digits:
        result = integer_cunie + radix_point + separator.join(fractional_digits)
    else:
        result = integer_cunie

    return f"𒇲{result}" if is_negative else result
    
if __name__ == "__main__":
    # Test basic cases along with a massive test case for 60^6
    # 46656000000 is exactly 60^6
    test_cases = [
        0,
        60,
        3600,
        216000,
        12960000,
        777600000,
        46656000000,
        10314424798490535546171949056000000000000000000000000000000000000,
        -10314424798490535546171949056000000000000000000000000000000000000
    ]

    print("--- Decimal to Base-60 cunie Conversion ---")
    for num in test_cases:
        print(f"{num} -> {convertNumbersToCuneiform(num)}")

    print(convertNumbersToCuneiform(1320))
    print(convertNumbersToCuneiform(1320, "-"))

    print(convertFloatToCuneiform("5.678"))
    print(convertFloatToCuneiform("5.678", "-"))
    print(convertFloatToCuneiform("-5.678", "-"))
