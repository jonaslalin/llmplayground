from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


def ask_for_a_company_name() -> str:
    llm = OpenAI(temperature=0.9)  # type: ignore[call-arg]
    query = "What would be a good company name for a company that makes colorful socks?"
    print(query)
    return llm(query)


def ask_for_a_company_name_2() -> str:
    llm = OpenAI(temperature=0.9)  # type: ignore[call-arg]
    prompt = PromptTemplate(
        template="What is a good name for a company that makes {product}?",
        input_variables=["product"],
    )
    query = prompt.format(product="colorful socks")
    print(query)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run("colorful socks")
