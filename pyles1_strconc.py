# String concatenation ways

pronome = "Excelentíssimo"
name = "Fulano" # some string variable
surname = "de Tal"

print("\nSeu nome é "+ name +" e seu sobrenome é " + surname)

print("\nSeu nome é",name,"e seu sobrenome é",surname)

print("\nSeu nome é {} e seu sobrenome é {}".format(name,surname))

print(f"\nSeu nome é {name} e seu sobrenome é {surname}\n")

# another example to use the concatenation string

# Let´s create a a text for e-mail and insert the data into the fix text

direct_mail =  f"\n {pronome} senhor(a) {name}, \ncomo tem passado? \
    \nGostariamos muito que você revissase seus dados de nome \"{name}\" e sobrenome \"{surname}\" para ter o dado correto em nossa base \
        "
print(direct_mail)