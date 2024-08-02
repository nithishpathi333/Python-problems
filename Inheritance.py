Q: Inheritance example

  class father():
    def action(self):
        print("he brought me a cycle")
  class son(father):
      def cycle(self):
          print("Riding a cycle")
          
  son().action()
  father().action()

output: 

  he brought me a cycle
  he brought me a cycle

NOTE: [ You are inheriting the father in son's class so when we call son() 
      with action() of father's then its giving the action of father because son is inheriting the properties from father ]

  
