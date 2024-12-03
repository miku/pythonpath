
# define a string and turn it into uppercase
s = "hello world"
print(s.upper())

# define a multiline string and split it, use different separators
t = """
line 1
line 2
line 3
line 4
"""

print(t.split())
print(t.split("\n"))


text = open("pg53292.txt").read()

print("Chemnitz", text.count("Chemnitz"))
print("Dresden", text.count("Dresden"))
print("Freiberg", text.count("Freiberg"))
print("Görlitz", text.count("Görlitz"))
print("Leipzig", text.count("Leipzig"))
