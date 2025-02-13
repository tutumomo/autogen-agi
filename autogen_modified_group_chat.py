"""
This is an example of a modified group chat using some of the agents in the agents/agents.py file. Compare these results to the results from autogen_standard_group_chat.py.
"""
import logging
import os

from autogen_mods.modified_group_chat import ModifiedGroupChat, ModifiedGroupChatManager

from agents.agents import (
    user_proxy,
    code_reviewer,
    agent_awareness_expert,
    python_expert,
    function_calling_agent,
    agi_gestalt_agent,
    creative_solution_agent,
    first_principles_thinker_agent,
    out_of_the_box_thinker_agent,
    strategic_planning_agent,
    project_manager_agent,
    efficiency_optimizer_agent,
    emotional_intelligence_expert_agent,
    task_history_review_agent,
    task_comprehension_agent,
)

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
"""
config_list3 = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": os.environ["OPENAI_API_KEY"],
    }
]

config_list4 = [
    {
        "model": "gpt-4-1106-preview",
        "api_key": os.environ["OPENAI_API_KEY"],
    }
]

llm_config4 = {
    "seed": 42,
    "config_list": config_list4,
    "temperature": 0.1,
}
"""
"""
20240219，此處列表更新為5類
gpt35、gpt4、gpt4v、gemini、gemini_vision
"""
config_list_gpt35 = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-3.5-turbo", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-16k", "gpt-3.5-turbo-16k-0613"],
    },
)
config_list_gpt4 = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4", "gpt-4-0613", "gpt-4-0314", "gpt-4-1106-preview"],
    },
)
config_list_gpt4v = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4-vision-preview", "dalle"],
    },
)
config_list_gemini = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gemini-pro"],
    },
)
config_list_gemini_vision = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gemini-pro-vision"],
    },
)
llm_config = {
    "seed": 42,
    "config_list": config_list_gemini,
    "temperature": 0.1,
}

AGENT_TEAM = [
    user_proxy,
    code_reviewer,
    agent_awareness_expert,
    python_expert,
    function_calling_agent,
    # agi_gestalt_agent,
    creative_solution_agent,
    first_principles_thinker_agent,
    # out_of_the_box_thinker_agent,
    # strategic_planning_agent,
    project_manager_agent,
    # efficiency_optimizer_agent,
    # emotional_intelligence_expert_agent,
    task_history_review_agent,
    task_comprehension_agent
]

groupchat = ModifiedGroupChat(
    agents=AGENT_TEAM,
    messages=[],
    max_round=100,
    use_agent_council=True,
    inject_agent_council=True,
    continue_chat=False,
)
manager = ModifiedGroupChatManager(groupchat=groupchat, llm_config=llm_config)

# NOTE: If the agents succussfully run their own autogen script, you will have to give it some time to process then press enter to exit the nested script.

message = """I'm interested in building autonomous agents using the autogen python library. Can you show me a complete example of how to do this? The example should show how to correctly configure and instantiate autogen automous agents. The request given to the agents will be: "Please write and then execute a python script that prints 10 dad jokes". I want the agents to run completely autonomously without any human intervention."""

user_proxy.initiate_chat(
    manager,
    clear_history=False,
    message=message,
)

