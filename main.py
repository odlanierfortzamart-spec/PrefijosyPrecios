from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Diccionario de prefijos a países
prefix_to_country = {
    "93": "Afganistán",
    "355": "Albania",
    "49": "Alemania",
    "376": "Andorra",
    "244": "Angola",
    "1-268": "Antigua y Barbuda",
    "966": "Arabia Saudita",
    "213": "Argelia",
    "54": "Argentina",
    "374": "Armenia",
    "61": "Australia",
    "43": "Austria",
    "994": "Azerbaiyán",
    "1-242": "Bahamas",
    "880": "Bangladés",
    "1-246": "Barbados",
    "973": "Baréin",
    "32": "Bélgica",
    "501": "Belice",
    "229": "Benín",
    "375": "Bielorrusia",
    "95": "Birmania (Myanmar)",
    "591": "Bolivia",
    "387": "Bosnia y Herzegovina",
    "267": "Botsuana",
    "55": "Brasil",
    "673": "Brunéi",
    "359": "Bulgaria",
    "226": "Burkina Faso",
    "257": "Burundi",
    "975": "Bután",
    "238": "Cabo Verde",
    "855": "Camboya",
    "237": "Camerún",
    "1": "Canadá / Estados Unidos",
    "974": "Catar",
    "235": "Chad",
    "56": "Chile",
    "86": "China",
    "357": "Chipre",
    "57": "Colombia",
    "269": "Comoras",
    "850": "Corea del Norte",
    "82": "Corea del Sur",
    "225": "Costa de Marfil",
    "506": "Costa Rica",
    "385": "Croacia",
    "53": "Cuba",
    "45": "Dinamarca",
    "1-767": "Dominica",
    "593": "Ecuador",
    "20": "Egipto",
    "503": "El Salvador",
    "971": "Emiratos Árabes Unidos",
    "421": "Eslovaquia",
    "386": "Eslovenia",
    "34": "España",
    "372": "Estonia",
    "251": "Etiopía",
    "63": "Filipinas",
    "358": "Finlandia",
    "679": "Fiyi",
    "33": "Francia",
    "241": "Gabón",
    "220": "Gambia",
    "995": "Georgia",
    "233": "Ghana",
    "30": "Grecia",
    "1-473": "Granada",
    "502": "Guatemala",
    "224": "Guinea",
    "245": "Guinea-Bisáu",
    "240": "Guinea Ecuatorial",
    "592": "Guyana",
    "509": "Haití",
    "504": "Honduras",
    "36": "Hungría",
    "91": "India",
    "62": "Indonesia",
    "964": "Irak",
    "98": "Irán",
    "353": "Irlanda",
    "354": "Islandia",
    "972": "Israel",
    "39": "Italia",
    "1-876": "Jamaica",
    "81": "Japón",
    "962": "Jordania",
    "7": "Rusia / Kazajistán",
    "254": "Kenia",
    "996": "Kirguistán",
    "686": "Kiribati",
    "965": "Kuwait",
    "856": "Laos",
    "371": "Letonia",
    "961": "Líbano",
    "231": "Liberia",
    "218": "Libia",
    "423": "Liechtenstein",
    "370": "Lituania",
    "352": "Luxemburgo",
    "261": "Madagascar",
    "60": "Malasia",
    "265": "Malaui",
    "960": "Maldivas",
    "223": "Malí",
    "356": "Malta",
    "212": "Marruecos",
    "230": "Mauricio",
    "222": "Mauritania",
    "52": "México",
    "373": "Moldavia",
    "377": "Mónaco",
    "976": "Mongolia",
    "382": "Montenegro",
    "258": "Mozambique",
    "264": "Namibia",
    "674": "Nauru",
    "977": "Nepal",
    "505": "Nicaragua",
    "227": "Níger",
    "234": "Nigeria",
    "47": "Noruega",
    "64": "Nueva Zelanda",
    "968": "Omán",
    "31": "Países Bajos",
    "92": "Pakistán",
    "680": "Palaos",
    "507": "Panamá",
    "675": "Papúa Nueva Guinea",
    "595": "Paraguay",
    "51": "Perú",
    "48": "Polonia",
    "351": "Portugal",
    "44": "Reino Unido",
    "236": "República Centroafricana",
    "420": "República Checa",
    "1-809": "República Dominicana",
    "250": "Ruanda",
    "40": "Rumanía",
    "685": "Samoa",
    "1-869": "San Cristóbal y Nieves",
    "378": "San Marino",
    "1-758": "Santa Lucía",
    "1-784": "San Vicente y las Granadinas",
    "221": "Senegal",
    "381": "Serbia",
    "248": "Seychelles",
    "232": "Sierra Leona",
    "65": "Singapur",
    "963": "Siria",
    "252": "Somalia",
    "94": "Sri Lanka",
"27": "Sudáfrica",
    "249": "Sudán",
    "46": "Suecia",
    "41": "Suiza",
    "597": "Surinam",
    "66": "Tailandia",
    "886": "Taiwán",
    "255": "Tanzania",
    "992": "Tayikistán",
    "670": "Timor Oriental",
"228": "Togo",
    "676": "Tonga",
    "1-868": "Trinidad y Tobago",
    "216": "Túnez",
    "90": "Turquía",
    "380": "Ucrania",
    "256": "Uganda",
    "598": "Uruguay",
    "998": "Uzbekistán",
    "58": "Venezuela",
    "84": "Vietnam",
    "967": "Yemen",
    "260": "Zambia",
    "263": "Zimbabue"
}

