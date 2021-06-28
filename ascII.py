def header():
    print("""                                                                          
            _/_/_/                _/_/_/  _/    _/    _/_/    _/          _/_/    
           _/    _/  _/    _/  _/        _/  _/    _/    _/  _/        _/    _/   
          _/_/_/    _/    _/    _/_/    _/_/      _/    _/  _/        _/_/_/_/    
         _/        _/    _/        _/  _/  _/    _/    _/  _/        _/    _/     
        _/          _/_/_/  _/_/_/    _/    _/    _/_/    _/_/_/_/  _/    _/      
                       _/                                                         
                  _/_/
        """)
    print("""
                    ir neskauda tau galvos del paitono paskolos . . . 
    """)
def main_meniu():
    print("""
[1] Įvesti paskolos duomenis [2] Sesijos istorija [3] Baigti darbą
    """)

def meniu2():
    print("""
[1] Paskolos mokejimo grafikas [2] Baigti darba
    """)

def info(amount, period, intrate):
    print(f"""
+-----------------------------------------------------------------+
|           P.A.S.K.O.L.O.S   I.N.F.O.R.M.A.C.I.J.A               |
+-----------------------------------------------------------------+
 Paskolos suma(Eur.)     Paskolos trukme(men.)       Palukanos(%)
        {amount}                        {period}                     {intrate}
          
    """)

def tbl():
    print("""
+-----------------------------------------------------------------+
|                  Linijinio mokėjimo grafikas                    |
+-----------------------------------------------------------------+
        """)

def hstr():
    print("""
+-----------------------------------------------------------------+
|                        ISTORIJA                                 |
+-----------------------------------------------------------------+
            """)

def godbye():
    print('Bye')