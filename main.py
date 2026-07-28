from core.aura_core import AuraCore


aura = AuraCore("qwen3:8b")


print("AURA 0.1 Alpha démarrée")
print("Tape 'exit' pour quitter")


while True:

    user = input("\nVous : ")

    if user.lower() == "exit":
        break

    answer = aura.ask(user)

    print("\nAURA :", answer)