import re
marcas = ["Kingston", "Corsair", "XPG", "Adata", "Husky", "Rise Mode",
          "Crucial", "HyperX", "PCYes", "Hiksemi", "Keepdata","Clanm", "Spectrum", "Best Memory", "Dale7", "Macrovip", "Patriot", "Sgmax", "Synex", "Hikvision"]

def separar(titulo):
    return {
        "marca": _achar_marca(titulo),
        "capacidade": _buscar(r"(\d+)\s*GB", titulo),                  
        "frequencia": _buscar(r"(\d{3,4})\s*(?:MHz|MT/s)", titulo),
        "tipo": _buscar(r"(DDR\dL?)", titulo),                        
        "notebook": bool(re.search(r"notebook|sodimm|so-dimm", titulo, re.I)),
    }

def _buscar(padrao, texto):
    achou = re.search(padrao, texto, re.I)
    return achou.group(1).upper().replace(" ", "") if achou else None

def _achar_marca(titulo):
    for marca in marcas:
        if marca.lower() in titulo.lower():
            return marca
    return None