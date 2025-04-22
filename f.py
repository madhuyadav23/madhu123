from collections import defaultdict

class GrammarProcessor:
    def __init__(self, productions):
        self.productions = productions
        self.first_sets = {nt: set() for nt in productions}
        self.follow_sets = {nt: set() for nt in productions}
        self.terminals = set()
        self._identify_terminals()
    
    def _identify_terminals(self):
        for rules in self.productions.values():
            for rule in rules:
                for symbol in rule:
                    if not symbol.isupper() and symbol != 'ε':
                        self.terminals.add(symbol)

    def compute_first_sets(self): 
        for terminal in self.terminals:
            self.first_sets[terminal] = {terminal}

        for non_terminal in self.productions:
            if not self.first_sets[non_terminal]:
                self.first_sets[non_terminal] = self._compute_first(non_terminal)
    
    def _compute_first(self, symbol):
        if not symbol.isupper():
            return {symbol}
        
        result = set()
        for production in self.productions[symbol]:
            for element in production:
                first_part = self._compute_first(element)
                result.update(first_part - {'ε'})
                if 'ε' not in first_part:
                    break
            else:
                result.add('ε')
        
        return result
    
    def compute_follow_sets(self):
        start_symbol = next(iter(self.productions))
        self.follow_sets[start_symbol].add('$')
        
        updated = True
        while updated:
            updated = False
            for non_terminal, rules in self.productions.items():
                for rule in rules:
                    follow_temp = self.follow_sets[non_terminal].copy()
                    for element in reversed(rule):
                        if element.isupper():
                            if follow_temp - self.follow_sets[element]:
                                self.follow_sets[element].update(follow_temp)
                                updated = True
                            if 'ε' in self.first_sets[element]:
                                follow_temp.update(self.first_sets[element] - {'ε'})
                            else:
                                follow_temp = self.first_sets[element].copy()
                        else:
                            follow_temp = {element}
    
    def display_results(self):
        print("First Sets:")
        for symbol in sorted(self.first_sets):
            print(f"First({symbol}) = {{ {', '.join(self.first_sets[symbol])} }}")

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
    
    grammar_processor = GrammarProcessor(grammar_rules)
    grammar_processor.compute_first_sets()
    grammar_processor.compute_follow_sets()
    grammar_processor.display_results()
