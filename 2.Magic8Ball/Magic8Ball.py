import time
import random


responses=[]
responses.append("No")
responses.append("Yes")
responses.append("I don't think so")
responses.append("Depends")
responses.append("Maybe")
responses.append("Try again later")
responses.append("If you want to")
responses.append("If it's cloudy outside")
responses.append("Ask a friend")
responses.append("I'm not feeling it")
responses.append("It sounds promising")
responses.append("I belive so")
responses.append("100%")
responses.append("I think it could happen")
responses.append("Try something else")
responses.append("Try asking something else")

while True:

    the_q = input("\nEnter your question (no to exit): ")
    if the_q == "no":
        time.sleep(1)
        print("\nOkay, Goodbye..")
        time.sleep(1)
        break
    print("\n --- Let me think for a moment ---\n")
    for i in range(5):
        print((i+1)*".")
        time.sleep(1)

    print("\n",random.choice(responses))
