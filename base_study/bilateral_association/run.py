from modulos import Casa, Pessoa

casa_da_ana = Casa()
ana = Pessoa("Ana")

ana.salvar_local(casa_da_ana)
casa_da_ana.salve_proprietario(ana)

proprietario = casa_da_ana.buscar_proprietario()
proprietario.se_apresentar()
