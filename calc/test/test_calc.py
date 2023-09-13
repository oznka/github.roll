from prog import byoz_calc



def test_calculator():
    assert byoz_calc.main(3,"+",3) == 6
    assert byoz_calc.main(3,"/",3) == 1
    assert byoz_calc.main(3,"*",3) == 9
    assert byoz_calc.main(3,"-",3) == 0
    assert byoz_calc.main(3,"x",3) == "Calculation has failed"

