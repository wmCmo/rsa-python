from module.sync import modInverse
import json

p = int(input("Please enter your P:"))
q = int(input("Please enter your Q:"))
e = int(input("Please enter your Public Key:"), 16)

n = p*q

phi_n = (p-1) * (q-1)

d = modInverse(e, phi_n)


def encode(input, pub, n):
    input = input.split(" ")
    output = list()
    for word in input:
        output.append([((ord(char)**pub) % n) for char in word])
    return output

def decode(cypher, priv, n):
    output = list()
    for word in cypher:
        output.append("".join([chr((int(num)**priv) % n) for num in word]))
    return output

def main():
    choice = input("What do you want to do? (e)ncrypt/(d)ecrypt:")
    if choice == "e":
        inp = input("Input your message:")
        print(encode(inp, e, n))
        input()
    else:
        cypher = input("Input your cypher:" )
        cypher = json.loads(cypher)
        print(decode(cypher, d, n))
        input()
main()