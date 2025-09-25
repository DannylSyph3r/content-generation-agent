"""
Agent runner utilities for Smart Routing Pipeline
Handles agent execution and session management
"""
from google.adk.agents import LlmAgent
from google.adk.runners import InMemoryRunner
from google.genai import types


async def run_single_agent(agent: LlmAgent, user_id: str, session_id: str, 
                          input_text: str) -> str:
    """
    Run a single agent and return its output.
    
    Args:
        agent: The LlmAgent to run
        user_id: User identifier
        session_id: Session identifier
        input_text: Input text/prompt for the agent
        
    Returns:
        Agent's response as string
    """
    try:
        # Create runner for individual agent
        runner = InMemoryRunner(agent)
        
        # Create session
        await runner.session_service.create_session(
            app_name=runner.app_name,
            user_id=user_id,
            session_id=session_id
        )
        
        # Create input content
        user_content = types.Content(
            role='user',
            parts=[types.Part(text=input_text)]
        )
        
        # Execute agent
        final_result = ""
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=user_content
        ):
            if event.is_final_response() and event.content:
                if hasattr(event.content, 'text') and event.content.text:
                    final_result = event.content.text
                elif event.content.parts:
                    text_parts = [part.text for part in event.content.parts 
                                if hasattr(part, 'text') and part.text]
                    final_result = "".join(text_parts)
                break
        
        return final_result
        
    except Exception as e:
        error_msg = f"Error running {agent.name}: {str(e)}"
        print(error_msg)
        return error_msg