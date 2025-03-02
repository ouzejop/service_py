from zeep import Client
from zeep.helpers import serialize_object

WSDL_URL = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = Client(WSDL_URL)

def ListOfContinentsByName():
    return client.service.ListOfContinentsByName()

def ListOfContinentsByCode():
    return client.service.ListOfContinentsByCode()

def ListOfCurrenciesByName():
    return client.service.ListOfCurrenciesByName()

def ListOfCurrenciesByCode():
    return client.service.ListOfCurrenciesByCode()

def CurrencyName(sCurrencyISOCode):
    return client.service.CurrencyName(sCurrencyISOCode=sCurrencyISOCode)

def ListOfCountryNamesByCode():
    return client.service.ListOfCountryNamesByCode()

def ListOfCountryNamesByName():
    return client.service.ListOfCountryNamesByName()

def ListOfCountryNamesGroupedByContinent():
    return client.service.ListOfCountryNamesGroupedByContinent()

def CountryName(sCountryISOCode):
    return client.service.CountryName(sCountryISOCode=sCountryISOCode)

def CountryISOCode(sCountryName):
    return client.service.CountryISOCode(sCountryName=sCountryName)

def CapitalCity(sCountryISOCode):
    return client.service.CapitalCity(sCountryISOCode=sCountryISOCode)

def CountryCurrency(sCountryISOCode):
    return client.service.CountryCurrency(sCountryISOCode=sCountryISOCode)

def CountryFlag(sCountryISOCode):
    return client.service.CountryFlag(sCountryISOCode=sCountryISOCode)

def CountryIntPhoneCode(sCountryISOCode):
    return client.service.CountryIntPhoneCode(sCountryISOCode=sCountryISOCode)

def FullCountryInfo(sCountryISOCode):
    response = client.service.FullCountryInfo(sCountryISOCode=sCountryISOCode)
    return serialize_object(response)
def FullCountryInfoAllCountries():
    return client.service.FullCountryInfoAllCountries()

def CountriesUsingCurrency(sISOCurrencyCode):
    return client.service.CountriesUsingCurrency(sISOCurrencyCode=sISOCurrencyCode)

def ListOfLanguagesByName():
    return client.service.ListOfLanguagesByName()

def ListOfLanguagesByCode():
    return client.service.ListOfLanguagesByCode()

def LanguageName(sISOCode):
    return client.service.LanguageName(sISOCode=sISOCode)

def LanguageISOCode(sLanguageName):
    return client.service.LanguageISOCode(sLanguageName=sLanguageName)

def ListOfContinentsByName():
    return client.service.ListOfContinentsByName()

def ListOfContinentsByCode():
    return client.service.ListOfContinentsByCode()

def ListOfCurrenciesByName():
    return client.service.ListOfCurrenciesByName()

def ListOfCurrenciesByCode():
    return client.service.ListOfCurrenciesByCode()

def CurrencyName(sCurrencyISOCode):
    return client.service.CurrencyName(sCurrencyISOCode=sCurrencyISOCode)

def ListOfCountryNamesByCode():
    return client.service.ListOfCountryNamesByCode()

def ListOfCountryNamesByName():
    return client.service.ListOfCountryNamesByName()

def ListOfCountryNamesGroupedByContinent():
    return client.service.ListOfCountryNamesGroupedByContinent()

def CountryName(sCountryISOCode):
    return client.service.CountryName(sCountryISOCode=sCountryISOCode)

def CountryISOCode(sCountryName):
    return client.service.CountryISOCode(sCountryName=sCountryName)

def CapitalCity(sCountryISOCode):
    return client.service.CapitalCity(sCountryISOCode=sCountryISOCode)

def CountryCurrency(sCountryISOCode):
    return client.service.CountryCurrency(sCountryISOCode=sCountryISOCode)

def CountryFlag(sCountryISOCode):
    return client.service.CountryFlag(sCountryISOCode=sCountryISOCode)

def CountryIntPhoneCode(sCountryISOCode):
    return client.service.CountryIntPhoneCode(sCountryISOCode=sCountryISOCode)

def FullCountryInfo(sCountryISOCode):
    return client.service.FullCountryInfo(sCountryISOCode=sCountryISOCode)

def FullCountryInfoAllCountries():
    return client.service.FullCountryInfoAllCountries()

def CountriesUsingCurrency(sISOCurrencyCode):
    return client.service.CountriesUsingCurrency(sISOCurrencyCode=sISOCurrencyCode)

def ListOfLanguagesByName():
    return client.service.ListOfLanguagesByName()

def ListOfLanguagesByCode():
    return client.service.ListOfLanguagesByCode()

def LanguageName(sISOCode):
    return client.service.LanguageName(sISOCode=sISOCode)

def LanguageISOCode(sLanguageName):
    return client.service.LanguageISOCode(sLanguageName=sLanguageName)

 