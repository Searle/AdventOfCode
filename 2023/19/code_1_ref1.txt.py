def run():
    x=0
    m=0
    a=0
    s=0
    result=0
    def accept():
        nonlocal result
        result += x + m + a + s
    def c_px():
        if a<2006:
            return c_qkq()
        if m>2090:
            return accept()
        return c_rfg()
    def c_pv():
        if a>1716:
            return
        return accept()
    def c_lnx():
        if m>1548:
            return accept()
        return accept()
    def c_rfg():
        if s<537:
            return c_gd()
        if x>2440:
            return
        return accept()
    def c_qs():
        if s>3448:
            return accept()
        return c_lnx()
    def c_qkq():
        if x<1416:
            return accept()
        return c_crn()
    def c_crn():
        if x>2662:
            return accept()
        return
    def c_in():
        if s<1351:
            return c_px()
        return c_qqz()
    def c_qqz():
        if s>2770:
            return c_qs()
        if m<1801:
            return c_hdj()
        return
    def c_gd():
        if a>3333:
            return
        return
    def c_hdj():
        if m>838:
            return accept()
        return c_pv()
    x=787
    m=2655
    a=1222
    s=2876
    c_in()
    x=1679
    m=44
    a=2067
    s=496
    c_in()
    x=2036
    m=264
    a=79
    s=2244
    c_in()
    x=2461
    m=1339
    a=466
    s=291
    c_in()
    x=2127
    m=1623
    a=2188
    s=1013
    c_in()
    print("RESULT:", result)
run()
