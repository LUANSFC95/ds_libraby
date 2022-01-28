
class Operations:
    """Classe com operadores matemáticos básicos 
    
    Esta classe reune as seguintes operações entre dois inteiros: adição, multiplicação, subtração e divisão"""

    def __init__(self, **kwargs):
        """Inits Class"""

        self.number_1 = kwargs.get('number_1')
        self.number_2 = kwargs.get('number_2')



    def multiplication(self):
        """Multiply an integer by specific multiplier 

        Perform multiply operation over two integers

        Args:
            number (int): Número a ser multiplicado
            multiplier (int): Multiplicador

        Returns:
            int: Valor da multiplicação entre 'numero' e 'multiplicador'
            
        """

        return (int(self.number_1*self.number_2))

    def division(self):
        """Divide an integer by specific divider 

        Perform division operation over two integers

        Args:
            number (int): Número a ser dividido
            divider (int): Divisor

        Returns:
            float: Valor da divisão entre 'number' e 'divider'
            
        """

        return (float(self.number*self.multiplier))
    