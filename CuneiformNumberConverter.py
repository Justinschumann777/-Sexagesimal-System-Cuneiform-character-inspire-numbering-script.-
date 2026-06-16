def convertNumbersToCuneiform(number: int) -> str:
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

             "𒄦", #34

              "𒎙", #35

               "𒎘", #36

             "𒎗", #37

             "𒎖", #38

              "𒎕", #39

             "𒎔", #40

            "𒎓", #41

              "𒎒", #42

              "𒎐", #43

            "𒎎", #44

              "𒎍", #45

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
    
        
    cunie_digits = []
    position = 0  

    
    # Mathematical Base-60 division loop
    while number > 0: 
        remainder = number % 60
        
        # custom monumental scale rules
        if position == 6 and remainder == 1:
            cunie_digits.append("𒈤") # MAH for 60^6
        elif position == 36 and remainder == 1:
            cunie_digits.append("𒂗") # EN for 60^36
        elif position == 216 and remainder == 1:
            cunie_digits.append("𒀭") # AN for 60^216
        else: 
            cunie_digits.append(cunie_map[remainder])
            
        number //= 60 
        position += 1  # Increment the column counter

    
    cunie_digits.reverse()
    result = "".join(cunie_digits)

    if is_negative:
        return "𒇲" + result  # for negative numbers 
        
    return result

    


    
if __name__ == "__main__":
    # Test basic cases along with a massive test case for 60^6
    # 46656000000 is exactly 60^6
    test_cases = [0, 11, 12, 13, 24, 1320, 46656000000]

    print("--- Decimal to Base-60 cunie Conversion ---")
    for num in test_cases:
        print(f"{num} -> {convertNumbersToCuneiform(num)}")
