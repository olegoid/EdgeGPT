import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

async def main():
    prompt = open("./prompt.txt", encoding="utf-8").read()
    key_phrase = "use prompt"
    
    cookies = json.loads(open("./cookies.json", encoding="utf-8").read())  # might omit cookies option
    bot = await Chatbot.create(cookies=cookies)
    continueConversation = True
    
    while continueConversation:
        user_input = input()
        imageUrl = None
        
        if user_input == key_phrase:
            user_input = prompt
            imageUrl = input("Enter image url:")
        
        response = await bot.ask(
            prompt=user_input,
            conversation_style=ConversationStyle.precise,
            simplify_response=True,
            imageUrl=imageUrl
        )
        print(json.dumps(response, indent=2))
    
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
