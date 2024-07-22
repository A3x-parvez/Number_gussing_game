from random import randint

num=randint(1,100)

user_guess=-1
guess_count=0

print("\n----------------------------------------------------------------")

while(num!=user_guess):
    guess_count=guess_count+1
    user_guess=int(input("Guess the number : "))
    
    if(num>user_guess):
        print("Higher number Please.")
    elif(num==user_guess):
        break
    elif(num<user_guess):
        print("Lower number please.")
        
print(f"Woo Hoo ! You guess the number {num} in {guess_count} atemps.")

print("\n----------------------------------------------------------------")