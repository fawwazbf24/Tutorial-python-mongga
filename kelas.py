def ilanginsimbol(var):
    var = var.replace(":", " ").replace("/", " ").replace(")", " ").replace("&", " ")
    var = var.replace("\"", " ").replace("\\", " ").replace("(", " ")
    var = var.strip()

    if not(var.isalnum()):
        if var.startswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")):
            if var[-1] == ".":
                var = var.replace(".", " ")
            elif var[-1] == ",":
                var = var.replace(",", " ")
        else:
            var = var.replace(",", " ").replace(".", " ")

    var = var.strip()
    var2 = var.split()
    return var2
