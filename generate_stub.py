from zeep import Client

# URL du service SOAP
WSDL_URL = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = Client(WSDL_URL)

# Ouvrir le fichier pour écrire le stub
with open("soap_stub.py", "w", encoding="utf-8") as f:
    f.write("from zeep import Client\n\n")
    f.write(f'WSDL_URL = "{WSDL_URL}"\n')
    f.write("client = Client(WSDL_URL)\n\n")

    # Générer des fonctions pour chaque méthode disponible
    for service in client.wsdl.services.values():
        for port in service.ports.values():
            for operation_name, operation in port.binding._operations.items():
                # Récupérer les noms des paramètres d'entrée
                input_params = [param[0] for param in operation.input.body.type.elements]
                param_str = ", ".join(input_params) if input_params else ""
                param_call = ", ".join(f"{p}={p}" for p in input_params)

                # Écrire la fonction correspondante
                f.write(f"def {operation_name}({param_str}):\n")
                f.write(f"    return client.service.{operation_name}({param_call})\n\n")

print("✅ Stub généré : soap_stub.py")
