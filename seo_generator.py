# seo_generator_single_class.py

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import Tool
from langchain_core.messages import HumanMessage, ToolMessage
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

class SEOGenerator:
    def generate_description(self, input: dict):
        llm = ChatOpenAI(temperature=0.3)
        
        @tool
        def get_SEO_description_for_Tshirts():
            """Tshirts SEO keywords"""
            return ["Pattern", "Fit type", "Sleeve", "Collar style", "Length"] 
            

        @tool
        def get_SEO_description_for_laptop():
            """Laptop SEO keywords"""
            return ["RAM", "PROCESSOR", "SCREEN_SIZE", "STORAGE", "MEMORY", "OS"]

        @tool
        def get_SEO_description_for_coffee_machine():
            """Coffee machine SEO keywords"""
            return ["Pressure", "Power", "Control Type", "Water Capacity", "Build Material"]

        @tool
        def get_SEO_description_for_shoes():
            """Shoes SEO keywords"""
            return ["Material type", "Closure type", "Heel type", "Water resistance level", "Sole material", "Style"]

        tools = [
            Tool(name="get_SEO_description_for_Tshirts", func=get_SEO_description_for_Tshirts, description="Tshirts SEO keywords"),
            Tool(name="get_SEO_description_for_laptop", func=get_SEO_description_for_laptop, description="Laptop SEO keywords"),
            Tool(name="get_SEO_description_for_coffee_machine", func=get_SEO_description_for_coffee_machine, description="Coffee machine SEO keywords"),
            Tool(name="get_SEO_description_for_shoes", func=get_SEO_description_for_shoes, description="Shoes SEO keywords"),
        ]

        llm_with_tools = llm.bind_tools(tools)

        query = HumanMessage(content=f"""
            The product details are {input}.
            Generate a compelling product description for an e-commerce listing using the given product details.
            Write description using key words from the tools for those who are in product details only.
        """)

        messages = [query]
        result = llm_with_tools.invoke(messages)
        messages.append(result)

        tool_call_id = result.tool_calls[0]['id']
        tool_call_name = result.tool_calls[0]['name']

        if tool_call_name== "get_SEO_description_for_Tshirts":
                print("Tshirt")
                tool_result = get_SEO_description_for_Tshirts.invoke({})  # No input expected for this tool
                messages.append(ToolMessage(tool_call_id=tool_call_id, content=str(tool_result)))
                
        if tool_call_name== "get_SEO_description_for_laptop":
                print("laptop")
                tool_result = get_SEO_description_for_laptop.invoke({})
                messages.append(ToolMessage(tool_call_id=tool_call_id, content=str(tool_result)))

        if tool_call_name== "get_SEO_description_for_coffee_machine":
                print("coffe")
                tool_result = get_SEO_description_for_coffee_machine.invoke({})
                messages.append(ToolMessage(tool_call_id=tool_call_id, content=str(tool_result)))

        if tool_call_name== "get_SEO_description_for_shoes":
                print("shoes")
                tool_result = get_SEO_description_for_shoes.invoke({})
                messages.append(ToolMessage(tool_call_id=tool_call_id, content=str(tool_result)))

        
        final_result = llm_with_tools.invoke(messages)

        print("User input is as product features:", input)
        print("SEO description for product:", final_result.content)
        return final_result.content



obj=SEOGenerator()
obj.generate_description({"title":"Tshirts", "features":["Solid", "Regular Fit", "Half Sleeve", "Band Collar", "Standard Length"]})