
class Enzyme:
    def __init__(self, acid_chain):
        self._acid_chain = acid_chain

    @property
    def acid_chain(self):
        return self._acid_chain
