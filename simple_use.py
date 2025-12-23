from browser_use import Agent, Browser, ChatBrowserUse
import asyncio

# set BROWSER_USE_API_KEY=your-key in the environment to use Browser Use Cloud

async def example():
    browser = Browser()

    llm = ChatBrowserUse()

    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=llm,
        browser=browser,
    )

    history = await agent.run()
    return history

if __name__ == "__main__":
    history = asyncio.run(example())