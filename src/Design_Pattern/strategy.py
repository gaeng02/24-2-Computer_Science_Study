class Strategy :
    def execute (self) :
        pass

class StrategyA (Strategy) :
    def execute (self) :
        return "Strategy A"

class StrategyB (Strategy) :
    def execute (self) :
        return "Strategy B"

class Context :
    def __init__ (self, strategy) :
        self._strategy = strategy

    def set (self, strategy) :
        self._strategy = strategy

    def execute (self) :
        return self._strategy.execute()


if (__name__ == "__main__") :

    context = Context(StrategyA())
    print(context.execute())

    context.set(StrategyB())
    print(context.execute())
