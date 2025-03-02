from flask import Flask, render_template, request
from soap_stub import (
    CountryISOCode, CountryName, CapitalCity,
    CountryCurrency, CountryFlag, CountryIntPhoneCode, FullCountryInfo,
    ListOfContinentsByCode
)

app = Flask(__name__)

# 1️⃣ Récupérer la liste des continents
continents_dict = {continent.sCode: continent.sName for continent in ListOfContinentsByCode()}

@app.route("/", methods=["GET", "POST"])
def index():
    country_info = {}
    error = None

    if request.method == "POST":
        country_name = request.form.get("country", "").strip()

        if not country_name:
            error = "Veuillez entrer un nom de pays."
        else:
            try:
                country_code = CountryISOCode(country_name)

                if not country_code:
                    error = f"Le pays '{country_name}' n'a pas été trouvé."
                else:
                    country_info["name"] = CountryName(country_code) or "Inconnu"
                    country_info["capital"] = CapitalCity(country_code) or "Inconnue"
                    country_info["currency"] = CountryCurrency(country_code)
                    country_info["flag"] = CountryFlag(country_code) or None
                    country_info["phone_code"] = CountryIntPhoneCode(country_code) or "Non défini"

                    full_info = FullCountryInfo(country_code)
                    if full_info:
                        country_info["continent"] = continents_dict.get(getattr(full_info, "sContinentCode", ""), "Non défini")
                        country_info["population"] = getattr(full_info, "sPopulation", "Non définie")
                        country_info["area"] = getattr(full_info, "sAreaInSqKm", "Non définie")
                    else:
                        country_info["continent"] = "Non défini"
                        country_info["population"] = "Non définie"
                        country_info["area"] = "Non définie"

            except Exception as e:
                error = f"Erreur lors de la récupération des données : {str(e)}"

    return render_template("index.html", country_info=country_info, error=error)

if __name__ == "__main__":
    app.run(debug=True)


import pprint

try:
    country_code = CountryISOCode("France")  # Remplace par un pays de test
    full_info = FullCountryInfo(country_code)

    print("🔍 Structure de FullCountryInfo :")
    pprint.pprint(full_info)

except Exception as e:
    print(f"Erreur : {e}")
