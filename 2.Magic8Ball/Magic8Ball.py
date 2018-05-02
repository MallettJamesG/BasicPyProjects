import time

the_q = input("Enter your question: ")
print("\n --- Let me think for a moment ---\n")
for i in range(5):
    print((i+1)*".")
    time.sleep(1)
    
print("I'm done thinking")
