"""
Developed by Nikolas Schildberg
For taubatexas Python lessons

"""
#intro
print("\nHello there! Welcome to this simples program!\n")

#print("Please enter your name:")
#nome_do_usuario = input()
nome_do_usuario = "Nikolas"

#print("Welcome, "+nome_do_usuario+"!")
mensagem = "Welcome, "+nome_do_usuario+"!"
print(mensagem)

#age = input("How old are you?")
#print("Really? You do look ",age/2,".",sep="")

#age=54
age = input("How old are you? ")
age = int(age)
print("Really? You look only ",round(age/2),"!","\nNice to see you!\n",sep="")
