import asyncio
import random
import string
import pandas as pd

from browser_use import Agent, Browser, ChatBrowserUse


def random_password(length=12):
    """Generate a random password with letters, digits & symbols."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

def get_random_name():
    """Generate a name from predefined first and last names in the csv files."""
    first_names = pd.read_csv("first_names.csv")['first_name'].tolist()
    last_names = pd.read_csv("last_names.csv")['last_name'].tolist()
    first = random.choice(first_names)
    last = random.choice(last_names)
    return f"{first} {last}"

async def create_email_and_password():
    """Step 1: Create a temporary email and password."""
    print("\n" + "="*50)
    print("STEP 1: Creating temporary email and password")
    print("="*50)
    
    browser = Browser(
        # use_cloud=True,
    )
    llm = ChatBrowserUse()

    agent = Agent(
        task="""
        1) Open https://tmailor.com/
        3) Click on new email button if email is not visible
        2) Copy the temporary email shown on screen once it loads
        Return only the email text.
        """,
        llm=llm,
        browser=browser,
    )

    try:
        history = await agent.run()

        # Parse email out of agent history
        email = None
        # Check the final result from the agent
        if history and hasattr(history, 'final_result'):
            email = history.final_result()
        
        # Try parsing the history list
        if not email and isinstance(history, list):
            for entry in history:
                if isinstance(entry, dict):
                    # Check various possible keys
                    for key in ['text', 'result', 'output', 'final_result']:
                        if key in entry and entry[key]:
                            text = str(entry[key]).strip()
                            if "@" in text and "." in text:
                                email = text
                                break
                if email:
                    break
        
        # Check if history itself is a string
        if not email and isinstance(history, str) and "@" in history:
            email = history.strip()

        if not email:
            print("❌ Failed to extract an email.")
            print(f"Debug - History type: {type(history)}")
            print(f"Debug - History content: {history}")
            return None, None

        # Generate a password
        pwd = random_password()

        # Append to CSV
        df = pd.DataFrame([{"email": email, "password": pwd}])

        try:
            # Try to append to existing file
            existing = pd.read_csv("email-password.csv")
            df = pd.concat([existing, df], ignore_index=True)
        except FileNotFoundError:
            pass

        df.to_csv("email-password.csv", index=False)

        print(f"✅ Saved: {email} / {pwd}")
        return email, pwd
    
    finally:
        print("🔒 Browser session ended for Step 1")


async def create_heatmap(email, pwd, random_name):
    """Step 2: Signup and create heatmap using the credentials."""
    print("\n" + "="*50)
    print("STEP 2: Signing up and creating heatmap")
    print("="*50)
    print(f"📧 Using email: {email}")
    
    browser = Browser(
        # use_cloud=True,
    )
    llm = ChatBrowserUse()
    
    signup_agent = Agent(
        task=f"""
        1) Navigate to "https://example.com/login"
        2) Find and click the signup button or link
        3) Fill in the signup form with:
           - Email: {email}
           - Password: {pwd}
           - Tick the checkbox to agree to terms and conditions
           - Press the signup for free button
        4) If a form appears asking for additional information, fill it in:
           - Name: {random_name}
           - Any additional info: Fill as required
        5) Submit the form
        6) Then end the task
        """,
        llm=llm,
        browser=browser,
    )
    
    try:
        signup_history = await signup_agent.run()
        print(f"✅ Heatmap creation process completed!")
        return signup_history
    finally:
        print("🔒 Browser session ended for Step 2")


async def run_full_workflow():
    """Run the complete workflow: create email -> create heatmap."""
    print("\n" + "="*50)
    print("🚀 STARTING FULL WORKFLOW")
    print("="*50)
    
    # Step 1: Create email and password
    email, pwd = await create_email_and_password()
    
    if not email or not pwd:
        print("\n❌ Workflow failed: Could not create email and password")
        return
    
    # Wait a moment before starting next step
    print("\n⏳ Waiting 2 seconds before starting heatmap creation...")
    await asyncio.sleep(2)

    # Step 2: Get random name
    random_name = get_random_name()
    
    # Step 3: Create heatmap
    await create_heatmap(email, pwd, random_name)
    
    print("\n" + "="*50)
    print("✅ FULL WORKFLOW COMPLETED SUCCESSFULLY!")
    print("="*50)


if __name__ == "__main__":
    asyncio.run(run_full_workflow())
