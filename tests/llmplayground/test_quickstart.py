from llmplayground.quickstart import ask_for_a_company_name, ask_for_a_company_name_2


def test_ask_for_a_company_name() -> None:
    company_name = ask_for_a_company_name()
    print(repr(company_name))


def test_ask_for_a_company_name_2() -> None:
    company_name = ask_for_a_company_name_2()
    print(repr(company_name))