# Diccionario inverso: país a prefijo
country_to_prefix = {v.lower(): k for k, v in prefix_to_country.items()}

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola 👋\n\nUsa comandos como:\n"
        "/34 → te diré el país\n"
        "/mexico → te diré el prefijo\n"
        "/precio → ver lista de precios"
    )

# Comando /precio
async def handle_precio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = "📋 Lista de precios por prefijo:\n\n"
    for prefijo, pais in prefix_to_country.items():
        mensaje += f"• +{prefijo} ({pais}): Por Definir\n"

    botones = [
        [InlineKeyboardButton("@OdlanierFM", url="https://t.me/OdlanierFM")],
        [InlineKeyboardButton("@sr_alpha_crypto", url="https://t.me/sr_alpha_crypto")]
    ]
    reply_markup = InlineKeyboardMarkup(botones)

    await update.message.reply_text(mensaje, reply_markup=reply_markup)

# Comandos tipo /34 (prefijo)
async def handle_prefijo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text[1:]
    if code in prefix_to_country:
        pais = prefix_to_country[code]
        await update.message.reply_text(f"El prefijo +{code} es de {pais}.")
    else:
        await update.message.reply_text("No reconozco ese prefijo.")

# Comandos tipo /mexico (nombre de país)
async def handle_pais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nombre = update.message.text[1:].strip().lower()
    if nombre.isalpha():
        prefijo = country_to_prefix.get(nombre)
        if prefijo:
            await update.message.reply_text(f"El prefijo de {nombre.title()} es +{prefijo}.")
        else:
            await update.message.reply_text("No reconozco ese país.")
    else:
        return

# Ignorar todo lo demás
async def ignorar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return

# Configuración del bot
def main():
    TOKEN = "7952223856:AAEoLQsKXZAzdzzhk14e7D_Ocpc3g2jo80c"  # Reemplaza con tu token real
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("precio", handle_precio))
    app.add_handler(MessageHandler(filters.Regex(r"^/\d+$"), handle_prefijo))
    app.add_handler(MessageHandler(filters.Regex(r"^/[a-zA-ZáéíóúñÑ]+$"), handle_pais))
    app.add_handler(MessageHandler(filters.ALL, ignorar))

    print("Bot activo...")
    app.run_polling()


if __name__ == "__main__":
    main()
