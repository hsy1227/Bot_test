def calc_bmi(weight:float,height:float=1.75)->float:
    """
    歡迎光臨:D
    """
    bmi=weight/(height*height)
    return(bmi)

print(calc_bmi(65.0, 1.8))
weight=65.0
height=1.8
print(calc_bmi(weight,height))
print(calc_bmi(weight=65.0,height=1.8))

