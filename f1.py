from collections import defaultdict
class Grammer:
    def __init__(self, productions):
        self.productions= productions
        self.first_set={nt: set for nt in productions}
        self.follow_set={nt: set for nt in productions}
        self.terminal=set()
        self._identify_terminal()
        
    def _identify_terminal(self):
        for rules in self.productions.values():
            for rule in rules:
                for symbol in rule:
                   if not symbol.isupper() and symbol!='eps':
                       self.terminal.append(symbol)
                    
    def _compute_first_sets(self):
        for terminal in self.terminal:
            self.first_set[terminal]={terminal}
            
        for non_terminal in self.productions:
            if not  self.first_set[non_terminal]:
                self.first_set[non_terminal]= self._compute_first(non_terminal)
                
    def _compute_first(self, symbol):
        if not symbol.isupper():
            return {symbol}
        result = set()
        
        for productions in self.productions[symbol]:
            for element in productions:
                first_part = self._compute_first(element)
                result.update(first_part-{'eps'})
                if 'eps' not in first_part:
                    break
                else:
                    result.add('eps')
        return result
    def compute_followset(self):
        start_symbol= next(iter(self.productions))
        self.compute_followset[start_symbol].add('$')
        
        updated = True
        while updated:
            updated = False
            for non_terminal, rules in self.productions.items():
                for rule in rules:
                    follow_temp = self.follow_set[non_terminal].copy()
                    for element in reversed(rule):
                        if element.isupper():
                            if follow_temp-self.follow_set[element]:
                                self.follow_set[element].update(follow_temp)
                                updated= True
                                if 'eps' in self.follow_set[element]:
                                    follow_temp.update(self.first_set[element]-{'eps'})
                                else:
                                    follow_temp=self.first_set[element].copy()
                            else:
                                follow_temp = {element}  
    def display_result(self):
        print("First Set")
        for symbol in sorted(self.first_set):
         print(f"First({symbol}) ={{{", ".join(self.first_set[symbol])}}}")
        
        print("\nFollow Sets:")
        for non_terminal in sorted(self.follow_sets):
            print(f"Follow({non_terminal}) = {{ {', '.join(self.follow_sets[non_terminal])} }}")
if __name__ == "__main__":
    grammar_rules = {}
    num_rules = int(input("Enter the number of productions: "))
    for _ in range(num_rules):
        lhs, rhs = input("Enter production: ").split("->")
        lhs = lhs.strip()
        rhs = [segment.strip().replace("eps", "ε") for segment in rhs.split("|")]
        grammar_rules[lhs] = rhs
    
    grammar_processor = Grammer(grammar_rules)
    grammar_processor._compute_first()
    grammar_processor.compute_followset()
    grammar_processor.display_result()                  
                        
 
        
              
         
                
        
        