typeList = [str, int, float]
def inp(type = str, quote = None, repeatQuote = None, skipable = False):
    ans = None
    if type not in typeList:
        raise NotImplementedError("Unlisted data type: "+str(type))
    else:
        try:
          if not quote:
              ans = type(input())
          else:
              ans = type(input(quote))
          if ans < 1:
              raise ValueError("Positive values only")
        except ValueError:
            if skipable:
                return None
            while (not ans):
              try:
                  if not repeatQuote:
                      ans = type(input())
                  else:
                      ans = type(input(repeatQuote))
                  if ans < 1:
                      ans = None
              except ValueError:
                  ans = None
        return ans

if __name__ == "__main__":
    print("Podporované datové typy: ", typeList)
    typ = float #Přepište pro jiný datový typ
    try:
        a = inp(typ, "Zadejte proměnnou typu "+str(typ)+": ", "Zkuste to znovu: ", True)
        print("Zadali jste: "+str(a)+". Tato hodnota je typu "+str(typ))
    except NotImplementedError:
        print("Ups, takový datový typ neexistuje.")

    input()

    
            