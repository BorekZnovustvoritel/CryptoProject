typeList = ["str", "int", "float"]
def inp(type = "str", quote = None, repeatQuote = None):
    ans = None
    if type not in typeList:
        raise NotImplementedError("Unlisted data type: "+str(type))
    else:
        try:
          if not quote:
              ans = eval("%s(input())" % type, {'input' : input})
          else:
              ans = eval("%s(input('%s'))" % (type, quote), {'input' : input})
        except ValueError:
            while (not ans):
              try:
                  if not repeatQuote:
                      ans = eval("%s(input())" % type, {'input' : input})
                  else:
                      ans = eval("%s(input('%s'))" % (type, repeatQuote), {'input' : input})
              except ValueError:
                  ans = None
        return ans

if __name__ == "__main__":
    print("Podporované datové typy: ", typeList)
    typ = input("Zadejte datový typ: ")
    try:
        a = inp(typ, "Zadejte proměnnou typu "+str(typ)+": ", "Zkuste to znovu: ")
        print("Zadali jste: "+str(a)+". Tato hodnota je typu "+str(typ))
    except NotImplementedError:
        print("Ups, takový datový typ neexistuje.")

    input()

    
            